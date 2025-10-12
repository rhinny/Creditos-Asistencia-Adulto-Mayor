from django.urls import path
from . import views

urlpatterns = [path('login/estudiante', views.login_estudiante, name='login_estudiante'),
               path('login/adultoM', views.login_adultoM, name='login_adultoM'),
               path('', views.home, name='home')]
