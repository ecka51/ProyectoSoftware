# Generated by Django 3.2.4 on 2021-09-10 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tramitesApp', '0008_auto_20210910_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tramite',
            name='fechatram',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
