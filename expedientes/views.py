from django.shortcuts import render


def clientes(request):
    return render(request, 'expedientes/clientes.html')


