# Generated by Django 4.0.3 on 2022-04-24 06:43

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0009_alter_howwework_pic_alter_photogallery_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alltestimonial',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='companyinformation',
            name='logo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='corevalue',
            name='pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='heromenu',
            name='pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='whoweare',
            name='pic',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
