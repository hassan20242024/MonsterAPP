# Generated by Django 4.2.7 on 2023-11-16 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0096_alter_protocolos_parametro"),
    ]

    operations = [
        migrations.RemoveField(model_name="protocolos", name="fecha_registro",),
    ]
