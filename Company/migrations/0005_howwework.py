# Generated by Django 4.0.3 on 2022-04-21 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0004_alter_corevalue_pic_alter_whoweare_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowWeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=50)),
                ('snippet', models.TextField()),
            ],
        ),
    ]
