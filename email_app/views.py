# email_app/views.py
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Usuario, PlantillaCorreo, EnvioCorreo


def enviar_correo(request, usuario_id, plantilla_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    plantilla = get_object_or_404(PlantillaCorreo, pk=plantilla_id)

    envio_correo, created = EnvioCorreo.objects.get_or_create(
        usuario=usuario, plantilla=plantilla)

    try:

        send_mail(
            plantilla.asunto,
            plantilla.cuerpo,
            'jjusturi@gmail.com',  # Reemplaza con tu dirección de correo electrónico
            [usuario.correo],
            fail_silently=False,
        )

        # Si el envío es exitoso, reiniciamos el contador de intentos fallidos
        envio_correo.intentos_fallidos = 0
        envio_correo.save()
        mensaje = "Correo enviado con éxito."

    except Exception as e:
        # Si el envío falla, incrementamos el contador de intentos fallidos
        envio_correo.intentos_fallidos += 1
        envio_correo.save()

        # Puedes agregar lógica para enviar una notificación o mensaje
        # por ejemplo, utilizando algún sistema de mensajería o registro de eventos.
        print(f"Fallo al enviar correo a {usuario}: {e}")
        mensaje = f"Error al enviar correo: {e}"

    return render(request, 'email_app/enviado.html', {'usuario': usuario, 'plantilla': plantilla, 'mensaje': mensaje})
