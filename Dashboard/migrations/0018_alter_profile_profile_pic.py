# Generated by Django 4.0.3 on 2022-04-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0017_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default-user.jfif', null=True, upload_to=''),
        ),
    ]
