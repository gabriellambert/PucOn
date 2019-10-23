from django.conf.urls import url
from django.urls import path
from novoProjeto.core.views import home
from novoProjeto.core.views import contact

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
]