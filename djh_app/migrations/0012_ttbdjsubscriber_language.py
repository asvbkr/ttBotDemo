# Generated by Django 3.0.7 on 2020-07-23 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djh_app', '0011_ttbdjsubscriber_chat_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttbdjsubscriber',
            name='language',
            field=models.CharField(max_length=20, null=True, verbose_name='language'),
        ),
    ]