# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 02:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0002_patient_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicalcontrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('natural_key', models.CharField(max_length=100)),
                ('make', models.DateTimeField()),
                ('medic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Person', verbose_name='autor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Patient')),
            ],
        ),
    ]
