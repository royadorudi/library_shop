# Generated by Django 4.0.6 on 2022-08-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان مقاله')),
                ('url_title', models.CharField(max_length=300, verbose_name='عنوان در url')),
                ('short_description', models.TextField(verbose_name='توضیحات کوتاه مقاله')),
                ('main_text', models.TextField(verbose_name='متن مقاله')),
                ('image', models.ImageField(upload_to='images/blog', verbose_name='تصویر مقاله')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'لیست مقالات',
                'verbose_name_plural': 'لیست مقالات',
            },
        ),
    ]
