from django.db import models
from books_module.models import Books


class Writers(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    url_title = models.CharField(max_length=250, verbose_name='عنوان در url')
    book = models.ManyToManyField(to=Books, related_name='book_writer', verbose_name='نویسنده ی کتاب')
    about = models.TextField(verbose_name='درباره')
    image = models.ImageField(upload_to='images/writers', null=True, blank=True,
                              verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال شده/نشده')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/نشده')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'


class Translators(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    url_title = models.CharField(max_length=250, verbose_name='عنوان در url')
    book = models.ManyToManyField(to=Books, related_name='book_translator', verbose_name='مترجم کتاب')
    about = models.TextField(verbose_name='درباره')
    image = models.ImageField(upload_to='images/translator', null=True, blank=True,
                              verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال شده/نشده')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده/نشده')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مترجم'
        verbose_name_plural = 'مترجمان'

