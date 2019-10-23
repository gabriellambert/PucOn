from django.conf.urls import url, include
# from simplemooc.accounts.views import index
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path
from novoProjeto.accounts.views import register, dashboard, edit, edit_password, password_reset, password_reset_confirm

# from novoProjeto.accounts.views import edit_password

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('cadastre-se/', register, name='register'),
    path('nova-senha/', password_reset, name='password_reset'),
    #path('confirmar-nova-senha/(?P<key>\w+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^confirmar-nova-senha/(?P<key>[\w_-]+)/$', password_reset_confirm, name='password_reset_confirm'),
    path('sair/', LogoutView.as_view(next_page='core:home'), name='logout'),
    path('', dashboard, name='dashboard'),
    path('editar/', edit, name='edit'),
    path('editar-password/', edit_password, name='edit_password'),

]
