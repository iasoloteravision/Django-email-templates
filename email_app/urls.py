# email_app/urls.py
from django.urls import path
from .views import enviar_correo

app_name = 'email_app'

urlpatterns = [
    path('enviar-correo/<int:usuario_id>/<int:plantilla_id>/', enviar_correo, name='enviar_correo'),
]
