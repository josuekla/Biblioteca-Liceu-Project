from django.shortcuts import render

def categoria_view(request, nome):
    return render(request, f'pages_categorias/html/{nome}.html')
