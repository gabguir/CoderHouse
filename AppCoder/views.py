from django.shortcuts import render
from .models import Familiar,Padre
from django.http import HttpResponse
# Create your views here.

# def familiar(request):

#     nombre = request.POST.get("nombre")
#     apellido = request.POST.get("apellido")
#     # familiar = familiar(nombre=nombre, apellido=apellido)
#     # familiar.save()
#     # familiar=familiar(nombre="curso creado en el ejemplo", apellido="perez")
#     # print("CREANDO familiar")
#     # familiar.save()
    
#     texto=f"Familiar:{familiar}"
#     return HttpResponse(texto)


def Familiar(request):

    return render (request, "templates/familiar.html")

def Padre(request):
    Padre.__str__()
    return render (request,  "padre.html")

def madre(request):
    nombre="Cristina"
    return render (request, "templates/madre.html")

def hijo(request):
    nombre="Matias"
    return render (request, "templates/hijo.html")