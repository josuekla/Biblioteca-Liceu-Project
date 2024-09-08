from django.urls import path
from biblioteca_admin import views


app_name = 'biblioteca_admin'

urlpatterns = [
    path('', views.biblioteca_admin, name='biblioteca_admin'),
]
