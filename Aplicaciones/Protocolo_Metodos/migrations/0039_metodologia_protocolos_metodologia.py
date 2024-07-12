# Generated by Django 4.2.1 on 2023-08-24 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0038_remove_protocolos_metodologia_delete_metodologia"),
    ]

    operations = [
        migrations.CreateModel(
            name="Metodologia",
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
                ("nombre", models.CharField(max_length=90, verbose_name="metodologia")),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default=False,
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="protocolos",
            name="metodologia",
            field=models.ForeignKey(
                default=None,
                max_length=90,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.metodologia",
                verbose_name="metodologia",
            ),
            preserve_default=False,
        ),
    ]
