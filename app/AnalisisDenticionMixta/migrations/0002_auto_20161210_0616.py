# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-10 12:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacion', '0001_initial'),
        ('AnalisisDenticionMixta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moyers_superior_ancho',
            name='fichas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='moyers_superior_ancho',
            name='posicion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AnalisisDenticionMixta.pos'),
        ),
        migrations.AddField(
            model_name='moyers_superior',
            name='fichas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='moyers_inferior_ancho',
            name='fichas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='moyers_inferior_ancho',
            name='posicion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AnalisisDenticionMixta.pos'),
        ),
        migrations.AddField(
            model_name='moyers_inferior',
            name='fichas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
    ]
