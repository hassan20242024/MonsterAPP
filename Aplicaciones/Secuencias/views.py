from django.shortcuts import render, redirect
from .models import Secuencias,Proceso,Muestras_y_Placebos, Protocolos, Parametro,Metodo, Ensayo, Sistema, Invalidar_Secuencia,Perfil,usuario_invalidar,usuario_validar, usuario_reporte,usuario_impresion,usuario_auditor
from .forms import secuenciasForm
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Q
import json
from django.core.exceptions import ValidationError
from datetime import datetime
import datetime
from django.utils import formats



# Create your views here.

 
        


@login_required
def crear_secuencias(request):
    titulo="Crear Secuencias"
    secuenicas=Secuencias.objects.all()
    protocolos=Protocolos.objects.all()
    parametros=Parametro.objects.all()
    ensayo=Ensayo.objects.all()
   
    if request.method == "POST":
        form = secuenciasForm(request.POST)
       
        if form.is_valid():
            form.save()
            
            messages.success(request, "Creada con éxito")
           
            return redirect("crear_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("crear_secuencias_en_curso")  
    else:
        form = secuenciasForm() 
        
    context={
        "titulo":titulo,
        "form":form,
        
        
        "secuenicas":secuenicas,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
    }
    
    return render(request, "secuencias/crear_secuencias_en_curso.html", context)

@login_required
def crear_secuencias_en_curso(request):
    #titulo="Crear Secuencias"
    pkt = Protocolos.objects.values("parametro")
    secuencias1=Secuencias.objects.values("parametro_sq")
    secuenicas=Secuencias.objects.all()
    metodo=Metodo.objects.all()
    protocolos=Protocolos.objects.all()
    protocolo_proceso =Proceso.objects.all()
    parametros=Parametro.objects.all()
    ensayo=Ensayo.objects.all()
    sistema=Sistema.objects.all()
    invalidez=Invalidar_Secuencia.objects.all
    usuario=Perfil.objects.all()
    invalidar=usuario_invalidar.objects.filter(usuario=request.user)
    validar=usuario_validar.objects.filter(usuario=request.user)
    protocolos_proceso=Proceso.objects.all()
    muestras=Muestras_y_Placebos.objects.all()

    sist=Sistema.objects.filter(id=1)
   
    if request.method == "POST":
        form = secuenciasForm(request.POST)
       
        if form.is_valid() and secuencias1 == pkt:
            form.save()
            messages.success(request, "Se ha creado un nuevo registro")
           
            return redirect("crear_secuencias_en_curso")
        else:
             print("Error")  
    else:
        form = secuenciasForm() 
        
    context={
        #"titulo":titulo,
        "metodo":metodo,
        "invalidar":invalidar,
        "validar":validar,
        "form":form,
        "invalidez":invalidez,
        "secuenicas":secuenicas,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "usuario":usuario,
         "protocolos_proceso":protocolos_proceso,
         "muestras":muestras,
         "protocolo_proceso":protocolo_proceso,
        
        
         #"parametro_dependiente":parametro_dependiente,
    }
    return render(request, "secuencias/crear_secuencias_en_curso.html", context)

@login_required
def proceso_secuencias_en_curso(request):
    secuenicas=Secuencias.objects.all()
    protocolos=Protocolos.objects.all()
    protocolo_proceso =Proceso.objects.all()
    muestras=Muestras_y_Placebos.objects.all()
    metodo=Metodo.objects.all()
    parametros=Parametro.objects.all()
    ensayo=Ensayo.objects.all()
    sistema=Sistema.objects.all()
    invalidez=Invalidar_Secuencia.objects.all
    invalidar=usuario_invalidar.objects.filter(usuario=request.user)
    validar=usuario_validar.objects.filter(usuario=request.user)
    imprimir=usuario_impresion.objects.filter(usuario=request.user)
    reportar=usuario_reporte.objects.filter(usuario=request.user)
    auditar=usuario_auditor.objects.filter(usuario=request.user)
    usuarios=Perfil.objects.all()
    secuencia=Secuencias.objects.all()
    #secuenciasp = Secuencias.objects.filter(protocolo=1)
    super_usuario=Perfil.objects.all()
    #secuencias1=Reporte.objects.filter(pk=1)
        
    context={
        #"titulo":titulo,
        #"secuenciasp":secuenciasp,
        "invalidar":invalidar,
        "validar":validar,
        "invalidez":invalidez,
        "secuenicas":secuenicas,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "reportar":reportar,
         "secuencia":secuencia,
         "super_usuario":super_usuario,
        "auditar":auditar,
         "imprimir":imprimir,
         "usuarios":usuarios,
         "protocolo_proceso":protocolo_proceso,
         "muestras":muestras,
         "metodo":metodo,
         #"secuencias1":secuencias1,
    
    }
    return render(request, "secuencias/proceso_secuencias_en_curso.html", context)

@login_required
def secuencias_invalidas(request):
    secuencias=Secuencias.objects.all()
    validar=usuario_validar.objects.filter(usuario=request.user)

    
        
    context={
        #"titulo":titulo,
        "secuencias":secuencias,
        "validar":validar
    }
    return render(request, "secuencias/secuencias_invalidas.html", context)


#def chart_js_proceso_secuencias_en_curso(request):
  
    #impresiones_UHPLC_TS_6 = Secuencias.objects.order_by("-sistema").values("sistema").filter(status="Impresa", sistema=1).count()
    #reportes_UHPLC_TS_6 = Secuencias.objects.order_by("-sistema").values("sistema").filter(status="Reportada", sistema=1).count()
    #impresiones_UHPLC_TS_7 = Secuencias.objects.order_by("-sistema").values("sistema").filter(status="Impresa", sistema=2).count()
    #reportes_UHPLC_TS_7 = Secuencias.objects.order_by("-sistema").values("sistema").filter(status="Reportada", sistema=2).count()
    #context={
        #"titulo":titulo,
         #"impresiones_UHPLC_TS_6":impresiones_UHPLC_TS_6,
         #"reportes_UHPLC_TS_6":reportes_UHPLC_TS_6,
        #"impresiones_UHPLC_TS_7":impresiones_UHPLC_TS_7,
         #"reportes_UHPLC_TS_7":reportes_UHPLC_TS_7, 
    #}
    #return render(request, "secuencias/chart_js__proceso_secuencias_en_curso.html", context)
@login_required
def chart_js_proceso_secuencias_en_curso(request):
   registro_total = Secuencias.objects.count()
   pendientes_validaciones = Secuencias.objects.filter(status="Registrada").count()
   pendientes_impresiones = Secuencias.objects.filter(status="Revisada").count()
   pendientes_reportes = Secuencias.objects.filter(status="Impresa").count()
   pendientes_auditorias = Secuencias.objects.filter(status="Reportada").count()
   invalidas = Secuencias.objects.filter(status="Invalida").count()
   ensayos = Secuencias.objects.filter(status="Ensayo").count()
   total_grafico_pie_secuencias=pendientes_validaciones+pendientes_impresiones+pendientes_reportes+pendientes_auditorias
   procentaje_pendientes_validaciones=pendientes_validaciones*100/total_grafico_pie_secuencias
   procentaje_pendientes_impresiones=pendientes_impresiones*100/total_grafico_pie_secuencias
   procentaje_pendientes_reportes=pendientes_reportes*100/total_grafico_pie_secuencias
   procentaje_pendientes_auditorias=pendientes_auditorias*100/total_grafico_pie_secuencias

   pendiente_validación = Secuencias.objects.filter(status="Registrada").count()
   pendiente_impresion = Secuencias.objects.filter(status="Revisada").count()
   pendiente_reporte = Secuencias.objects.filter(status="Impresa").count()
   pendientes_auditoria = Secuencias.objects.filter(status="Reportada").count()
   chart1 = {
        'chart': {'type': 'pie'},
        'title': {'text': ''},
         
     
         "credits": "false",
         
               "plotOptions": {
		"pie": {
			"pointPadding": 0,
			"borderWidth": 8,
            
		}
	},

        'series': [{
             "name": "Status",
            'data': [{
            'y': pendiente_validación,
            'name':  '%s°/° Adquiriendo'% int(procentaje_pendientes_validaciones),
            'color': "#FF6384",
            
            
        }, {
            'y': pendiente_impresion,
            'name':  '%s°/° Impresiones pendientes'  %int(procentaje_pendientes_impresiones),
            'color':  "#63FF84", 
        },{
         'y': pendiente_reporte,
            'name':  '%s°/° Reportes pendientes'  %int(procentaje_pendientes_reportes),
            'color': "#8463FF",
              
        }, {
         'y': pendientes_auditoria,
            'name':  '%s°/° Pendientes por auditar'  %int(procentaje_pendientes_auditorias),
            'color': "#6384FF" 
               
        }
        ]
        }]
    }
   
   chart1A = {
        'chart': {'type': 'column'},
        'title': {'text': ''},
         "credits": "false",
          "xAxis": {
            "categories": ['Adquiriendo', 'Impresiones pendientes', 'Reportes pendientes', 'Pendientes por auditar']
        },
         "plotOptions": {
		"column": {
			"pointPadding": 0.2,
			"borderWidth": 15,
               #"borderColor": "#417690",
		}
	},
    
        'series': [{
            "name": "Status",
            'data': [{
            'y': pendiente_validación,
            'name': "Adquiriendo",
            'color': "#FF6384",
            
        }, {
            'y': pendiente_impresion,
            'name': "Impresiones pendientes",
            'color':  "#63FF84",
        },{
         'y': pendiente_reporte,
            'name': "Reportes pendientes",
            'color':"#8463FF",    
        }, {
         'y': pendientes_auditoria,
            'name': "Pendientes por auditar",
            'color': "#6384FF"    
        }
        ]
        }]
    }
  
   dataset = Secuencias.objects \
        .values('sistema__nombre') \
        .annotate(registrada=Count('sistema', filter=Q(status="Registrada")),
                  validada=Count('sistema', filter=Q(status="Revisada")),
                  impresa=Count('sistema', filter=Q(status="Impresa"))) \
        .order_by('-sistema')

   categories = []
   registrada = list()
   validada = list()
   impresa = list()

   for entry in dataset:
        categories.append('%s ' % entry['sistema__nombre'])
        registrada.append(entry['registrada'])
        validada.append(entry['validada'])
        impresa.append(entry['impresa'])
        

   registrada_series = {
        'name': ' Adquiriendo',
        'data': registrada,
        'color': "#FF6384",
        
    }

   validada_series = {
        'name': 'Impresiones pendientes',
        'data': validada,
        'color': "#63FF84",
    }
   
   impresa_series = {
        'name': 'Reportes pendientes',
        'data': impresa,
        'color': "#8463FF",
    }


   chart = {
        'chart': {'type': 'column' },
        "credits": "false",

        'title': {'text': ''},
        'xAxis': {'categories': categories},
        'series': [registrada_series, validada_series, impresa_series],
         
    }

   dump = json.dumps(chart)
    
   return render(request, 'secuencias/chart_js__proceso_secuencias_en_curso.html', {'chart': dump, "chart1":chart1,"chart1A":chart1A,
    "registro_total":registro_total, "pendientes_validaciones":pendientes_validaciones,"pendientes_impresiones":pendientes_impresiones,
    "pendientes_reportes":pendientes_reportes, "invalidas":invalidas, "pendientes_auditorias":pendientes_auditorias, "ensayos":ensayos})


@login_required
def editar_secuencias_en_curso(request, pk):
    titulo="Crear Secuencias"
  
    secuencia=Secuencias.objects.get(id=pk)
    protocolos=Protocolos.objects.all()
    parametros=Parametro.objects.all()
    sistema=Sistema.objects.all()
    

    ensayo=Ensayo.objects.all()

   
    if request.method == "POST":
        form = secuenciasForm(request.POST, instance=secuencia)
       
        if form.is_valid():
            form.save()
            messages.success(request, "La secuencia ha sido actualizada")
           
            return redirect("crear_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("crear_secuencias_en_curso")    
    else:
        form = secuenciasForm(instance=secuencia) 
        
    context={
        "titulo":titulo,
        "form":form,
        
        
        
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
    return render(request, "secuencias/crear_secuencias_en_curso.html", context)

@login_required
def duplicar_secuencias(request, pk):
    titulo="Crear Secuencias"
  
    secuencia=Secuencias.objects.get(id=pk)
    protocolos=Protocolos.objects.all()
    parametros=Parametro.objects.all()
    sistema=Sistema.objects.all()

    ensayo=Ensayo.objects.all()

   
    if request.method == "POST":
        form = secuenciasForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request, "La secuencia ha sido agregada")
           
            return redirect("crear_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("crear_secuencias_en_curso")    
    else:
        form = secuenciasForm() 
        
    context={
        "titulo":titulo,
        "form":form,
        
        
        
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
    return render(request, "secuencias/crear_secuencias_en_curso.html", context)

@login_required
def duplicar_secuencias_muestras(request, pk):
    titulo="Crear Secuencias"
  
    secuencia=Secuencias.objects.get(id=pk)
    protocolos=Protocolos.objects.all()
    parametros=Parametro.objects.all()
    sistema=Sistema.objects.all()

    ensayo=Ensayo.objects.all()

   
    if request.method == "POST":
        form = secuenciasForm(request.POST)
       
        if form.is_valid():
            form.save()
            messages.success(request, "La secuencia ha sido agregada")
           
            return redirect("crear_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("crear_secuencias_en_curso")    
    else:
        form = secuenciasForm() 
        
    context={
        "titulo":titulo,
        "form":form,
        
        
        
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
    return render(request, "secuencias/crear_secuencias_en_curso.html", context)

@login_required
def invalidar_prueba(request, pk):
    titulo="Crear Secuencias"
  
    
    protocolos=Protocolos.objects.all()
    parametros=Parametro.objects.all()
    sistema=Sistema.objects.all()

    ensayo=Ensayo.objects.all()

   
    if request.method == "POST":
        secuencia=Secuencias.objects.get(id=pk)
        secuencia.headline
        form = secuenciasForm( instance=secuencia)
       
        if form.is_valid():
            form.save()
            Secuencias.objects.filter(id=pk).update(
        status="Invalida"
        )
            messages.success(request, "La secuencia ha sido actualizada")
           
            return redirect("crear_secuencias_en_curso")
        else:
             print("Error")  
    else:
        form = secuenciasForm(instance=secuencia) 
        
    context={
        "titulo":titulo,
        "form":form,
        
        
        "secuenicas":secuencia,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
    return render(request, "secuencias/crear_secuencias_en_curso.html", context)

@login_required
def invalidar_secuencias(request, pk):
   
  
   titulo="Crear Secuencias"
   secuencia=Secuencias.objects.get(id=pk)
   protocolos=Protocolos.objects.all()
   parametros=Parametro.objects.all()
   sistema=Sistema.objects.all()
   date_joined = datetime.datetime.now()
  
    

   ensayo=Ensayo.objects.all()

   
   if request.method == "POST":
        form = secuenciasForm(request.POST, instance=secuencia)
       
        if form.is_valid():
            form.save()
            Secuencias.objects.filter(id=pk).update(
        status="Invalida", fecha_invalidar=date_joined
        )
          
            

          
            messages.success(request, "La secuencia ha sido invalidada")
           
            return redirect("crear_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("crear_secuencias_en_curso")    
   else:
        form = secuenciasForm(instance=secuencia) 
        
   context={
        "titulo":titulo,
        "form":form,
        
        
        "secuenica":secuencia,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
   return render(request, "secuencias/crear_secuencias_en_curso.html", context)

@login_required
def validar_secuencias(request, pk):
   
  
   titulo="Crear Secuencias"
   secuencia=Secuencias.objects.get(id=pk)
   protocolos=Protocolos.objects.all()
   parametros=Parametro.objects.all()
   sistema=Sistema.objects.all()
   date_joined = datetime.datetime.now()
  
    

   ensayo=Ensayo.objects.all()
   fecha_Final=Secuencias.objects.values("fecha_Final").filter(id=pk)
   fecha_Inicio=Secuencias.objects.values("fecha_Inicio").filter(id=pk) 
   def clean_date(self):
    date = self.cleaned_data['fecha_Final']
    date1 = self.cleaned_data['fecha_Inicio']
    if date < date1:
        raise ValidationError(self.error_messages['Date cannot be in the past'], code='Date cannot be in the past') 
       
   if request.method == "POST":

     
        form = secuenciasForm(request.POST, instance=secuencia)
       
        if form.is_valid():
            form.save()
            Secuencias.objects.filter(id=pk).update(
        status="Revisada", fecha_validar=date_joined
        )
          
            messages.success(request, "La secuencia ha sido validada")
           
            return redirect("crear_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("crear_secuencias_en_curso")    
   else:
        form = secuenciasForm(instance=secuencia) 
           
   def clean_date(self):
       fecha_Final=Secuencias.objects.filter("fecha_Final")
       
   context={
        "titulo":titulo,
        "form":form,
        
        
        "secuenica":secuencia,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
         "clean_date":clean_date,
         "fecha_Final":fecha_Final,
         "fecha_Inicio":fecha_Inicio,

    }
  
   return render(request, "secuencias/crear_secuencias_en_curso.html", context)

@login_required
def editar_secuencias(request, pk):
    titulo="Editar Secuencias"
    protocolos=Protocolos.objects.all()
    parametros=Parametro.objects.all()
    ensayo=Ensayo.objects.all()
    secuencias1=Secuencias.objects.filter(pk=pk)
   
    context={
        "titulo":titulo,
        "protocolos":protocolos,
        "parametros":parametros,
        "ensayo":ensayo,
        "secuencias1":secuencias1
    }
    return render(request, "secuencias/editarSecuencias.html", context)

@login_required
def actualizarEstadoParametros(request, pk):
   
    secuencias1=Secuencias.objects.filter(id=pk)
    secuencias=Secuencias.objects.all()
    for item in secuencias1:
        for items in item.protocolo.parametro.all():
              
         if items.status_parametro > "Auditado":

            Parametro.objects.filter(pk=pk).update(
                status_parametro="Revisado"
            )
    return redirect("secuencias") 

@login_required
def impresion_secuencia(request, pk):
   titulo="Crear Secuencias"
   secuencia=Secuencias.objects.get(id=pk)
   protocolos=Protocolos.objects.all()
   parametros=Parametro.objects.all()
   sistema=Sistema.objects.all()
   ensayo=Ensayo.objects.all()
   date_joined = datetime.datetime.now()
   
   if request.method == "POST":
        form = secuenciasForm(request.POST, instance=secuencia)
        if form.is_valid() :
          
            prueba =form.save(commit=False)
            prueba.user =request.user
            form.save()
          
            Secuencias.objects.filter(id=pk).update(
        status="Impresa" , fecha_impresion = date_joined
        )
       
            
            messages.success(request, "La secuencia ha sido impresa")
            return redirect("proceso_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("proceso_secuencias_en_curso")    
   else:
        form = secuenciasForm(instance=secuencia) 
        
   context={
        "titulo":titulo,
        "form":form,
        "secuenica":secuencia,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
   return render(request, "secuencias/proceso_secuencias_en_curso.html", context)

@login_required
def reporte_secuencias(request, pk):
   titulo="Crear Secuencias"
   protocolos=Protocolos.objects.all()
   parametros=Parametro.objects.all()
   sistema=Sistema.objects.all()
   ensayo=Ensayo.objects.all()
   date_joined = datetime.datetime.now()

   if request.method == "POST":
        secuencia=Secuencias.objects.get(id=pk)

        form = secuenciasForm(request.POST, instance=secuencia)
        if form.is_valid():
           #form.save()
            prueba =form.save(commit=False)
            prueba.secuencia =request.user
            prueba.save()
            Secuencias.objects.filter(id=pk).update(
        status="Reportada", fecha_reporte = date_joined
        )
            messages.success(request, "La secuencia ha sido reportada")
            return redirect("proceso_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("proceso_secuencias_en_curso")    
   else:
        form = secuenciasForm(instance=secuencia) 
        
   context={
        "titulo":titulo,
        "form":form,
        "secuenica":secuencia,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
   return render(request, "secuencias/proceso_secuencias_en_curso.html", context)

@login_required
def auditar_secuencias(request, pk):
   titulo="Crear Secuencias"
   protocolos=Protocolos.objects.all()
   parametros=Parametro.objects.all()
   sistema=Sistema.objects.all()
   ensayo=Ensayo.objects.all()
   date_joined = datetime.datetime.now()

   if request.method == "POST":
        secuencia=Secuencias.objects.get(id=pk)

        form = secuenciasForm(request.POST, instance=secuencia)
        if form.is_valid():
           #form.save()
            prueba =form.save(commit=False)
            prueba.secuencia =request.user
            prueba.save()
            Secuencias.objects.filter(id=pk).update(
        status="Auditada", fecha_auditada = date_joined
        )
            messages.success(request, "La secuencia ha sido auditada")
            return redirect("proceso_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("proceso_secuencias_en_curso")    
   else:
        form = secuenciasForm(instance=secuencia) 
        
   context={
        "titulo":titulo,
        "form":form,
        "secuenica":secuencia,
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
   return render(request, "secuencias/proceso_secuencias_en_curso.html", context)

@login_required
def actualizar_secuencias_validadas(request, pk):
   titulo="Crear Secuencias"
  
   secuencia=Secuencias.objects.get(id=pk)
   protocolos=Protocolos.objects.all()
   parametros=Parametro.objects.all()
   sistema=Sistema.objects.all()
   ensayo=Ensayo.objects.all()

   if request.method == "POST":
        form = secuenciasForm(request.POST, instance=secuencia)
       
        if form.is_valid():
            form.save()
            messages.success(request, "La secuencia ha sido actualizada")
           
            return redirect("proceso_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("crear_secuencias_en_curso")    
   else:
        form = secuenciasForm(instance=secuencia) 
        
   context={
        "titulo":titulo,
        "form":form,
        
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
   return render(request, "secuencias/actualizar_secuencias_validadas.html", context)

@login_required
def cambiar_estado_ensayo(request, pk):
   titulo="Crear Secuencias"
  
   secuencia=Secuencias.objects.get(id=pk)
   protocolos=Protocolos.objects.all()
   parametros=Parametro.objects.all()
   sistema=Sistema.objects.all()
   ensayo=Ensayo.objects.all()

   if request.method == "POST":
        form = secuenciasForm(request.POST, instance=secuencia)
       
        if form.is_valid():
            form.save()
            Secuencias.objects.filter(id=pk).update(
        status="Ensayo", )
            messages.success(request, "La secuencia ha sido actualizada")
           
            return redirect("proceso_secuencias_en_curso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             return redirect("crear_secuencias_en_curso")    
   else:
        form = secuenciasForm(instance=secuencia) 
        
   context={
        "titulo":titulo,
        "form":form,
        
        "protocolos":protocolos,
        "parametros":parametros,
         "ensayo":ensayo,
         "sistema":sistema,
         "secuencia":secuencia,
    }
   return render(request, "secuencias/cambiar_estado_ensayo.html", context)


