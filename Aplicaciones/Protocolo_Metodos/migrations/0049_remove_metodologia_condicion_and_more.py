# Generated by Django 4.2.1 on 2023-08-24 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "Protocolo_Metodos",
            "0048_alter_metodologia_nombre_alter_parametro_nombre_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="metodologia", name="condicion",),
        migrations.RemoveField(model_name="parametro", name="condicion",),
    ]
