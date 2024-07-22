from django.shortcuts import render, redirect
from .models import Proceso
from .forms import ProcesoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def crear_protocolo_proceso(request):
    titulo="Crear Protocolos de Proceso"
    protocolo_proceso=Proceso.objects.all()
   
    if request.method == "POST":
        form = ProcesoForm(request.POST or None)
       
        if form.is_valid():
            form.save()

            messages.success(request, "Protocolo creado satisfactoriamente")
            return redirect("crear_protocolo_proceso")
        else:
             messages.error(request, "Por favor revisa los datos ingresados")
             #return redirect("crear_protocolo_metodos")
    else:
            
        form = ProcesoForm() 
    context={
        "titulo":titulo,
        "form":form,
        "protocolo_proceso":protocolo_proceso
    }
    return render(request, "protocolo_proceso/crear_protocolo_proceso.html", context)
