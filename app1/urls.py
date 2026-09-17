from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('albumes/', views.vista_albumes, name='albumes'),
    path('canciones/', views.vista_canciones, name='canciones'),
]