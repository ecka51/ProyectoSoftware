# Generated by Django 3.2.4 on 2021-09-05 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tramitesApp', '0003_auto_20210904_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisito',
            name='tipoRequisitos',
        ),
        migrations.AddField(
            model_name='requisito',
            name='tipoTramite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tramitesApp.tipotramite'),
        ),
        migrations.DeleteModel(
            name='TipoRequisito',
        ),
    ]
