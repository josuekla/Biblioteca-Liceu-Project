from django.urls import path
from . import views

app_name = 'estudante'

urlpatterns = [
    path('', views.estudante, name='estudante' ),
]