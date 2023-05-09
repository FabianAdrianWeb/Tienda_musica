from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import include
from .forms import MyAuthForm

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto', views.contacto, name='contacto'),
    path('productos', views.productos, name='productos'),
    path('top10', views.api, name='top10'),
    path('login', LoginView.as_view(template_name='paginas/login.html', authentication_form=MyAuthForm,redirect_authenticated_user=True), name='login'),
    path('logout', LogoutView.as_view(template_name='index.html'), name='logout'),
    path('registro', views.registro, name='registro'),

    
]