# Generated by Django 4.2.7 on 2024-09-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Secuencias", "0012_remove_secuencias_unique_intro_nue_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="secuencias",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Registrada", "REGISTRADA"),
                    ("Invalida", "INVALIDA"),
                    ("Revisada", "REVISADA"),
                    ("Impresa", "IMPRESA"),
                    ("Reportada", "REPORTADA"),
                    ("Auditada", "AUDITADA"),
                    ("Ensayo", "ENSAYO"),
                ],
                default="Registrada",
                max_length=90,
                null=True,
                verbose_name="Status",
            ),
        ),
    ]
