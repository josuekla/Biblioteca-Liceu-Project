from django.shortcuts import render
from django.http import HttpResponse

def visitante(request):
    print("visitante Funcionando!")
    return HttpResponse("test")


