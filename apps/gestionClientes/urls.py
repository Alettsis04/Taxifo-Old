from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gestion'),
    path('crearAgente', views.crearAgente, name='crear_agente'),
    path('modificarAgente/<int:agente_id>/', views.modificarAgente, name='modificar_agente'),
    path('eliminarAgente/<int:agente_id>/', views.eliminarAgente, name='eliminar_agente'),

    path('barrios', views.indexBarrio, name='barrios'),
    path('crearBarrio', views.crearBarrio, name='crear_barrio'),
    path('modificarBarrio/<int:barrio_id>/', views.modificarBarrio, name='modificar_barrio'),
    path('eliminarBarrio/<int:barrio_id>/', views.eliminarBarrio, name='eliminar_barrio'),

    path('crearCliente/<int:barrio_id>/', views.crearCliente, name='crear_cliente'),
    path('modificarCliente/<int:cliente_id>/', views.modificarCliente, name='modificar_cliente'),
    path('eliminarCliente/<int:cliente_id>/', views.eliminarCliente, name='eliminar_cliente'),

    path('chofer', views.indexChofer, name='chofer'),

    #path('cuentas/<int:cedula>/', views.listarCuentas, name="cuentas"),
    #path('crearCuentas/<int:cedula>/', views.crearCuenta, name='crear_cuentas'),
    #path('modificarCuenta/<int:numero>/<int:cedula>/', views.modificarCuenta, name='modificar_cuenta'),
    #path('eliminarCuenta/<int:numero>/<int:cedula>/', views.eliminarCuenta, name='eliminar_cuenta'),
]

