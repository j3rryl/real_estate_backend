from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'location', 'image', 'created_at')
    search_fields = ('title', 'location')
    # list_filter = ('is_available',)

    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 50px; height: auto;" />'
        return "No Image"

    image_tag.allow_tags = True
    image_tag.short_description = "Image"