# Generated by Django 5.1.3 on 2024-12-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginaMuni', '0004_taller_inscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taller',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]