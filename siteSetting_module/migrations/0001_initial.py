# Generated by Django 4.0.6 on 2022-08-20 07:03

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('url_title', models.URLField(max_length=300, verbose_name='عنوان در url')),
                ('text', models.TextField(verbose_name='توضیحات کوتاه')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone_number', models.CharField(max_length=200, verbose_name='شماره تماس')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('copy_right_text', models.TextField(verbose_name='متن کپی رایت')),
            ],
            options={
                'verbose_name': 'درباره ی ما',
                'verbose_name_plural': 'درباره ی ما',
            },
        ),
        migrations.CreateModel(
            name='SiteLocationMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='شهر')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'نقشه ی لوکیشن سایت',
                'verbose_name_plural': 'نقشه ی لوکیشن سایت ',
            },
        ),
    ]
