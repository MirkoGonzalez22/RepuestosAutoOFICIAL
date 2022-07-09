from django.urls import URLPattern, path

from core.models import Repuestos
from .views import index, contacto, iniciarsesion, motor, pagos, suspension, terminos, electrico, embrague, frenos, gruas, modificarform, eliminarform


urlpatterns = [
    path('', index, name="index"),
    path('contacto', contacto, name="contacto"),
    path('iniciarsesion', iniciarsesion, name="iniciarsesion"),
    path('motor', motor, name="Motor"),
    path('pagos', pagos, name="pagos"),
    path('suspension', suspension, name="suspension"),
    path('terminos', terminos, name="terminos"),
    path('electrico', electrico, name="electrico"),
    path('embrague', embrague, name="embrague"),
    path('frenos', frenos, name="frenos"),
    path('gruas', gruas, name="gruas"),
    path('modificarform/<id>', modificarform, name="modificarform"),
    path('eliminarform/<id>', eliminarform, name="eliminarform"),
]