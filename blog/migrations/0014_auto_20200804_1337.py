# Generated by Django 3.0.8 on 2020-08-04 08:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200803_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='content',
            new_name='hobbies',
        ),
        migrations.AddField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
