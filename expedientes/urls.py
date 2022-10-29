from django.urls import path
from expedientes.views import clientes

app_name = 'expedientes'
urlpatterns = [
    path('', clientes, name='clientes'),
]