from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def familia(request):
    familia = Familia(ap="Perez" , nom_padre="Juan", nom_madre="Marta", nom_hijo="Lucas", padres_nac="Arg")
    familia.save()
    data = f" Familia:{familia.ap} Padre:{familia.nom_padre} Madre:{familia.nom_madre} Hijo:{familia.nom_hijo} Nacionalidad: {familia.padres_nac}"
    return render(request, "familia.html", {"data":data})

def padre(request):
    padre = Miembro(nom="Juan", edad=61, ap="Perez", nac="Arg")
    padre.save()
    data = f" Padre:\nNombre: {padre.nom}\nApellido: {padre.ap}\nEdad: {padre.edad}\nFecha de nacimiento: {padre.nac}."
    return render(request, "padre.html", {"data":data})

def madre(request):
    madre = Miembro(nom="Marta", ap="Perez" , nac="Arg", edad=32)
    madre.save()
    data = f" Padre:\nNombre: {madre.nom}\nApellido: {madre.ap}\nEdad: {madre.edad}\nFecha de nacimiento: {madre.nac}."
    return render(request, "madre.html", {"data":data})

def hijo(request):
    hijo = Miembro(nom="Lucas", ap="Perez" , nac="Arg", edad=5)
    hijo.save()
    data = f" Padre:\nNombre: {hijo.nom}\nApellido: {hijo.ap}\nEdad: {hijo.edad}\nFecha de nacimiento: {hijo.nac}."
    return render(request, "hijo.html", {"data":data})