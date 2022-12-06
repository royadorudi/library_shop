from django.contrib import admin
from .models import BlogList


class BlogListAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_active']
    list_editable = ['is_active']


admin.site.register(BlogList, BlogListAdmin)
