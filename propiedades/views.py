from django.shortcuts import render

# Create your views here.
def prueba(request):
    return render(request, "prueba.html")

def otro(request):
    return render(request,"otro.html")