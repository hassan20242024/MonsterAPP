# Generated by Django 4.2.1 on 2023-08-31 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0068_alter_protocolos_parametro"),
    ]

    operations = [
        migrations.CreateModel(
            name="EstadoProtocolo",
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
                    "estado_protocolos",
                    models.CharField(max_length=90, verbose_name="Estado Protocolos"),
                ),
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
        migrations.RemoveField(model_name="protocolos", name="estado",),
        migrations.AddField(
            model_name="protocolos",
            name="fecha_ingreso",
            field=models.DateField(
                blank=True,
                help_text="AAAA/MM/DD",
                null=True,
                verbose_name="Fecha de Registro",
            ),
        ),
        migrations.AlterField(
            model_name="protocolos",
            name="fecha_registro",
            field=models.DateField(
                auto_now_add=True,
                default=None,
                help_text="AAAA/MM/DD",
                verbose_name="Fecha de Registro",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="protocolos",
            name="estado_protocolo",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.estadoprotocolo",
                verbose_name="Estado Protocolo",
            ),
        ),
    ]
