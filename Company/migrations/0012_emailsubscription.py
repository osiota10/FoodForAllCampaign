# Generated by Django 4.0.3 on 2022-05-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0011_contactus_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]