from django.urls import path
from base.views import home, bot, form_consulta

app_name = 'base'
urlpatterns = [
    path('', home, name='home'),
    path('busca/', bot, name='busca'),
    path('consulta/', form_consulta, name='consulta')
]