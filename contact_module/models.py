from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان پیام')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    phone_number = models.CharField(max_length=250, verbose_name='شماره تلفن')
    message = models.TextField(verbose_name='متن پیام')
    response = models.TextField(null=True, blank=True, verbose_name='جواب ادمین')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده / نشده توسط ادمین')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'
