# Generated by Django 3.0.8 on 2020-08-03 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200803_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='hobbies',
            new_name='content',
        ),
    ]
