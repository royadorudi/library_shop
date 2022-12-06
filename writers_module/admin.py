from django.contrib import admin
from .models import Writers, Translators


class WritersAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'is_delete']


class TranslatorAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'is_delete']


admin.site.register(Writers, WritersAdmin)
admin.site.register(Translators, TranslatorAdmin)
