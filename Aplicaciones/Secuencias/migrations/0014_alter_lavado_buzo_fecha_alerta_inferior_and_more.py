# Generated by Django 4.2.7 on 2024-11-25 16:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Secuencias", "0013_alter_lavado_buzo_fecha_alerta_inferior_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 24, 6, 38, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta inferior",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 11, 30, 11, 26, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta inferior calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 24, 6, 38, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta inferior celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 11, 30, 11, 26, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta inferior mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_test",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 24, 6, 38, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta inferior test",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 9, 2, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta superior",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 2, 11, 26, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta superior calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 9, 2, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta superior celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 2, 11, 26, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta superior mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_test",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 9, 2, 15, 21025),
                null=True,
                verbose_name="Fecha de alerta superior test",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 6, 38, 15, 21025),
                null=True,
                verbose_name="Fecha de la calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_lavado_buzo",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 25, 11, 26, 15, 21025),
                null=True,
                verbose_name="Fecha de lavado de buzos",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_lavado_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 25, 11, 26, 15, 21025),
                null=True,
                verbose_name="Fecha de lavado de celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 25, 6, 38, 15, 21025),
                null=True,
                verbose_name="Fecha del Mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_test_diagnostico",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 25, 11, 26, 15, 21025),
                null=True,
                verbose_name="Fecha del test",
            ),
        ),
    ]