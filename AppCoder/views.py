from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def familia(self):

    familia = Familia(ap="Perez" , nom_padre="Juan", nom_madre="Marta", nom_hijo="Lucas", padres_nac="Arg")   
    familia.save() 
    data = f" Familia:{familia.ap} Padre:{familia.nom_padre} Madre:{familia.nom_madre} Hijo:{familia.nom_hijo} Nacionalidad: {familia.padres_nac}"
    
    return HttpResponse(data)
    # return render (request, "familia.html")

def padre(request):

    padre = Padre(nom="Juan", edad="asd", ap="Perez", nac="Arg")   
    padre.save() 
    data = f">>> Nombre:{padre.nom} Apellido:{padre.ap} Edad:{padre.edad}  Nacionalidad: {padre.nac}"
    
    return HttpResponse(data)
    # return render (request, "padre.html")

def madre(request):

    madre = Madre(nom="Marta", ap="Perez" , edad="52" , nac="Arg")   
    madre.save() 
    data = f">>> Nombre:{madre.nom} \\ Apellido:{madre.ap} \\ Edad:{madre.edad}  Nacionalidad: {madre.nac}"
    
    return HttpResponse(data)
    # return render (request, "madre.html")

def hijo(request):

    hijo = Hijo(nom="Lucas", ap="Perez" , edad="14" , nac="Arg")   
    hijo.save() 
    data = f">>> Nombre:{hijo.nom} \\ Apellido:{hijo.ap} \\ Edad:{hijo.edad}  Nacionalidad: {hijo.nac}"
    
    return HttpResponse(data)
    # return render (request, "hijo.html")