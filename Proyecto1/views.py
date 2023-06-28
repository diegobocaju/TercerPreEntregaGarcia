from django.http import HttpResponse
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def saludo(request):
    mensaje = 'PaRa InGrEsAr a NuEsTrO SiTiO, POR FAVOR sElEcCiOnA  <a href="http://127.0.0.1:8000/AppCoder/inicio/">aquí</a>.'
    return HttpResponse(mensaje)

def segunda_vista(request):
    return HttpResponse("<br><br> <h1>Mi primer proyecto con Django</h1>")

def miNombreEs(request, nombre):
    data = f"Mi nombre es: <h1>{nombre}</h1>"
    return HttpResponse(data)

def probandoTemplate(request):
    nombre = "Diego"
    apellido = "Garcia"

    namelist = ["Diego", "Alumno1", "Alumno2", "Alumno3", "Alumno4"]

    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
