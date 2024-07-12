# Generated by Django 4.2.1 on 2023-08-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0064_alter_protocolos_parametro"),
    ]

    operations = [
        migrations.RemoveField(model_name="protocolos", name="parametro",),
        migrations.AddField(
            model_name="protocolos",
            name="parametro",
            field=models.ManyToManyField(
                max_length=90,
                null=True,
                to="Protocolo_Metodos.parametro",
                verbose_name="parametro",
            ),
        ),
    ]
