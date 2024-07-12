from django.db import models
from django.conf import settings
from Aplicaciones.Protocolo_Metodos.models import Protocolos, Parametro, Ensayo
from Aplicaciones.perfiles.models import Perfil
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q
import datetime


# Create your models here.

class Sistema(models.Model):
    nombre=models.CharField(max_length=250, verbose_name="Sistema",  null=True, blank=False)
    class Condicion(models.TextChoices):
        ACTIVO = "Activo", "ACTIVO"
        PASIVO = "Pasivo", "PASIVO"
    condicion=models.CharField(max_length=90, choices=Condicion.choices, default=Condicion.ACTIVO, verbose_name="Condicion")  
    
    def __str__(self):    

        return(self.nombre)

class Invalidar_Secuencia(models.Model):
    razon=models.CharField(max_length=250, verbose_name="Causa",  null=True, blank=False)
    class Condicion(models.TextChoices):
        ACTIVO = "Activo", "ACTIVO"
        PASIVO = "Pasivo", "PASIVO"
    condicion=models.CharField(max_length=90, choices=Condicion.choices, default=Condicion.ACTIVO, verbose_name="Condicion")  
    
    def __str__(self):    

        return(self.razon) 

class usuario_invalidar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Python 3
    def __str__(self): 
        return self.usuario.username   
class usuario_validar(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Python 3
    def __str__(self): 
        return self.usuario.username
           
class usuario_impresion(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Python 3
    def __str__(self): 
        return self.usuario.username
    
class usuario_reporte(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Python 3
    def __str__(self): 
        return self.usuario.username

class usuario_auditor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # Python 3
    def __str__(self): 
        return self.usuario.username         
    



class Secuencias(models.Model):
    #order_number = models.IntegerField(primary_key=False, blank=True, null=True, default=0 )
    fecha_Invalidez=models.DateTimeField(verbose_name="Fecha ID", null=True, blank=True, default=datetime.datetime.now)
    nombre=models.CharField(max_length=250, verbose_name="Nombre",  null=False, blank=False)
    fecha_Inicio=models.DateTimeField(verbose_name="Fecha de Inicio", null=False, blank=False)
    #hora_Inicio=models.TimeField(verbose_name="Hora de Inicio", null=True, blank=True )
    fecha_Final=models.DateTimeField(verbose_name="Fecha de Finalización", null=True, blank=True)
    #hora_Final=models.TimeField(verbose_name="Hora de Finalización", null=True, blank=True )
    protocolo=models.ForeignKey(to=Protocolos, on_delete=models.CASCADE, verbose_name="Protocolo", null=True, blank=True)
    sistema=models.ForeignKey(to=Sistema, on_delete=models.CASCADE, verbose_name="Sistema", null=True, blank=False)
    class Status(models.TextChoices):
        REGISTRADA = "Registrada", "REGISTRADA"
        INVALIDA = "Invalida", "INVALIDA"
        REVISADA = "Revisada", "REVISADA"
        IMPRESA = "Impresa", "IMPRESA"
        REPORTADA = "Reportada", "REPORTADA"
        AUDITADA = "Auditada", "AUDITADA"
    status=models.CharField(max_length=90, choices=Status.choices, default=Status.REGISTRADA, verbose_name="Status", null=True, blank=True)  
    class Condicion(models.TextChoices):
        ACTIVO = "Activo", "ACTIVO"
        PASIVO = "Pasivo", "PASIVO"
    condicion=models.CharField(max_length=90, choices=Condicion.choices, default=Condicion.ACTIVO, verbose_name="Condicion", null=True, blank=True)  
    observaciones=models.CharField(max_length=250, verbose_name="Observaciones",  null=True, blank=False)
    parametro_sq=models.ForeignKey(to=Parametro, on_delete=models.CASCADE, verbose_name="Parametro", null=True, blank=True)
    invalidez=models.ForeignKey(to=Invalidar_Secuencia, on_delete=models.CASCADE, verbose_name="Invalidar", null=True, blank=True, default="N.A")
    fecha_invalidar=models.DateTimeField(verbose_name="Fecha de Invalidéz", null=True, blank=True)
    fecha_validar=models.DateTimeField(verbose_name="Fecha de Validación", null=True, blank=True)
    fecha_impresion=models.DateTimeField(verbose_name="Fecha de Impresión", null=True, blank=True)
    fecha_reporte=models.DateTimeField(verbose_name="Fecha de Reporte", null=True, blank=True)
    fecha_auditada=models.DateTimeField(verbose_name="Fecha auditada", null=True, blank=True)
    def individual():
     " This function will be called when a default value is needed.ll return a 31 length string with a-z, 0-9."
     return 'Prueba'
    referencia=models.CharField(max_length=250, verbose_name="Referencia Reporte",  null=True, blank=True,default=individual)
    invalidar=models.ForeignKey(to=usuario_invalidar, on_delete=models.CASCADE, verbose_name="Invalidada por", null=True, blank=True)
    validar=models.ForeignKey(to=usuario_validar, on_delete=models.CASCADE, verbose_name="Validada por", null=True, blank=True)
    imprimir=models.ForeignKey(to=usuario_impresion, on_delete=models.CASCADE, verbose_name="Impresa por", null=True, blank=True)
    reportar=models.ForeignKey(to=usuario_reporte, on_delete=models.CASCADE, verbose_name="Reportada por", null=True, blank=True)
    auditar=models.ForeignKey(to=usuario_auditor, on_delete=models.CASCADE, verbose_name="Auditada por", null=True, blank=True)
   
    class Meta:
       unique_together = ("protocolo", "parametro_sq", "fecha_Invalidez")

    #def clean_end_time(self):
        #if self.fecha_Final < self.fecha_Inicio:
            #raise ValidationError('La fecha de termino debe ser mayor a la de inicio')
  


    #reportado_por=models.ForeignKey(to=Generar_reporte, on_delete=models.CASCADE, verbose_name="Usuario", null=True, blank=True)
    
    def nombre_Secuencia(self):
        return "{}".format(self.nombre)    
    def __str__(self):    

        return str(self.nombre_Secuencia())
    

    











