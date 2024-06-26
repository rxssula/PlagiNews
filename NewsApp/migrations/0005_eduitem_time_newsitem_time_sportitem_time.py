# Generated by Django 4.2.11 on 2024-04-09 23:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0004_eduitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduitem',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsitem',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sportitem',
            name='time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
