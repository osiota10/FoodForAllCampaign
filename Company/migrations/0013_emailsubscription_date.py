# Generated by Django 4.0.3 on 2022-05-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0012_emailsubscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsubscription',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
