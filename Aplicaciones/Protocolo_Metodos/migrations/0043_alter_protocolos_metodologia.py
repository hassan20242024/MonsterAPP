# Generated by Django 4.2.1 on 2023-08-24 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0042_alter_protocolos_parametro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="protocolos",
            name="metodologia",
            field=models.ForeignKey(
                blank=True,
                max_length=90,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.metodologia",
                verbose_name="metodologia",
            ),
        ),
    ]
