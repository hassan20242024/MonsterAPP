from django.urls import path

from . import views

urlpatterns=[
   
    path("crear_secuencias/",views.crear_secuencias, name="crear_secuencias"),
    path("editar_secuencias/<int:pk>/", views.editar_secuencias, name="editar_secuencias"),
    path("actualizar_secuencias_validadas/<int:pk>/", views.actualizar_secuencias_validadas,name="actualizar_secuencias_validadas"),
    path("cambiar_estado_ensayo/<int:pk>/", views.cambiar_estado_ensayo,name="cambiar_estado_ensayo"),
    #path("actualizar_secuencias_impresas/<int:pk>/", views.actualizar_secuencias_impresas, name="actualizar_secuencias_impresas"),
    #path("actualizar_secuencias_reportadas/<int:pk>/", views.actualizar_secuencias_reportadas, name="actualizar_secuencias_reportadas"),
    path("actualizarEstadoParametros/<int:pk>/", views.actualizarEstadoParametros, name="actualizarEstadoParametros"),
    path("validar_secuencias/<int:pk>/", views.validar_secuencias, name="validar_secuencias"),
    path("crear_secuencias_en_curso/",views.crear_secuencias_en_curso, name="crear_secuencias_en_curso"),
    path("invalidar_secuencias/<int:pk>/", views.invalidar_secuencias, name="invalidar_secuencias"),
    path("editar_secuencias_en_curso/<int:pk>/", views.editar_secuencias_en_curso, name="editar_secuencias_en_curso"),
    path("invalidar_prueba/<int:pk>/", views.invalidar_prueba, name="invalidar_prueba"),
    path("duplicar_secuencias/<int:pk>/", views.duplicar_secuencias, name="duplicar_secuencias"),
    path("duplicar_secuencias_muestras/<int:pk>/", views.duplicar_secuencias_muestras, name="duplicar_secuencias_muestras"),
    path("proceso_secuencias_en_curso/",views.proceso_secuencias_en_curso, name="proceso_secuencias_en_curso"),
    path("impresion_secuencia/<int:pk>/", views.impresion_secuencia, name="impresion_secuencia"),
    path("reporte_secuencias/<int:pk>/", views.reporte_secuencias, name="reporte_secuencias"),
    path("auditar_secuencias/<int:pk>/", views.auditar_secuencias, name="auditar_secuencias"),
    path("secuencias_invalidas/",views.secuencias_invalidas, name="secuencias_invalidas"),
    path("chart_js_proceso_secuencias_en_curso/",views.chart_js_proceso_secuencias_en_curso, name="chart_js_proceso_secuencias_en_curso"),
    

  
]