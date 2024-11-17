from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    format_choices = [
        ('png', 'PNG'),
        ('jpeg', 'JPEG'),
        ('jpg', 'JPG'),
        ('ico', 'ICO'),
        ('bmp', 'BMP'),
        ('tiff', 'TIFF'),
        ('webp', 'WEBP'),
    ]
    format = models.CharField(max_length=10, choices=format_choices, default='png')
    uploaded_at = models.DateTimeField(auto_now_add=True)
