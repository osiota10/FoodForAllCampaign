# Generated by Django 4.0.3 on 2022-05-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0022_howwework_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
