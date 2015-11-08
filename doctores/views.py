from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return render(request, 'home.html', {
        'nuevo_doctor': request.POST.get('nombre_doc', ''),
    })
    """if(request.method == 'POST'):
        return HttpResponse(request.POST['nombre_doctor'])
    return render(request, 'home.html')"""
