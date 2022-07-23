# Generated by Django 4.0.3 on 2022-04-13 02:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0019_alter_profile_profile_pic_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='withdrawals',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='updated',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]