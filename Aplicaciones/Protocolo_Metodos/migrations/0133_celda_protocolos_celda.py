# Generated by Django 4.2.7 on 2024-06-28 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Protocolo_Metodos", "0132_alter_parametro_nombre_parametro_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Celda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_celda",
                    models.CharField(
                        max_length=90,
                        null=True,
                        unique=True,
                        verbose_name="Nombre de Celda",
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
                (
                    "responsable",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="protocolos",
            name="celda",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.celda",
                verbose_name="Celda",
            ),
        ),
    ]
