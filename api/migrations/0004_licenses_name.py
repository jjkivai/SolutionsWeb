# Generated by Django 3.1.4 on 2020-12-31 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_client_licenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='licenses',
            name='name',
            field=models.CharField(default='Solutions License', max_length=64, verbose_name='License Title'),
        ),
    ]
