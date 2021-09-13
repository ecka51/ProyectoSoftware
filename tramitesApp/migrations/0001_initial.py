# Generated by Django 3.2.4 on 2021-09-13 18:54

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('codigo', models.CharField(max_length=10)),
                ('dni', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=9)),
                ('facultad', models.CharField(default='INGENIERIA', max_length=10)),
                ('escuela', models.CharField(default='INGENIERIA DE SISTEMAS', max_length=22)),
                ('firma', models.ImageField(null=True, upload_to='alumno')),
                ('estado', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File_tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisito1', models.FileField(null=True, upload_to='tramite/')),
                ('requisito2', models.FileField(null=True, upload_to='tramite/')),
                ('requisito3', models.FileField(null=True, upload_to='tramite/')),
                ('requisito4', models.FileField(null=True, upload_to='tramite/')),
                ('requisito5', models.FileField(null=True, upload_to='tramite/')),
                ('requisito6', models.FileField(null=True, upload_to='tramite/')),
                ('requisito7', models.FileField(null=True, upload_to='tramite/')),
                ('requisito8', models.FileField(null=True, upload_to='tramite/')),
            ],
        ),
        migrations.CreateModel(
            name='TipoTramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abreviatura_tipoTramite', models.CharField(max_length=8)),
                ('tipoTramite', models.CharField(max_length=90)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechatram', models.DateField(default=datetime.date.today, editable=False)),
                ('estado', models.CharField(default='CREADO', max_length=20)),
                ('alumnos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.alumno')),
                ('file_tramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.file_tramite')),
                ('tipoTramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.tipotramite')),
            ],
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abreviatura_req', models.CharField(max_length=12)),
                ('requisito', models.CharField(max_length=200)),
                ('estado', models.BooleanField()),
                ('tipoTramite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.tipotramite')),
            ],
        ),
        migrations.CreateModel(
            name='Fut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto', models.CharField(max_length=500, null=True)),
                ('fecha', models.DateField(default=datetime.date.today, editable=False)),
                ('estado', models.BooleanField(default=True, editable=False)),
                ('alumnos', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.alumno')),
                ('tipoTramite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.tipotramite')),
            ],
        ),
    ]
