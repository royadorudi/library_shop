from django.db import models


class BlogList(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان مقاله')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')
    short_description = models.TextField(verbose_name='توضیحات کوتاه مقاله')
    main_text = models.TextField(verbose_name='متن مقاله')
    image = models.ImageField(upload_to='images/blog', verbose_name='تصویر مقاله')
    date = models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لیست مقالات'
        verbose_name_plural = 'لیست مقالات'

