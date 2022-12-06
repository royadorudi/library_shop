from django.db import models
from account_module.models import User
import os


class BookCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')
    image = models.ImageField(null=True, blank=True, upload_to='images/logo', verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال شده / نشده')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی کتاب'
        verbose_name_plural = 'دسته بندی کتاب ها'


class Books(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url_title = models.CharField(max_length=200, verbose_name='عنوان در url')
    writer = models.CharField(max_length=200, verbose_name='نویسنده')
    translator = models.CharField(null=True, blank=True, max_length=200, verbose_name='مترجم')
    image = models.ImageField(upload_to='images/books', verbose_name='تصویر')
    file = models.FileField(upload_to='files/books', verbose_name='فایل')
    category = models.ManyToManyField(BookCategory, related_name='book_category', verbose_name='دسته بندی')
    price = models.IntegerField(null=True, blank=True, verbose_name='بها')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    submit_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    bookmarks = models.ManyToManyField(User, related_name='bookmarks', blank=True, verbose_name='نشان شده')

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.file.name)

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'


class BookComments(models.Model):
    book = models.ForeignKey(Books, related_name='book_comment', on_delete=models.CASCADE, verbose_name='کتاب')
    user = models.ForeignKey(User, related_name='user', default=False, on_delete=models.CASCADE, verbose_name='کاربر')
    comment = models.TextField(verbose_name='نظر')
    submit_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ ثبت')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='والد')

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        else:
            return self.user.email

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'





