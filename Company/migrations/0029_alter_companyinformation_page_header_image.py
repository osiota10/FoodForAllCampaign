# Generated by Django 4.0.3 on 2022-05-29 07:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0028_companyinformation_page_header_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinformation',
            name='page_header_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
