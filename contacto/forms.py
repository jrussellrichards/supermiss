from django import forms

class FormularioContacto(forms.Form):
    nombres = forms.CharField(label = 'Nombres', required=True)
    apellidos = forms.CharField(label = 'Apellidos', required=True)
    email = forms.EmailField(label="Correo Electrónico", required=True)
    telefono = forms.IntegerField(label="Teléfono Contacto", required=True)
    descripcion = forms.CharField(label="Comentarios", required=True, widget=forms.Textarea)




