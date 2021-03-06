# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 19:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum', '0018_auto_20160629_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField(blank=True, default=0)),
                ('contents', models.TextField(default='')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.Module')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
