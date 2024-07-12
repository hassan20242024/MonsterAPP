# Generated by Django 4.2.1 on 2023-08-20 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "Protocolo_Metodos",
            "0009_alter_parametro_parametro_alter_protocolos_parametro",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="parametro",
            name="parametro",
            field=models.CharField(
                blank=True, max_length=90, null=True, verbose_name="Subparametros"
            ),
        ),
        migrations.AlterField(
            model_name="protocolos",
            name="parametro",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.parametro",
                verbose_name="Parámetros",
            ),
        ),
    ]
