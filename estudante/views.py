from django.shortcuts import render

def home(request):
    context = {
        'title': 'estudante'
    }
    return render(request,
                 'estudante/home.index',
                  context )


