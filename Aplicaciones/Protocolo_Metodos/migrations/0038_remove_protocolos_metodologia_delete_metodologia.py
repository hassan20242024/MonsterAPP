# Generated by Django 4.2.1 on 2023-08-24 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0037_alter_metodologia_nombre"),
    ]

    operations = [
        migrations.RemoveField(model_name="protocolos", name="metodologia",),
        migrations.DeleteModel(name="Metodologia",),
    ]
