from django.db import models
import os

def property_image_upload_path(instance, filename):
    return os.path.join('property_images', filename)

class Property(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    area = models.DecimalField(max_digits=8, decimal_places=2, help_text="Square footage or square meters")
    image = models.ImageField(upload_to=property_image_upload_path, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title