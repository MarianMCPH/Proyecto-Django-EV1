from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('integrantes/', views.vista_integrantes, name='integrantes'),
    path('premios/', views.vista_premios, name='premios'),
]