from django.shortcuts import render, HttpResponse


# Create your views here.
def inicio(request):

    return render(request, "ProyectoWebApp/inicio.html")





def certamenes(request):

    return render(request, "ProyectoWebApp/certamenes.html")


def escuela(request):

    return render(request, "ProyectoWebApp/escuela.html")


def tienda(request):

    return render(request, "ProyectoWebApp/tienda.html")





def postulaciones(request):

    return render(request, "ProyectoWebApp/postulaciones.html")
