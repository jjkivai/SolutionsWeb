# Generated by Django 3.1.4 on 2020-12-31 00:31

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201230_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_image', models.ImageField(upload_to=api.models.client_logo, verbose_name='Client Logo')),
            ],
        ),
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_image', models.ImageField(upload_to=api.models.license_images, verbose_name='License Photo')),
            ],
        ),
    ]
