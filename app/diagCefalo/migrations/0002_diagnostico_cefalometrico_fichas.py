# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-27 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacion', '0001_initial'),
        ('diagCefalo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostico_cefalometrico',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
    ]
