# Generated by Django 4.0.3 on 2022-04-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0022_alter_level_down_lines_alter_level_match_bonus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=20, null=True),
        ),
    ]