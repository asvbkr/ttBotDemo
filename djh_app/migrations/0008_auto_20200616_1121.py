# Generated by Django 3.0.7 on 2020-06-16 08:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djh_app', '0007_ttbdjlimitedbuttons'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttbdjchatavailable',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='ttbdjlimitedbuttons',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='ttbdjsubscriber',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='ttbprevstep',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='ttbuser',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='ttbdjchatavailable',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='ttbdjchatavailable',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='ttbdjlimitedbuttons',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='ttbdjsubscriber',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='ttbdjsubscriber',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='ttbprevstep',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='ttbuser',
            name='avatar_url',
            field=models.TextField(blank=True, null=True, verbose_name='avatar url'),
        ),
        migrations.AlterField(
            model_name='ttbuser',
            name='full_avatar_url',
            field=models.TextField(blank=True, null=True, verbose_name='full avatar url'),
        ),
        migrations.AlterField(
            model_name='ttbuser',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated'),
        ),
        migrations.CreateModel(
            name='TtbUserProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('p_type', models.CharField(default='common', max_length=16, verbose_name='type')),
                ('code', models.CharField(max_length=32, verbose_name='code')),
                ('value', models.CharField(max_length=256, verbose_name='value')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('db_user', models.ManyToManyField(to='djh_app.TtbUser', verbose_name='user')),
            ],
            options={
                'abstract': False,
                'unique_together': {('p_type', 'code', 'value')},
            },
        ),
        migrations.CreateModel(
            name='TtbDjSubscriberProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('p_type', models.CharField(default='common', max_length=16, verbose_name='type')),
                ('code', models.CharField(max_length=32, verbose_name='code')),
                ('value', models.CharField(max_length=256, verbose_name='value')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('db_chat', models.ManyToManyField(to='djh_app.TtbDjSubscriber', verbose_name='chat')),
            ],
            options={
                'abstract': False,
                'unique_together': {('p_type', 'code', 'value')},
            },
        ),
    ]