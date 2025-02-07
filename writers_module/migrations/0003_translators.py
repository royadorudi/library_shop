# Generated by Django 4.0.6 on 2022-11-13 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_module', '0021_bookcomments_parent'),
        ('writers_module', '0002_remove_writers_book_writers_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام')),
                ('url_title', models.CharField(max_length=250, verbose_name='عنوان در url')),
                ('about', models.TextField(verbose_name='درباره')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/translator', verbose_name='تصویر')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال شده/نشده')),
                ('is_delete', models.BooleanField(default=False, verbose_name='حذف شده/نشده')),
                ('book', models.ManyToManyField(related_name='book_translator', to='books_module.books', verbose_name='مترجم کتاب')),
            ],
            options={
                'verbose_name': 'مترجم',
                'verbose_name_plural': 'مترجمان',
            },
        ),
    ]
