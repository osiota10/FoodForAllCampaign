# Generated by Django 4.0.3 on 2022-04-21 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0003_alter_corevalue_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corevalue',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='whoweare',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
