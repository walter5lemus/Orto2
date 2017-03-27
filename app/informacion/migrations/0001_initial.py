# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-27 03:44
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dui', models.CharField(max_length=10)),
                ('carnet', models.CharField(max_length=7)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='catalogo_enfermedades',
            fields=[
                ('id_enfermedad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_enfermedad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='codigo_expediente',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='datos_generales',
            fields=[
                ('cod_expediente', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('edad_registro', models.IntegerField()),
                ('fecha_nac', models.DateField()),
                ('telefono', models.IntegerField()),
                ('genero', models.IntegerField(choices=[(1, b'Masculino'), (2, b'Femenino')], default=1)),
                ('direccion', models.CharField(max_length=200)),
                ('nombre_resp', models.CharField(max_length=100)),
                ('fecha_hora_creacion', models.DateTimeField()),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='estado_general',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cambio_salud', models.BooleanField(choices=[(True, b'Yes'), (False, b'No')], default=False)),
                ('detalle_enf_operacion', models.CharField(blank=True, max_length=500, null=True)),
                ('detalle_medicamento', models.CharField(blank=True, max_length=30, null=True)),
                ('detalle_otra_enfermedad', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='fichas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('cod_expediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informacion.datos_generales')),
                ('usuario_creador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['cod_expediente'],
            },
        ),
        migrations.CreateModel(
            name='motivo_consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_consulta', models.CharField(max_length=500)),
                ('fechaRegistro', models.DateField(default=datetime.datetime(2017, 3, 27, 3, 44, 7, 652000, tzinfo=utc))),
                ('fichas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas')),
            ],
        ),
        migrations.CreateModel(
            name='ultima_modificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('fichas', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas')),
            ],
        ),
        migrations.AddField(
            model_name='estado_general',
            name='fichas',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='informacion.fichas'),
        ),
        migrations.AddField(
            model_name='estado_general',
            name='otras_enfermedades',
            field=models.ManyToManyField(blank=True, null=True, to='informacion.catalogo_enfermedades'),
        ),
        migrations.AlterUniqueTogether(
            name='fichas',
            unique_together=set([('cod_expediente', 'numero')]),
        ),
    ]
