# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20170523_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='news_images/'),
        ),
    ]
