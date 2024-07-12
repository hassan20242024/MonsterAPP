from django.urls import path

from . import views

urlpatterns=[
    path("protocolo_metodos/",views.protocolo_metodos, name="protocolo_metodos"),
    path("crear_protocolo_metodos/", views.crear_protocolo_metodos, name="crear_protocolo_metodos"),
    path("configuracion_protocolo_metodos/", views.configuracion_protocolo_metodos, name="configuracion_protocolo_metodos"),
    path("editar_parametro/<int:pk>/", views.editar_parametro, name="editar_parametro"),
    path("crear_metodologia/", views.crear_metodologia, name="crear_metodologia"),
    path("definir_estado/", views.definir_estado, name="definir_estado"),
    path("crear_ensayo/", views.crear_ensayo, name="crear_ensayo"),
    path("insumosDelProceso/", views.insumosDelProceso, name="insumosDelProceso"),
    path("editar_protocolo_metodos/<int:pk>/", views.editar_protocolo_metodos, name="editar_protocolo_metodos"),
    path("crear_cliente/", views.crear_cliente, name="crear_cliente"),
    #path("editar_protocolo_metodos/accion_editar_protocolo_metodos/<int:id>/", views.accion_editar_protocolo_metodos, name="accion_editar_protocolo_metodos"),
    path("revisar_protocolo_metodos/<int:pk>/", views.revisar_protocolo_metodos, name="revisar_protocolo_metodos"),
    path("detalles_protocolo_metodos/", views.detalles_protocolo_metodos, name="detalles_protocolo_metodos"),
    path("subparametro/", views.subparametro, name="subparametro"),
    path("titulo_parametro/", views.titulo_parametro, name="titulo_parametro"),
    path("ingresar_muestras/", views.ingresar_muestras, name="ingresar_muestras"),
    path("editar_titulo_parametro/<int:pk>/", views.editar_titulo_parametro, name="editar_titulo_parametro"),
    path("editar_subparametro/<int:pk>/", views.editar_subparametro, name="editar_subparametro"),
    path("editar_definir_estado/<int:pk>/", views.editar_definir_estado, name="editar_definir_estado"),
    path("editar_insumosDelProceso/<int:pk>/", views.editar_insumosDelProceso, name="editar_insumosDelProceso"),
    path("editar_ensayo/<int:pk>/", views.editar_ensayo, name="editar_ensayo"),
    path("editar_metodologia/<int:pk>/", views.editar_metodologia, name="editar_metodologia"),
    path("editar_cliente/<int:pk>/", views.editar_cliente, name="editar_cliente"),


   
]






