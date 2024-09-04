# Generated by Django 4.2.7 on 2024-09-02 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Protocolo_Metodos", "0001_initial"),
        ("Secuencias", "0003_alter_secuencias_parametro_sq_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="secuencias", unique_together=set(),),
        migrations.AlterField(
            model_name="secuencias",
            name="parametro_sq",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.parametro",
                verbose_name="Parametro",
            ),
        ),
        migrations.AlterField(
            model_name="secuencias",
            name="protocolo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.protocolos",
                verbose_name="Protocolo",
            ),
        ),
        migrations.AddConstraint(
            model_name="secuencias",
            constraint=models.UniqueConstraint(
                fields=("protocolo", "parametro_sq"), name="unique_intro"
            ),
        ),
    ]
