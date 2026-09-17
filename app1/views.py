from django.shortcuts import render

def vista_albumes(request):
    return render(request, 'app1/albumes.html')

def vista_canciones(request):
    return render(request, 'app1/canciones.html')