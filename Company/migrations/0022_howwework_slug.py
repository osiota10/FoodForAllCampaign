# Generated by Django 4.0.3 on 2022-05-19 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0021_alter_branchaddress_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='howwework',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
