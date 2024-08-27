from django.contrib import admin
from .models import Viabilidad
#from .models import Estado_Proceso
from .models import Proceso

class ProcesoAdmin(admin.ModelAdmin):
    search_fields = ("codigo_metodo"),
    list_display = ["id","codigo", "nombre" ]  

# Register your models here.
admin.site.register(Viabilidad)
#admin.site.register(Estado_Proceso)
admin.site.register(Proceso, ProcesoAdmin)

