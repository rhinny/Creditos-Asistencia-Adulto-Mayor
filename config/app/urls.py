from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [#path('registro/estudiante', views.registro_estudiante, name='registro_estudiante'),
               #path('registro/adultoM', views.registro_adultoM, name='registro_adultoM'),
               path('', views.home, name='home'),
               path('usuarios/registro/', views.registro, name="registro")]
