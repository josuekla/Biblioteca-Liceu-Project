from django.urls import path
from . import views

app_name = 'visitante'


urlpatterns = [
    path('', views.visitante),
    path('home', views.visitante),
    path('categorias', views.visitante),
    path('emprestar', views.visitante),
]