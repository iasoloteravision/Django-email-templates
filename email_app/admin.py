# email_app/admin.py
from django.contrib import admin
from .models import Usuario, PlantillaCorreo, EnvioCorreo

admin.site.register(Usuario)
admin.site.register(PlantillaCorreo)
admin.site.register(EnvioCorreo)
