from django.urls import path

from . import views

urlpatterns=[
    #path("protocolo_metodos/",views.protocolo_metodos, name="protocolo_metodos"),
    path("crear_protocolo_proceso/", views.crear_protocolo_proceso, name="crear_protocolo_proceso"),
]