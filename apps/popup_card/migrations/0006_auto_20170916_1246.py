# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-16 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20170915_2118'),
        ('popup_card', '0005_auto_20170916_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=500, unique=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Status_general')),
            ],
        ),
        migrations.AddField(
            model_name='popup_card',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='popup_card.Category_card'),
        ),
    ]
