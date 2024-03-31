from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import register


# Create your views here.
def index(request):
    return render(request, "index.html")

def registro(request):
    if request.method == "POST":
        if "nameUser" in request.POST and "password" in request.POST:
            user = request.POST["nameUser"]
            password = request.POST["password"]
            objeto = register(user=user, password=password)
            objeto.save()
            print(f"-----------------------------------\n{user} - {password}")
            return redirect('https://edwinjsa.github.io/Dedicatoria/dedicatoria.html')
        else:
            return render(request, "index.html")
    return HttpResponse("No se realizó el método POST")
    
    
    