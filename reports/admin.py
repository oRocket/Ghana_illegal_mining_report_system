from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import BlogPost

@admin.register(BlogPost)  # Use the decorator or admin.site.register, not both
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    
    # Override the formfield for TextField to use TinyMCE
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }
