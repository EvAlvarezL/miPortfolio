from django.urls import path
from portfolioApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('habilidades/', views.habilidades, name="habilidades"),
    path('proyectos/', views.proyectos, name="proyectos"),
    path('recorrido/', views.recorrido, name="recorrido"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)