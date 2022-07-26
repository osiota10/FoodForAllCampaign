# Generated by Django 4.0.3 on 2022-04-21 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyinformation',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyinformation',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyinformation',
            name='linkenin_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyinformation',
            name='tag_line',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='companyinformation',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyinformation',
            name='whataspp_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
