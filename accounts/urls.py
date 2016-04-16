from django.conf.urls import url
from django.contrib.auth.views import login, logout
from accounts import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', login, {
        'template_name': 'accounts/login.html'
    }, name='login'),
    url(r'^sair/$', logout, {
        'next_page': 'core:home'
    }, name='logout'),

    url(r'^registrar/$', views.register, name='register'),
    url(r'^editar/$', views.edit, name='edit'),
]
