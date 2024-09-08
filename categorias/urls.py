from django.urls import path
from . import views

urlpatterns = [
    path('/<str:nome>/', views.categoria_view, name='categoria'),
]
