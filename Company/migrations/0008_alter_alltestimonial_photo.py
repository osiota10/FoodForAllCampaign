# Generated by Django 4.0.3 on 2022-04-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0007_alltestimonial_delete_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alltestimonial',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
