# Generated by Django 2.2.1 on 2019-05-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djh_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='greeting',
            name='request_body',
            field=models.TextField(null=True, verbose_name='request body'),
        ),
    ]
