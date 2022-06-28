from django.shortcuts import render, redirect
from CoderApp.models import Planta
from CoderApp.models import Arbol
from CoderApp.models import Cactus
#from CoderApp.forms import CursoFormulario

def inicio(request):
     return render(request,"inicio.html")

def planta(request):
     planta = Planta.objects.all()
     print(planta)
     return render(request,"planta.html",{'planta':planta})

def arbol(request):
     arbol = Arbol.objects.all()
     print(arbol)
     return render(request,"arbol.html",{'arboles':arbol})

def cactus(request):
     cactus = Cactus.objects.all()
     print(cactus)
     return render(request,"cactus.html",{'cactus':cactus})

def registrarArbol(request):
     print(request.POST)
     print('test')
     nombre = request.POST['txtnombre']
     nombreCientifico = request.POST['txtnombreCientifico']
     alturaMax = request.POST['txtalturaMax']

     arbol = Arbol.objects.create(nombre=nombre, nombreCientifico=nombreCientifico, alturaMax=alturaMax)

     return redirect('arbol')

def registrarPlanta(request):
     print(request.POST)
     print('test')
     nombre = request.POST['txtnombre']
     nombreCientifico = request.POST['txtnombreCientifico']
     deInterior = request.POST['txtdeInterior']

     planta = Planta.objects.create(nombre=nombre, nombreCientifico=nombreCientifico, deInterior=deInterior)

     return redirect('planta')

def registrarCactus(request):
     print(request.POST)
     print('test')
     nombre = request.POST['txtnombre']
     nombreCientifico = request.POST['txtnombreCientifico']
     tiempoSinAgua = request.POST['txttiempoSinAgua']

     cactus = Cactus.objects.create(nombre=nombre, nombreCientifico=nombreCientifico, tiempoSinAgua=tiempoSinAgua)

     return redirect('cactus')




