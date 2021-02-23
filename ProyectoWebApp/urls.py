from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  
    path('',views.inicio, name="Inicio"),
    path('escuela',views.escuela, name="Escuela"),
    path('postulaciones',views.postulaciones, name="Postulaciones"),
    path('tienda',views.tienda, name="Tienda"),
    path('certamenes',views.certamenes, name="Certamenes")





]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
