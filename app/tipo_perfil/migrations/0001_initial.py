# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPerfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frontal_facial', models.IntegerField(choices=[(1, b'Dolicofacial'), (2, b'Mesofacial'), (3, b'Braquifacial')])),
                ('tipoPerfiltotal', models.IntegerField(choices=[(1, b'Ortonagtico'), (2, b'Divergente Anterior'), (3, b'Divergente Posterior')])),
                ('perfilTercio_inferior', models.IntegerField(choices=[(1, b'Recto'), (2, b'Concavo'), (3, b'Convexo')])),
                ('tipoSonrisa', models.IntegerField(choices=[(1, b'Gingival'), (2, b'Dental')])),
                ('tipo_competenciaLabial', models.IntegerField(choices=[(1, b'Competente'), (2, b'Potencialmente Competente'), (3, b'Incompetente')])),
                ('grosorLabios', models.IntegerField(choices=[(1, b'Grueso'), (2, b'Delgado')])),
                ('tamanoLabios', models.IntegerField(choices=[(2, b'Mediana'), (3, b'Peque\xc3\xb1a'), (1, b'Grande')])),
                ('tipoNariz', models.IntegerField(choices=[(2, b'Mediana'), (3, b'Peque\xc3\xb1a'), (1, b'Grande')])),
                ('angulo_Naso_labial', models.IntegerField()),
                ('tercio_superior', models.IntegerField()),
                ('tercio_medio', models.IntegerField()),
                ('tercio_inferior', models.IntegerField()),
                ('tamanoSonrisa', models.IntegerField()),
                ('fichas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas')),
            ],
        ),
    ]
