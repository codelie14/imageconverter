from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
from .forms import ImageUploadForm
import os

def image_converter(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            format = form.cleaned_data['format']

            # Sauvegarder l'image temporairement
            fs = FileSystemStorage()
            filename = fs.save(image_file.name, image_file)
            uploaded_image_path = fs.path(filename)

            # Conversion de l'image
            img = Image.open(uploaded_image_path)
            output_path = f"{uploaded_image_path.rsplit('.', 1)[0]}.{format}"
            img.save(output_path, format=format.upper())

            # Supprimer l'image temporaire initiale
            os.remove(uploaded_image_path)

            return render(request, 'converter/result.html', {'output_path': output_path})
    else:
        form = ImageUploadForm()
    return render(request, 'converter/upload.html', {'form': form})
