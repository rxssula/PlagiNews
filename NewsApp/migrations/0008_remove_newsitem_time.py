# Generated by Django 4.2.11 on 2024-04-10 00:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0007_alter_newsitem_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='time',
        ),
    ]