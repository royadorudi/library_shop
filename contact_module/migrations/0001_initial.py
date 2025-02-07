# Generated by Django 4.0.6 on 2022-08-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان پیام')),
                ('full_name', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('email', models.EmailField(max_length=300, verbose_name='ایمیل')),
                ('phone_number', models.CharField(max_length=250, verbose_name='شماره تلفن')),
                ('message', models.TextField(verbose_name='متن پیام')),
                ('response', models.TextField(blank=True, null=True, verbose_name='جواب ادمین')),
                ('is_read_by_admin', models.BooleanField(default=False, verbose_name='خوانده شده / نشده توسط ادمین')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاریخ')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس با ما',
            },
        ),
    ]
