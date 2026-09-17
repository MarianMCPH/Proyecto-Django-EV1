from django.shortcuts import render

def vista_integrantes(request):
    return render(request, 'integrantes.html')

def vista_premios(request):
    return render(request, 'premios.html')