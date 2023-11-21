from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 
from .models import Inventario, Producto
from django.contrib import messages
inventario = Inventario()

def index(request):
     template = loader.get_template("inventarioapp/index.html")
     return HttpResponse(template.render( {'Periodos': ''}, request))  

def catalogo(request):
     template = loader.get_template("inventarioapp/catalogo.html")
     inventario.insertar(Producto(1, "Manzana", "Frutas", "Manzana", 100, 10))
     inventario.insertar(Producto(2, "Coca Cola", "Bebidas", "Coca Cola", 100, 10))
     inventario.insertar(Producto(3, "Pepsi", "Bebidas", "Pepsi", 100, 10))
     inventario.insertar(Producto(4, "Sprite", "Bebidas", "Sprite", 100, 10))
     inventario.insertar(Producto(5, "Fanta", "Bebidas", "Fanta", 100, 10))
     results =inventario.obtener_productos()
     return HttpResponse(template.render( {'Productos': results}, request))    
  
def nuevo_producto(request):
    context = {"dummy": 'dummy'}
    return render(request, "inventarioapp/nuevo_producto.html", context)

def crear_producto(request):
     if request.method=="POST":
          p=Producto(int(request.POST.get('codigo')),
                     request.POST.get('nombre'),
                     request.POST.get('categoria'),
                     request.POST.get('marca'),
                     int(request.POST.get('stock')),
                     int(request.POST.get('min_stock')))

          inventario.insertar(p)
          messages.success(request, "se creo el nuevo proceso")
          template = loader.get_template("inventarioapp/catalogo.html")
          results =inventario.obtener_productos()
          return HttpResponse(template.render( {'Productos': results}, request))      

