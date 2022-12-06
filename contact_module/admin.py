from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'is_read_by_admin']


admin.site.register(ContactUs, ContactUsAdmin)
