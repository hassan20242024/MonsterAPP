from django.shortcuts import render, redirect

from .models import Protocolos,Subparametro, Parametro, Metodologia,EstadoProtocolo,Viabilidad,Titulo_Parametro,Muestras_y_Placebos,Ensayo, Cliente
from .forms import ProtocolosForm,ParametroForm, MetodologiaForm, EstadoProtocoloForm, crear_ensayoForm,ViabilidadForm, SubparametroForm,Titulo_ParametroForm, ingresar_muestrasForm, clienteForm
from Aplicaciones.Secuencias.models import Secuencias
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def protocolo_metodos(request):
    titulo = "Protocolo de Métodos"
    protocolo_metodos=Protocolos.objects.all()
    #secuencia_registro = Secuencias.objects.filter(status="Registrada").count()
    
    context = {

        "titulo": titulo,
        "protocolo_metodos": protocolo_metodos,
       
        "crear_metodologia":crear_metodologia,
        #"secuencia_registro":secuencia_registro,
    }
    return render(request, "protocolo_metodos/protocolo_metodos.html", context)




#def crear_protocolo_metodos(request):  
  
    protocolo_metodos=Protocolos.objects.all()
    seleccionarEnsayo=Ensayo.objects.all()
    ingresar_muestras=Muestras_y_Placebos.objects.all()
    seleccionarParametro=Parametro.objects.all()
    seleccionarMetodologia=Metodologia.objects.all()
    seleccionarEstadoProtocolo=EstadoProtocolo.objects.all()
    seleccionarViabilidad=Viabilidad.objects.all()
    titulo="Crear Protocolos"
    if request.method == "POST":
         if request.POST.get('txtFechaIngreso') and \
            request.POST.get('txtCodigo') and \
            request.POST.get('nombreProtocolo') and \
            request.POST.get('txtEnsayo_id') and \
            request.POST.get('seleccionMetodologia_id') and \
            request.POST.get('txtParametro_id') and \
            request.POST.get('muestrasyPlacebos') and \
            request.POST.get('insumosProceso') and \
            request.POST.get('estadoProtocolo_id') and \
            request.POST.get('txtObserbaciones'):
             
            generarProtocolo = Protocolos()
       

            generarProtocolo.fecha_ingreso = request.POST.get("txtFechaIngreso") 
            generarProtocolo.codigo =request.POST.get('txtCodigo')
            generarProtocolo.nombre =request.POST.get('nombreProtocolo')
            generarProtocolo.ensayo_id =request.POST.get('txtEnsayo_id')
            generarProtocolo.metodologia_id =request.POST.get('seleccionMetodologia_id')
            generarProtocolo.estado_protocolo_id =request.POST.get('estadoProtocolo_id')
            generarProtocolo.observaciones =request.POST.get('txtObserbaciones')
            generarProtocolo.save()
            
            generarProtocolo.muestras_y_Placebos.set(request.POST.getlist('muestrasyPlacebos'))
            generarProtocolo.parametro.set(request.POST.getlist('txtParametro_id'))
       
            generarProtocolo.viabilidad.set(request.POST.getlist('insumosProceso'))
            
        

       
            return redirect("protocolo_metodos")
    else:
   
     context={
        "protocolo_metodos":protocolo_metodos,
        "seleccionarEnsayo":seleccionarEnsayo,
        "ingresar_muestras":ingresar_muestras,
        "seleccionarParametro":seleccionarParametro,
        "seleccionarMetodologia":seleccionarMetodologia,
        "seleccionarEstadoProtocolo":seleccionarEstadoProtocolo,
        "seleccionarViabilidad":seleccionarViabilidad,
        "titulo":titulo,
    }
    return render(request, "protocolo_metodos/crear_protocolo_metodos.html", context)

@login_required
def crear_protocolo_metodos(request):
    titulo="Crear Protocolos"
    protocolo_metodos=Protocolos.objects.all()
   
    if request.method == "POST":
        form = ProtocolosForm(request.POST or None)
       
        if form.is_valid():
            form.save()

            messages.success(request, "Protocolo creado satisfactoriamente")
           
            return redirect("protocolo_metodos")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             #return redirect("crear_protocolo_metodos")
    else:
            
        form = ProtocolosForm() 
        
    context={
        "titulo":titulo,
        "form":form,
        
        
        "protocolo_metodos":protocolo_metodos
    }
    return render(request, "protocolo_metodos/crear_protocolo_metodos.html", context)


#def editar_protocolo_metodos(request, id):
    titulo = "Edicion de Métodos"
    
    seleccionarEnsayo=Ensayo.objects.all()
    ingresar_muestras=Muestras_y_Placebos.objects.all()
    seleccionarParametro=Parametro.objects.all()
    seleccionarMetodologia=Metodologia.objects.all()
    seleccionarEstadoProtocolo=EstadoProtocolo.objects.all()
    seleccionarViabilidad=Viabilidad.objects.all()
    generarProtocolo = Protocolos.objects.get(id=id)
   

    context = {
        "titulo": titulo,
        "seleccionarEnsayo":seleccionarEnsayo,
        "ingresar_muestras":ingresar_muestras,
        "seleccionarParametro":seleccionarParametro,
        "seleccionarMetodologia":seleccionarMetodologia,
        "seleccionarEstadoProtocolo":seleccionarEstadoProtocolo,
        "seleccionarViabilidad":seleccionarViabilidad,
     
        "generarProtocolo":generarProtocolo,

    }
    return render(request, "protocolo_metodos/editar_protocolo_metodos.html", context)

#def accion_editar_protocolo_metodos(request, id):
    
    seleccionarEnsayo=Ensayo.objects.all()
    ingresar_muestras=Muestras_y_Placebos.objects.all()
    seleccionarParametro=Parametro.objects.all()
    seleccionarMetodologia=Metodologia.objects.all()
    seleccionarEstadoProtocolo=EstadoProtocolo.objects.all()
    seleccionarViabilidad=Viabilidad.objects.all()
 
    
    titulo="Crear Protocolos"
    if request.method == "POST":
         if request.POST.get('txtFechaIngreso') and \
            request.POST.get('txtCodigo') and \
            request.POST.get('nombreProtocolo') and \
            request.POST.get('txtEnsayo_id') and \
            request.POST.get('seleccionMetodologia_id') and \
            request.POST.get('txtParametro_id') and \
            request.POST.get('muestrasyPlacebos') and \
            request.POST.get('insumosProceso') and \
            request.POST.get('estadoProtocolo_id') and \
            request.POST.get('txtObserbaciones'):
             
            generarProtocolo = Protocolos.objects.get(id=id)
            generarProtocolo.fecha_ingreso = request.POST.get("txtFechaIngreso")
            generarProtocolo.codigo =request.POST.get('txtCodigo')
            generarProtocolo.nombre =request.POST.get('nombreProtocolo')
            generarProtocolo.ensayo__id =request.POST.get('txtEnsayo_id') 
            
            generarProtocolo.metodologia__id =request.POST.get('seleccionMetodologia_id')
            generarProtocolo.estado_protocolo__id =request.POST.get('estadoProtocolo_id')
            generarProtocolo.observaciones =request.POST.get('txtObserbaciones')
          
            generarProtocolo.save()
            
            generarProtocolo.muestras_y_Placebos.set(request.POST.getlist('muestrasyPlacebos'))
            generarProtocolo.parametro.set(request.POST.getlist('txtParametro_id'))
       
            generarProtocolo.viabilidad.set(request.POST.getlist('insumosProceso.id'))
            
            
            
            
            protocolo_metodos=Protocolos.objects.all()
            
        

       
            return redirect("protocolo_metodos")
    else:
     
   
     context={
        "protocolo_metodos":protocolo_metodos,
        "seleccionarEnsayo":seleccionarEnsayo,
        "ingresar_muestras":ingresar_muestras,
        "seleccionarParametro":seleccionarParametro,
        "seleccionarMetodologia":seleccionarMetodologia,
        "seleccionarEstadoProtocolo":seleccionarEstadoProtocolo,
        "seleccionarViabilidad":seleccionarViabilidad,
        "titulo":titulo
    }
    return render(request, "protocolo_metodos/editar_protocolo_metodos.html", context)   

@login_required
def configuracion_protocolo_metodos(request):
    titulo = "Ajustes Protocolo de Métodos/Parámetros"
    Pto=Parametro.objects.all()
    tituloParametro=Titulo_Parametro.objects.all()
    nombreSubparametro=Subparametro.objects.all()

    if request.method == "POST":
        form = ParametroForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("configuracion_protocolo_metodos")
        else:
             print("Error")  
    else:
        form = ParametroForm() 
    
    context={
        "titulo":titulo,
        "form":form,
       "Pto": Pto,
       "tituloParametro":tituloParametro,
       "nombreSubparametro":nombreSubparametro
    }
    
   
    return render(request, "protocolo_metodos/configuracion_protocolo_metodos.html", context)

@login_required
def editar_protocolo_metodos(request, pk):



    titulo="Editar Protocolos"
    protocolo_metodo=Protocolos.objects.get(id=pk)
    protocolo_metodos=Protocolos.objects.all()

    if request.method == "POST":
         form = ProtocolosForm(request.POST, instance=protocolo_metodo)
         #messages.success(request, "Editada con exito")
         if form.is_valid():
           form.save()
           messages.success(request, "Protocolo editado correctamente")
           return redirect("protocolo_metodos")
         else:
           messages.error(request, "Por favor revisa los datos ingresados")  
    else:
          form = ProtocolosForm(instance=protocolo_metodo)
    context={
    "titulo":titulo,
    "form":form,
    "protocolo_metodo": protocolo_metodo,
    "protocolo_metodos":protocolo_metodos
   
}
    return render(request, "protocolo_metodos/edicion_protocolo_metodos.html", context)

@login_required
def revisar_protocolo_metodos(request, pk):

    titulo="Revisar Protocolos"
    protocolo_metodo=Protocolos.objects.get(id=pk)
    pkt = Protocolos.objects.filter(id=pk)
    a=2
    secuencias1=Secuencias.objects.filter(protocolo=pk)
    status_secuencia=Secuencias.objects.filter(status=pk)
    contarParametroProtocolo=Protocolos.objects.values("parametro").filter(id=pk).count()
     
    contarStatusRegistrada=Secuencias.objects.filter(protocolo=pk, status="Registrada").count()
    contarStatusRevisada=Secuencias.objects.filter(protocolo=pk, status="Revisada").count()
    contarStatusImpresa=Secuencias.objects.filter(protocolo=pk, status="Impresa").count()
    contarStatusReportada=Secuencias.objects.filter(protocolo=pk, status="Reportada").count()
    contarStatusAuditada=Secuencias.objects.filter(protocolo=pk, status="Auditada").count()

    porcentajeStatusRegistrada=contarStatusRegistrada*20/contarParametroProtocolo
    porcentajeStatusRevisada=contarStatusRevisada*40/contarParametroProtocolo
    porcentajeStatusImpresa=contarStatusImpresa*60/contarParametroProtocolo
    porcentajeStatusReportada=contarStatusReportada*80.0/contarParametroProtocolo
    porcentajeStatusAuditada=contarStatusAuditada*100/contarParametroProtocolo
   
  

    labels = []
    data = []

    queryset = Secuencias.objects.order_by('-nombre')[:5]
    for city in queryset:
        labels.append(city.nombre)
        data.append(city.nombre)
  
    context={
         
        "titulo":titulo,
   
    "protocolo_metodo": protocolo_metodo,
    "pkt":pkt,
    "secuencias1":secuencias1,
    "status_secuencia":status_secuencia,
    "labels":labels,
    "data":data,
    "queryset":queryset,
    "contarParametroProtocolo":contarParametroProtocolo,
    "a":a,
    "contarStatusRegistrada":contarStatusRegistrada,
    "contarStatusRevisada":contarStatusRevisada,
    "contarStatusImpresa":contarStatusImpresa,
    "contarStatusReportada":contarStatusReportada,
    "contarStatusAuditada":contarStatusAuditada,
    "porcentajeStatusRegistrada":porcentajeStatusRegistrada,
    "porcentajeStatusRevisada":porcentajeStatusRevisada,
    "porcentajeStatusImpresa":porcentajeStatusImpresa,
    "porcentajeStatusReportada":porcentajeStatusReportada,
    "porcentajeStatusAuditada":porcentajeStatusAuditada,
   

}
    return render(request, "protocolo_metodos/revisar_protocolo_metodos.html", context)

@login_required
def editar_parametro(request, pk):
    titulo="Editar Parámetros"
   
   
    if request.method == "POST":
        Pto=Parametro.objects.get(pk=pk)
        form = ParametroForm(request.POST, instance=Pto)
        if form.is_valid():
            form.save()
           
            return redirect("configuracion_protocolo_metodos")
        else:
             print("Error")  
    else:
        form = ParametroForm(instance=Pto)

    context={
        "titulo":titulo,
        "form":form,
        "Pto":Pto
    }
    return render(request, "protocolo_metodos/configuracion_protocolo_metodos.html", context)

@login_required
def subparametro(request):
    titulo="Ajustes Protocolo de Métodos/Subparametros"
    subparametro=Subparametro.objects.all()
    
    if request.method == "POST":
        form = SubparametroForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("subparametro")
        else:
             print("Error")  
    else:
        form = SubparametroForm() 
    context={
        "titulo":titulo,
        "form":form,
        "subparametro":subparametro
    }
    return render(request, "protocolo_metodos/subparametro.html", context)

@login_required
def editar_subparametro(request, pk):
    titulo="Ajustes Protocolo de Métodos/Subparametros"
    subparametro=Subparametro.objects.get(id=pk)
    
    if request.method == "POST":
        form = SubparametroForm(request.POST, instance=subparametro)
        if form.is_valid():
            form.save()
            return redirect("subparametro")
        else:
             print("Error")  
    else:
        form = SubparametroForm(instance=subparametro) 
    context={
        "titulo":titulo,
        "form":form,
        "subparametro":subparametro
    }
    return render(request, "protocolo_metodos/subparametro.html", context)

@login_required
def titulo_parametro(request):
    titulo="Ajustes Protocolo de Métodos/Titulo parámetro"
    titulo_parametro=Titulo_Parametro.objects.all()
    
    if request.method == "POST":
        form = Titulo_ParametroForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("titulo_parametro")
        else:
             print("Error")  
    else:
        form = Titulo_ParametroForm() 
    context={
        "titulo":titulo,
        "form":form,
        "titulo_parametro":titulo_parametro
    }
    return render(request, "protocolo_metodos/titulo_parametro.html", context)

@login_required
def editar_titulo_parametro(request, pk):
    titulo="Editar Título Parámetro"
    titulo_parametro=Titulo_Parametro.objects.get(id=pk)
   
    if request.method == "POST":
        form = Titulo_ParametroForm(request.POST, instance=titulo_parametro)
        if form.is_valid():
            form.save()
           
            return redirect("titulo_parametro")
        else:
             print("Error")  
    else:
        form = Titulo_ParametroForm(instance=titulo_parametro)

    context={
        "titulo":titulo,
        "form":form,
        "titulo_parametro":titulo_parametro
    }
    return render(request, "protocolo_metodos/titulo_parametro.html", context)

@login_required
def crear_metodologia(request):
    titulo="Ajustes Protocolo de Métodos/Metodologia"
    crear_metodologia=Metodologia.objects.all()
    
    
    if request.method == "POST":
        form = MetodologiaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("crear_metodologia")
        else:
             print("Error")  
    else:
        form = MetodologiaForm() 
    context={
        "titulo":titulo,
        "form":form,
        "crear_metodologia":crear_metodologia
    }
    return render(request, "protocolo_metodos/crear_metodologia.html", context)

@login_required
def editar_metodologia(request, pk):
    titulo="Ajustes Protocolo de Métodos/Metodologia"
    crear_metodologia=Metodologia.objects.get(id=pk)
    
    
    if request.method == "POST":
        form = MetodologiaForm(request.POST, instance=crear_metodologia)
        if form.is_valid():
            form.save()
            return redirect("crear_metodologia")
        else:
             print("Error")  
    else:
        form = MetodologiaForm(instance=crear_metodologia) 
    context={
        "titulo":titulo,
        "form":form,
        "crear_metodologia":crear_metodologia
    }
    return render(request, "protocolo_metodos/crear_metodologia.html", context)

@login_required
def definir_estado(request):
    titulo="Ajustes Protocolo de Métodos/Estado"
    definir_estado=EstadoProtocolo.objects.all()
    
    
    if request.method == "POST":
        form = EstadoProtocoloForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("definir_estado")
        else:
             print("Error")  
    else:
        form = EstadoProtocoloForm() 
    context={
        "titulo":titulo,
        "form":form,
        "definir_estado":definir_estado
    }
    return render(request, "protocolo_metodos/definir_estado.html", context)

@login_required
def editar_definir_estado(request,pk):
    titulo="Ajustes Protocolo de Métodos/Estado"
    definir_estado=EstadoProtocolo.objects.get(id=pk)
    
    
    if request.method == "POST":
        form = EstadoProtocoloForm(request.POST, instance=definir_estado)
        if form.is_valid():
            form.save()
            return redirect("definir_estado")
        else:
             print("Error")  
    else:
        form = EstadoProtocoloForm(instance=definir_estado) 
    context={
        "titulo":titulo,
        "form":form,
        "definir_estado":definir_estado
    }
    return render(request, "protocolo_metodos/definir_estado.html", context)

@login_required
def crear_ensayo(request):
    titulo="Ajustes Protocolo de Métodos/Ensayo"
    crear_ensayo=Ensayo.objects.all()
    if request.method == "POST":
        form = crear_ensayoForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("crear_ensayo")
        else:
             print("Error")  
    else:
        form = crear_ensayoForm() 
    context={
        "titulo":titulo,
        "form":form,
        "crear_ensayo":crear_ensayo,
        
    }
    return render(request, "protocolo_metodos/crear_ensayo.html", context)

@login_required
def editar_ensayo(request, pk):
    titulo="Ajustes Protocolo de Métodos/Ensayo"
    crear_ensayo=Ensayo.objects.get(id=pk)
    if request.method == "POST":
        form = crear_ensayoForm(request.POST, instance=crear_ensayo)
        if form.is_valid():
            form.save()
            return redirect("crear_ensayo")
        else:
             print("Error")  
    else:
        form = crear_ensayoForm(instance=crear_ensayo) 
    context={
        "titulo":titulo,
        "form":form,
        "crear_ensayo":crear_ensayo,
        
    }
    return render(request, "protocolo_metodos/crear_ensayo.html", context)

@login_required
def insumosDelProceso(request):
    titulo="Ajustes Protocolo de Métodos/Insumos del Proceso"
    viabilidad=Viabilidad.objects.all()
    
    
    if request.method == "POST":
        form = ViabilidadForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("insumosDelProceso")
        else:
             print("Error")  
    else:
        form = ViabilidadForm() 
    context={
        "titulo":titulo,
        "form":form,
        "viabilidad":viabilidad
    }
    return render(request, "protocolo_metodos/insumosDelProceso.html", context)

@login_required
def editar_insumosDelProceso(request, pk):
    titulo="Ajustes Protocolo de Métodos/Insumos del Proceso"
    viabilidad=Viabilidad.objects.get(id=pk)
    
    
    if request.method == "POST":
        form = ViabilidadForm(request.POST, instance=viabilidad)
        if form.is_valid():
            form.save()
            return redirect("insumosDelProceso")
        else:
             print("Error")  
    else:
        form = ViabilidadForm(instance=viabilidad) 
    context={
        "titulo":titulo,
        "form":form,
        "viabilidad":viabilidad
    }
    return render(request, "protocolo_metodos/insumosDelProceso.html", context)

@login_required
def crear_cliente(request):
    titulo="Ajustes Protocolo de Métodos/Clientes"
    crear_cliente=Cliente.objects.all()
    if request.method == "POST":
        form = clienteForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("crear_cliente")
        else:
             print("Error")  
    else:
        form = clienteForm() 
    context={
        "titulo":titulo,
        "form":form,
        "crear_cliente":crear_cliente,
        
    }
    return render(request, "protocolo_metodos/clientes.html", context)

    
@login_required
def editar_cliente(request, pk):
    titulo="Ajustes Protocolo de Métodos/Clientes"
    crear_cliente=Cliente.objects.get(id=pk)
    if request.method == "POST":
        form = clienteForm(request.POST, instance=crear_cliente)
        if form.is_valid():
            form.save()
            return redirect("crear_cliente")
        else:
             print("Error")  
    else:
        form = clienteForm(instance=crear_cliente) 
    context={
        "titulo":titulo,
        "form":form,
        "crear_cliente":crear_cliente,
        
    }
    return render(request, "protocolo_metodos/clientes.html", context)

@login_required
def detalles_protocolo_metodos(request):
    titulo = "Detalles del Protocolo"
    protocolo_metodos=Protocolos.objects.all()
    
    context = {

        "titulo": titulo,
        "protocolo_metodos": protocolo_metodos,
       
    }

    return render(request, "protocolo_metodos/detalles_protocolo_metodos.html", context)

@login_required
def ingresar_muestras(request):
    titulo="Ingreso de Muestras"
    ingresar_muestras=Muestras_y_Placebos.objects.all()
    
    
    if request.method == "POST":
        form = ingresar_muestrasForm(request.POST or None)
     
        if form.is_valid():
            form.save()
            messages.success(request, "Registro creado satisfactoriamente")
            return redirect("ingresar_muestras")
        else:
             messages.error(request, "por favor, revise los datos ingresados") 
    else:
        form = ingresar_muestrasForm() 
    context={
        "titulo":titulo,
        "form":form,
        "ingresar_muestras":ingresar_muestras
    }

    return render(request, "protocolo_metodos/ingresar_muestras.html", context)































    
        


    
