from django.urls import path, re_path
from django.shortcuts import redirect
from . import views
urlpatterns = [
    #path('', views.hola),
    #path('about/',views.acercade),
    #path('polityka-prywatnosci/',views.privacidad),
    #path('menu/',views.menu),
    #path('kontakt/',views.contacto),
    #path('rezerwacje/',views.reserva, name='reserva'),
    #path('o-klubie/',views.acercade),
    path('coming-soon/', views.comingsoon, name='coming_soon'),
    re_path(r'^.*$', lambda request: redirect('coming_soon')),


]