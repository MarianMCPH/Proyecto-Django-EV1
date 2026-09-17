from django.shortcuts import render

def vista_albumes(request):
    return render(request, 'albumes.html')  

def vista_canciones(request):
    return render(request, 'canciones.html')  