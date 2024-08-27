from django.contrib import admin


from .models import Secuencias, Sistema, Invalidar_Secuencia,usuario_invalidar,usuario_validar,usuario_impresion, usuario_reporte, usuario_auditor


# Register your models here.
class SecuenciasAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=["fecha_Inicio",'nombre', 'protocolo', "sistema", "status", "parametro_sq","invalidar","validar", "imprimir","reportar","auditar"]
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ('nombre'),
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['nombre', 'protocolo', 'sistema', "status"]
    


class SistemaAdmin(admin.ModelAdmin):
    search_fields = ("nombre"),
    ordering = ('-id',)
    
    list_display = ["id", "nombre"]



  

admin.site.register(Secuencias,SecuenciasAdmin)
admin.site.register(Sistema, SistemaAdmin)
admin.site.register(Invalidar_Secuencia)
admin.site.register(usuario_invalidar)
admin.site.register(usuario_validar)
admin.site.register(usuario_impresion)
admin.site.register(usuario_reporte)
admin.site.register(usuario_auditor)






# Register your models here.
