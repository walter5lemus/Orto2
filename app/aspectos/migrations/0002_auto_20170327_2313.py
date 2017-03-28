# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacion', '0001_initial'),
        ('aspectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_denticion',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='tipo_denticion',
            name='tipo',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='aspectos.tipo'),
        ),
        migrations.AddField(
            model_name='sobremordidas',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='relaciones_sagitales',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='registro_mordidas',
            name='fichas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='registro',
            name='fichas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='registro',
            name='problema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aspectos.problema'),
        ),
        migrations.AddField(
            model_name='linea_media_facial',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='imagenes_afmp',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='funcion_mandibular',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='diastemas_denticion',
            name='fichas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='denticion',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
    ]
