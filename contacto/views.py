from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage


# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method=="POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombres = request.POST.get("nombres")
            apellidos = request.POST.get("apellidos")
            email = request.POST.get("email")
            telefono = request.POST.get("telefono")
            descripcion = request.POST.get("descripcion")

            email = EmailMessage("Contacto", 
            "El usuario, Nombre: {}, Correo Electrónico {}, indica lo siguiente: \n\n {}".format((nombres + " " + apellidos).upper(), email.upper(), descripcion.upper()),
            "", ["estebangarcescastaneda@gmail.com"], reply_to=[email] )

            try: 
                email.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})
