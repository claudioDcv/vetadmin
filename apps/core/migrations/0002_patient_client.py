# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='core.Person', verbose_name='cliente'),
        ),
    ]
