from django.shortcuts import render 
from django.http import HttpResponse
from datetime import date

def hola(request):
        return render(request, 'inicio.html')
    
def acercade(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def privacidad (request):
    return render(request, 'pdp.html')

def reserva (request):
    hoy = date.today().isoformat()
    return render(request, 'reserva.html',{'hoy': hoy})
def contacto (request):
 return render(request, 'contacto.html')  

def comingsoon(request):
    return render(request, 'coming_soon.html')
    