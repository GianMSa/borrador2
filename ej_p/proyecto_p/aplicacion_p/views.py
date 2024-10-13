from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def ficha_lista(request):
    return render(request,"ficha_lista.html")

def servicio_lista(request):
    return render(request, "servicio_lista.html")
