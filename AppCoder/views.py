from django.shortcuts import render
from .models import familiar
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


def familiar(request):

    nom = "Juan"
    ap  = "Perez"
    dic = {"Nombre:nom", "Apellido:ap"}
    return render (request, "templates/familiar.html")

def padre(request):
    nom = "Adolfo"
    ap  = "Perez"
    dic = {"Nombre:nom", "Apellido:ap"}
    micontext = 
    # return render (request, "templates/padre.html")

def madre(request):
    nom = "Marta"
    ap  = "Perez"
    dic = {"Nombre:nom", "Apellido:ap"}
    return render (request, "templates/madre.html")

def hijo(request):
    return render (request, "templates/hijo.html")