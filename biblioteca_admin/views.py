from django.shortcuts import render

def biblioteca_admin(request):
    print("Admin Funcionando!")


    # context = {
    #     'title' : 'Texto modificado pelo josué'
    # }

    return render(
        request,
        'biblioteca_admin/home.html',
    )
