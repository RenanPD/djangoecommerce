# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2017-04-10 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Imagem'),
        ),
    ]
