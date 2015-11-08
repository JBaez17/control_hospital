from django.shortcuts import render, redirect
from doctores.models import Doctor


def home_page(request):
    """doctor = Doctor()
    doctor.nombre = request.POST.get('nombre_doc', '')
    doctor.save()"""

    if request.method == 'POST':
        # nuevo_doctor = request.POST['nombre_doc']
        # Doctor.objects.create(nombre=nuevo_doctor)
        Doctor.objects.create(nombre=request.POST['nombre_doc'])
        return redirect('/')
    # else:
    # nuevo_doctor = ''
    doctores = Doctor.objects.all()

    return render(request, 'home.html', {'doctores': doctores})
