# Generated by Django 4.2.1 on 2023-08-25 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0057_alter_protocolos_metodologia_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metodologia",
            name="nombre_metodologia",
            field=models.IntegerField(max_length=90, verbose_name="Metodologia"),
        ),
        migrations.AlterField(
            model_name="parametro",
            name="nombre_parametro",
            field=models.IntegerField(max_length=90, verbose_name="Nombre Parametros"),
        ),
    ]
