# Generated by Django 4.2.11 on 2024-04-09 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0005_eduitem_time_newsitem_time_sportitem_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EduItem',
        ),
        migrations.DeleteModel(
            name='SportItem',
        ),
        migrations.AddField(
            model_name='newsitem',
            name='category',
            field=models.CharField(default='news', max_length=200),
            preserve_default=False,
        ),
    ]
