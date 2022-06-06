from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('apps.gestionClientes.urls')),
    path('login/', include('apps.login.urls')),
    path('', views.index, name='homepage')
]
