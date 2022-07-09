from ast import Return
from django.shortcuts import render, redirect

from core.forms import RepuestosForm
from .models import Repuestos






# Create your views here.

def index(request):

    return render(request, 'core/index.html')

def iniciarsesion(request):

    return render(request, 'core/Iniciarsesion.html')

def motor(request):

    return render(request, 'core/motor.html')

def pagos(request):

    return render(request, 'core/Pagos.html')

def suspension(request):

    return render(request, 'core/Suspension.html')

def terminos(request):

    return render(request, 'core/terminos.html')

def contacto(request):
    repuestos= Repuestos.objects.all()

    datos = {
        'repuestos': repuestos,
        'form': RepuestosForm,

    }
    if request.method== 'POST':
        formulario = RepuestosForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados Correctamente"

        


    return render(request, 'core/Contacto.html', datos)

def electrico(request):

    return render(request, 'core/Electrico.html')

def embrague(request):

    return render(request, 'core/Embrague.html')

def frenos(request):

    return render(request, 'core/Frenos.html')

def gruas(request):

    return render(request, 'core/Gruas.html')

def modificarform(request, id):
    repuestos = Repuestos.objects.get(id=id)
    datos = {
        'form': RepuestosForm(instance=repuestos)
    }
    if request.method== 'POST':
        formulario = RepuestosForm(data=request.POST, instance=repuestos)
        formulario.save()
        datos['mensaje'] = "Modificado Correctamente"


    return render(request, 'core/modificarform.html', datos)




def eliminarform(request, id):
    repuestos = Repuestos.objects.get(id=id)
    repuestos.delete()
    return redirect(to="contacto")


