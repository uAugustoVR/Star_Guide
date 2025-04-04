# Generated by Django 5.1.4 on 2025-01-09 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_photographs_date_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographs',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='photographs',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
