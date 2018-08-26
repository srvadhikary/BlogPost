# Generated by Django 2.0 on 2018-08-22 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='blog',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
