# Generated by Django 4.2.7 on 2024-07-09 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Secuencias", "0034_usuario_validar_usuario_invalidar_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="secuencias",
            name="fecha_invalidar",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Fecha de Invalidéz"
            ),
        ),
        migrations.AddField(
            model_name="secuencias",
            name="fecha_validar",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Fecha de Validación"
            ),
        ),
        migrations.AlterField(
            model_name="secuencias",
            name="invalidar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Secuencias.usuario_invalidar",
                verbose_name="Invalidada por",
            ),
        ),
        migrations.AlterField(
            model_name="secuencias",
            name="validar",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Secuencias.usuario_validar",
                verbose_name="Validada por",
            ),
        ),
    ]
