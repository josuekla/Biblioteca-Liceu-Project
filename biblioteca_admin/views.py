from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required
def biblioteca_admin(request):
    print("Admin Funcionando!")


    context = {
        'title' : 'Texto modificado pelo josué',
    }

    return render(
        request,
        'biblioteca_admin/home.html',
        context,
    )


