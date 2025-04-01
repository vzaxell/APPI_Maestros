from django.urls import path
from .views import index, eliminar_maestro
from .views import mapa_view

app_name = 'maestros'

urlpatterns = [
    path('', index, name='index'),
    path('eliminar/<int:maestro_id>/', eliminar_maestro, name='eliminar_maestro'),
    path('mapa/', mapa_view, name='mapa'),
]

