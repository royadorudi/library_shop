# Generated by Django 4.0.6 on 2022-10-18 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books_module', '0015_remove_bookcomments_user_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcomments',
            name='user_name',
        ),
        migrations.AddField(
            model_name='bookcomments',
            name='user',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]