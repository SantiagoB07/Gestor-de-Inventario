from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('catalogo/',views.catalogo),
    path('nuevo_producto/',views.nuevo_producto),
    path('nuevo_producto/crear_producto',views.crear_producto),
]