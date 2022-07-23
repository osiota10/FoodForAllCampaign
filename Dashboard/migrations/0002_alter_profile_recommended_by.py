# Generated by Django 4.0.3 on 2022-04-04 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='recommended_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.fields.CharField, related_name='ref_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
