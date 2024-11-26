# Generated by Django 4.2.7 on 2024-11-25 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Secuencias", "0012_alter_lavado_buzo_fecha_alerta_inferior_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 24, 5, 14, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta inferior",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 11, 30, 10, 2, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta inferior calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 24, 5, 14, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta inferior celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 11, 30, 10, 2, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta inferior mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_test",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 24, 5, 14, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta inferior test",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 7, 38, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta superior",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 2, 10, 2, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta superior calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 7, 38, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta superior celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 2, 10, 2, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta superior mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_test",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 7, 38, 2, 41957),
                null=True,
                verbose_name="Fecha de alerta superior test",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 5, 14, 2, 41957),
                null=True,
                verbose_name="Fecha de la calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_lavado_buzo",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 25, 10, 2, 2, 41957),
                null=True,
                verbose_name="Fecha de lavado de buzos",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_lavado_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 25, 10, 2, 2, 41957),
                null=True,
                verbose_name="Fecha de lavado de celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 5, 14, 2, 41957),
                null=True,
                verbose_name="Fecha del Mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_test_diagnostico",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 25, 10, 2, 2, 41957),
                null=True,
                verbose_name="Fecha del test",
            ),
        ),
    ]
