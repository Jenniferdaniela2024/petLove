from django.urls import path 
from . import views 


#el nombre de views.nombre debe coincidir con la funcion que creamos en views
urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('Clientes/', views.Clientes, name='Clientes'),
    path('Clientes/crear', views.crear, name='crear'),
    path('Clientes/editar', views.editar, name='editar'),
    path('eliminar/<int:identificacion_cliente>', views.eliminar, name='eliminar'),
    path('Clientes/editar/<int:identificacion_cliente>', views.editar, name='editar'),
    path('Mascotas/', views.Mascotas, name='Mascotas'), 
]

