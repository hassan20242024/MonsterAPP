from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Aplicaciones.Protocolo_Metodos.models import Protocolos
from django.db.models import Count,Q,Sum
import json
import datetime
from django.conf import settings
settings.DATE_FORMAT
from django.template.defaultfilters import date



# Create your views here.

 
        


def inicio(request):
    context={
    }
    return render(request, "index-admin.html", context)

@login_required
def inicioAdmin(request):
  

    
     return render(request, "index-admin.html")


@login_required
def adm_inicio(request):
     #currentdate = datetime.datetime.now()
     registro_total_protocolo_metodos = Protocolos.objects.count()
     dataset = Protocolos.objects \
       .values('fecha_final__month')\
        .annotate(Finalizado=Count('fecha_final__month', filter=Q(estado_protocolo="6", fecha_final__year=2024)),
                 ) \
#extra(select={'month': 'DATE_FORMAT(date, '%B')'})
        #.order_by('-fecha_final__month')
   #fecha = datetime.datetime.strptime(dataset, "%d/%m/%Y").strftime("%Y-%m-%d")

     #categories = []
     #Finalizado = list()
  
     #for entry in dataset:
        ##Finalizado.append(entry['Finalizado'])
     #Finalizado_series = {
        #'name': 'Finalizado',
        #'data': Finalizado,
        #'colorByPoint': 'True',
        #'showInLegen': 'False',
        
   ###'chart': {'type': 'column' },
        #'title': {'text': ''},
        #'xAxis': [
            #{'categories': categories},
        #],
        #'series': [Finalizado_series],
    #}
     #chart1 = {
        #'chart': {'type': 'line' },
        #'title': {'text': ''},
        #'xAxis': {'categories': categories},
        #'series': [Finalizado_series]
    #}

     #dump = json.dumps(chart)
     #dump1 = json.dumps(chart1)

     dataset_motivo = Protocolos.objects.values("estado_protocolo__estado_motivo").annotate(
         Listado=Count("estado_protocolo", filter=Q(estado_protocolo="5")),
         finalizado=Count("estado_protocolo", filter=Q(estado_protocolo="6")),
         falta_insumos=Count("estado_protocolo__estado_motivo", filter=Q(estado_protocolo="2")),
         metodologia=Count("estado_protocolo__estado_motivo", filter=Q(estado_protocolo="3")),
         criterio=Count("estado_protocolo__estado_motivo", filter=Q(estado_protocolo="4")),
         ejecucion=Count("estado_protocolo", filter=Q(estado_protocolo="1"))
     )

     categories = []
     Listado = list()
     finalizado = list()
     falta_insumos = list()
     metodologia = list()
     criterio = list()
     ejecucion = list()
     for entry in dataset_motivo:
         categories.append('%s ' % entry['estado_protocolo__estado_motivo'])
         Listado.append(entry['Listado'])
         finalizado.append(entry['finalizado'])
         falta_insumos.append(entry['falta_insumos'])
         metodologia.append(entry['metodologia'])
         criterio.append(entry['criterio'])
         ejecucion.append(entry['ejecucion'])
     listadoseries = {
        'name': 'Listado',
        'data': Listado,
        'color': '#08ee97', 
   } 
     finalizado_series = {
        'name': 'Finalizado',
        'data': finalizado,
        'color': '#0855ee', 
   } 

     falta_insumos_series = {
        'name': 'Falta de insumos',
        'data': falta_insumos,
        'color': '#11d0d2',
    } 
     metodologia_series = {
        'name': 'Problemas de método',
        'data': metodologia,
        'color': '#ee5f08',
    } 
     criterio_series = {
        'name': 'Muestras no cumplen parámetros',
        'data': criterio,
        'color': '#ff0d0d',
    } 
     ejecucion_series = {
        'name': 'En ejecución',
        'data': ejecucion,
        'color': '#db08ee',
    } 
     chart2 = {
        'chart': {'type': 'bar'},
        'title': {'text': ''},
        'xAxis': {'categories': categories},
        'series': [falta_insumos_series,finalizado_series,metodologia_series,criterio_series,listadoseries,ejecucion_series]
    } 
     dump2 = json.dumps(chart2)   
     titulo="Tablero principal"
     context={
        "titulo":titulo,
       # 'chart': dump,
        #'chart1': dump1,
        "dataset":dataset,
        #"Finalizado":Finalizado,
        'chart2': dump2,
        "registro_total_protocolo_metodos":registro_total_protocolo_metodos

    }
     return render(request, "inicio.html", context)

