from django.shortcuts import render, redirect
from doctores.models import Doctor


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    doctores = Doctor.objects.all()
    return render(request, 'list.html', {'doctores': doctores})


def nuevo_doctor(request):
    Doctor.objects.create(nombre=request.POST['nombre_doc'])
    return redirect('/lists/la-unica-lista-en-el-mundo/')
