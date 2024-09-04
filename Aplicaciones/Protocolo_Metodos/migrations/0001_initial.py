# Generated by Django 4.2.7 on 2024-09-02 15:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Celda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_celda",
                    models.CharField(
                        max_length=90,
                        null=True,
                        unique=True,
                        verbose_name="Nombre de Celda",
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
                (
                    "responsable",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_cliente",
                    models.CharField(
                        max_length=90, null=True, unique=True, verbose_name="Cliente"
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ensayo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_ensayo",
                    models.CharField(max_length=90, unique=True, verbose_name="Ensayo"),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EstadoProtocolo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "estado_protocolos",
                    models.CharField(max_length=90, verbose_name="Estado Protocolos"),
                ),
                (
                    "estado_motivo",
                    models.CharField(
                        blank=True,
                        max_length=90,
                        unique=True,
                        verbose_name="Motivo del estado",
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Etapa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_etapa",
                    models.CharField(max_length=90, unique=True, verbose_name="Etapa"),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
                (
                    "ensayo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Protocolo_Metodos.ensayo",
                        verbose_name="Ensayo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Metodo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "codigo_metodo",
                    models.CharField(max_length=90, unique=True, verbose_name="código"),
                ),
                (
                    "nombre_metodo",
                    models.CharField(max_length=90, unique=True, verbose_name="Nombre"),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Metodologia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_metodologia",
                    models.CharField(
                        max_length=90, unique=True, verbose_name="Metodologia"
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Muestras_y_Placebos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fecha_ingreso",
                    models.DateField(
                        help_text="AAAA/MM/DD",
                        null=True,
                        verbose_name="Fecha de ingreso muestra",
                    ),
                ),
                (
                    "nombre_muestra",
                    models.CharField(
                        max_length=300, verbose_name="nombre de Muestra/Placebo/MP"
                    ),
                ),
                (
                    "codigo_muestra_interno",
                    models.CharField(max_length=90, verbose_name="CIM / LIMS"),
                ),
                (
                    "codigo_muestra_producto",
                    models.CharField(max_length=90, verbose_name="Código de Producto"),
                ),
                ("lote_muestra", models.CharField(max_length=90, verbose_name="Lote")),
                (
                    "observaciones_muestras",
                    models.TextField(max_length=300, verbose_name="Observaciones"),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
                (
                    "etapa",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Protocolo_Metodos.etapa",
                        verbose_name="Etapa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Parametro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subparametro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_subparametro",
                    models.CharField(
                        blank=True,
                        max_length=90,
                        unique=True,
                        verbose_name="Subparametro",
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tipo_muestra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo_muestra",
                    models.CharField(
                        max_length=90, unique=True, verbose_name="Tipo de muestra"
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Titulo_Parametro",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "titulo_parametro",
                    models.CharField(
                        blank=True,
                        max_length=90,
                        unique=True,
                        verbose_name="Titulo Párametro",
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Viabilidad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_viabilidad",
                    models.CharField(
                        max_length=90,
                        null=True,
                        unique=True,
                        verbose_name="Insumos del Proceso",
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Protocolos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fecha_ingreso",
                    models.DateField(
                        help_text="AAAA/MM/DD",
                        null=True,
                        verbose_name="Fecha de Registro",
                    ),
                ),
                (
                    "codigo",
                    models.CharField(
                        max_length=90,
                        null=True,
                        unique=True,
                        verbose_name="Código Protocolo",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        max_length=250,
                        null=True,
                        unique=True,
                        verbose_name="Título_del_Protocolo",
                    ),
                ),
                (
                    "condicion",
                    models.CharField(
                        choices=[("Activo", "ACTIVO"), ("Pasivo", "PASIVO")],
                        default="Activo",
                        max_length=90,
                        verbose_name="Condicion",
                    ),
                ),
                (
                    "observaciones",
                    models.CharField(
                        max_length=250, null=True, verbose_name="Observaciones"
                    ),
                ),
                (
                    "fecha_final",
                    models.DateField(
                        blank=True,
                        default=datetime.datetime.now,
                        null=True,
                        verbose_name="Fecha de Finalización",
                    ),
                ),
                (
                    "Insumos_del_Proceso",
                    models.ManyToManyField(to="Protocolo_Metodos.viabilidad"),
                ),
                (
                    "celda",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Protocolo_Metodos.celda",
                        verbose_name="Celda",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Protocolo_Metodos.cliente",
                        verbose_name="Cliente",
                    ),
                ),
                (
                    "ensayo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Protocolo_Metodos.ensayo",
                        verbose_name="Ensayo",
                    ),
                ),
                (
                    "estado_protocolo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Protocolo_Metodos.estadoprotocolo",
                        verbose_name="Estado Protocolo",
                    ),
                ),
                (
                    "metodo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Protocolo_Metodos.metodo",
                        verbose_name="Metodo de referencia",
                    ),
                ),
                (
                    "metodologia",
                    models.ForeignKey(
                        max_length=90,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Protocolo_Metodos.metodologia",
                        verbose_name="metodologia",
                    ),
                ),
                (
                    "muestras_y_Placebos",
                    models.ManyToManyField(to="Protocolo_Metodos.muestras_y_placebos"),
                ),
                (
                    "parametro",
                    models.ManyToManyField(
                        related_name="parametro", to="Protocolo_Metodos.parametro"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="parametro",
            name="nombre_parametro",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.subparametro",
                verbose_name="Nombre Parametro",
            ),
        ),
        migrations.AddField(
            model_name="parametro",
            name="nombre_titulo",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.titulo_parametro",
                verbose_name="Titulo Parametro",
            ),
        ),
        migrations.AddField(
            model_name="muestras_y_placebos",
            name="tipo_muestra",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Protocolo_Metodos.tipo_muestra",
                verbose_name="Tipo de muestra",
            ),
        ),
    ]
