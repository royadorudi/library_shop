from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.URLField(max_length=300, verbose_name='عنوان در url')
    text = models.TextField(verbose_name='توضیحات کوتاه')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField(max_length=200, verbose_name='شماره تماس')
    address = models.TextField(verbose_name='آدرس')
    copy_right_text = models.TextField(verbose_name='متن کپی رایت')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درباره ی ما'
        verbose_name_plural = 'درباره ی ما'


