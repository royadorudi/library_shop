# Generated by Django 4.0.6 on 2022-09-08 11:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books_module', '0007_alter_books_bookmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, default=False, null=True, related_name='bookmarks', to=settings.AUTH_USER_MODEL, verbose_name='نشان شده'),
        ),
    ]
