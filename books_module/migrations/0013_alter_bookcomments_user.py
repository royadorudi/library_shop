# Generated by Django 4.0.6 on 2022-10-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_module', '0012_remove_bookcomments_is_read_by_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcomments',
            name='user',
            field=models.CharField(max_length=200, verbose_name='کاربر'),
        ),
    ]