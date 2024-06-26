# Generated by Django 4.2.11 on 2024-04-09 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_link', models.URLField()),
                ('link', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SportItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_link', models.URLField()),
                ('link', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='newsitem',
            name='description',
            field=models.TextField(default='Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='link',
            field=models.URLField(),
        ),
    ]
