# Generated by Django 4.0.3 on 2022-04-07 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0012_remove_level_user_currentlevel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentlevel',
            name='level',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Dashboard.level'),
        ),
    ]
