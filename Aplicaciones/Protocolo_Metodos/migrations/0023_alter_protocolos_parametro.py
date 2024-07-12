# Generated by Django 4.2.1 on 2023-08-21 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0022_remove_protocolos_parametro_protocolos_parametro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="protocolos",
            name="parametro",
            field=models.OneToOneField(
                max_length=90,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.parametro",
                verbose_name="Parámetros",
            ),
        ),
    ]
