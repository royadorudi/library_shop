# Generated by Django 4.0.6 on 2022-09-26 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books_module', '0011_bookcomments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcomments',
            name='is_read_by_admin',
        ),
        migrations.AddField(
            model_name='bookcomments',
            name='submit_date',
            field=models.DateField(auto_now=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='bookcomments',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='books_module.books', verbose_name='کتاب'),
        ),
        migrations.AlterField(
            model_name='bookcomments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]
