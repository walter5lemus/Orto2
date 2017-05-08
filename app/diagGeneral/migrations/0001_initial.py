# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='diagnostico_general',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico_ortodontico_general', models.TextField()),
                ('problemas', models.TextField()),
                ('objetivos', models.TextField()),
                ('tratamiento', models.IntegerField(choices=[(1, b'Desgaste selectivo de pieza'), (2, b'Placas Activas'), (3, b'Placas Pasivas'), (4, b'Planos Inclinados'), (5, b'Pistas Indirectas Planas Simples'), (6, b'Rompeh\xc3\xa1bitos'), (7, b'Reganadores de Espacio')], default=1)),
                ('descripcion_tratamiento', models.TextField()),
            ],
        ),
    ]
