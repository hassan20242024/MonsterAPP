# Generated by Django 4.2.7 on 2024-11-17 03:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Secuencias", "0004_alter_lavado_buzo_fecha_alerta_inferior_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 15, 17, 18, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta inferior",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 11, 21, 22, 6, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta inferior calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 15, 17, 18, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta inferior celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 11, 21, 22, 6, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta inferior mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_inferior_test",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 15, 17, 18, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta inferior test",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 16, 19, 42, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta superior",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 11, 23, 22, 6, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta superior calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 16, 19, 42, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta superior celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 11, 23, 22, 6, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta superior mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_alerta_superior_test",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 16, 19, 42, 15, 448917),
                null=True,
                verbose_name="Fecha de alerta superior test",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_calificacion",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 16, 17, 18, 15, 448917),
                null=True,
                verbose_name="Fecha de la calificación",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_lavado_buzo",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 16, 22, 6, 15, 448917),
                null=True,
                verbose_name="Fecha de lavado de buzos",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_lavado_celda",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 16, 22, 6, 15, 448917),
                null=True,
                verbose_name="Fecha de lavado de celda",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_mantenimiento",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2025, 1, 16, 17, 18, 15, 448917),
                null=True,
                verbose_name="Fecha del Mantenimiento",
            ),
        ),
        migrations.AlterField(
            model_name="lavado_buzo",
            name="fecha_test_diagnostico",
            field=models.DateField(
                blank=True,
                default=datetime.datetime(2024, 12, 16, 22, 6, 15, 448917),
                null=True,
                verbose_name="Fecha del test",
            ),
        ),
    ]