# Generated by Django 5.1.4 on 2025-01-30 05:37

import apps.galeria.rename
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0010_alter_photographs_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographs',
            name='photo',
            field=models.ImageField(blank=True, upload_to=apps.galeria.rename.rename_photo),
        ),
    ]
