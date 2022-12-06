from django.contrib import admin
from .models import BookCategory, Books, BookComments


class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer', 'translator', 'is_active', 'submit_date']


class BookCommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'submit_date']


admin.site.register(BookCategory)
admin.site.register(Books, BooksAdmin)
admin.site.register(BookComments, BookCommentsAdmin)
