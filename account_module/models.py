from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', null=True, blank=True, verbose_name='تصویر')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره ی کاربر')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    def __str__(self):
        if self.first_name is '' and self.last_name is '':
            return self.email
        return self.get_full_name()


class Subscriber(models.Model):
    email = models.EmailField(max_length=250, verbose_name='ایمیل')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'عضو خبرنامه'
        verbose_name_plural = 'اعضای خبرنامه'
