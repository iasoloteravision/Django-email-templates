# email_app/models.py
from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} (ID: {self.id})"


class PlantillaCorreo(models.Model):
    asunto = models.CharField(max_length=255)
    cuerpo = models.TextField()

    def __str__(self):
        return f"{self.asunto} (ID: {self.id})"


class EnvioCorreo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    plantilla = models.ForeignKey(PlantillaCorreo, on_delete=models.CASCADE)
    enviado_en = models.DateTimeField(auto_now_add=True)
    intentos_fallidos = models.IntegerField(default=0)

    def __str__(self):
        return f"Envío a {self.usuario} - Intentos fallidos: {self.intentos_fallidos}"
