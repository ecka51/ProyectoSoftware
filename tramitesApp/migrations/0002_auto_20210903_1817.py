# Generated by Django 3.2.4 on 2021-09-03 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tramitesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoTramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estadotram', models.CharField(max_length=20)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisito', models.CharField(max_length=200)),
                ('archivo', models.FileField(blank=True, null=True, upload_to='requisito')),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='tramite',
            name='firma',
        ),
        migrations.AddField(
            model_name='alumno',
            name='escuela',
            field=models.CharField(default='INGENIERIA DE SISTEMAS', max_length=22),
        ),
        migrations.AddField(
            model_name='alumno',
            name='facultad',
            field=models.CharField(default='INGENIERIA', max_length=10),
        ),
        migrations.AddField(
            model_name='alumno',
            name='firma',
            field=models.ImageField(null=True, upload_to='alumno'),
        ),
        migrations.AddField(
            model_name='tramite',
            name='alumnos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.alumno'),
        ),
        migrations.AlterField(
            model_name='tipotramite',
            name='tipoTramite',
            field=models.CharField(max_length=90),
        ),
        migrations.CreateModel(
            name='TipoRequisito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoRequisito', models.CharField(max_length=100)),
                ('estado', models.BooleanField()),
                ('requisitos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.requisito')),
            ],
        ),
        migrations.CreateModel(
            name='BandejaTramite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(max_length=200)),
                ('tiempo', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('estado', models.BooleanField(default=True)),
                ('estadotramites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.estadotramite')),
                ('tramites', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.tramite')),
            ],
        ),
        migrations.AddField(
            model_name='tipotramite',
            name='tipoRequisitos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.tiporequisito'),
        ),
    ]