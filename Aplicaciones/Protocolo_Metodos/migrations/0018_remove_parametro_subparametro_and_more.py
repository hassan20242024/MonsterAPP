# Generated by Django 4.2.1 on 2023-08-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0017_alter_parametro_nombre_alter_subparametro_nombre"),
    ]

    operations = [
        migrations.RemoveField(model_name="parametro", name="subparametro",),
        migrations.AlterField(
            model_name="protocolos",
            name="metodologia",
            field=models.CharField(
                choices=[
                    ("HPLC Ó UHPLC", "HPLC_UHPLC"),
                    ("HPLC", "HPLC"),
                    ("UHPLC", "UHPLC"),
                ],
                default="HPLC Ó UHPLC",
                max_length=90,
                verbose_name="metodologia",
            ),
        ),
        migrations.AddField(
            model_name="parametro",
            name="subparametro",
            field=models.ManyToManyField(
                max_length=250,
                to="Protocolo_Metodos.subparametro",
                verbose_name="subparametro",
            ),
        ),
    ]
