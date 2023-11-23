"""from django.db import models

class Producto():
    def __init__(self, codigo, nombre, categoria,marca,stock,min_stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.stock = stock
        self.min_stock = min_stock
        self.izquierda = None
        self.derecha = None"""


"Pila"
class Producto:
    def __init__(self, Id, nombre, precio):
        self.Id=Id
        self.nombre=nombre
        self.precio=precio


class Pila:
    def __init__(self):"
        self.mLista=[]
        
    def insertar(self, valor):
        self.mLista.append(valor)
    
    def remover(self):
        self.mLista.pop()
    
    def ultimoElemento(self):
        print(self.mLista[-1])
    
    def mostrarPila(self):
        for x in self.mLista:
            print(x)

"cola"
class Producto:
    def __init__(self, Id, nombre, precio):
        self.Id = Id
        self.nombre = nombre
        self.precio = precio


class Pedido(Producto):
    def __init__(self, Id, nombre, precio, nombre_cliente, direccion):
        super().__init__(Id, nombre, precio)
        self.nombre_cliente = nombre_cliente
        self.direccion = direccion
        

class ColaPedidos:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.insert(0, item)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def tamaño(self):
        return len(self.items)

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

"tabla Hash"
class Producto:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        
    def Hash_function(self, value): #Función Hash para calcular los índices
        key = 0 
        for i in range(0, len(value)):
            key += ord(value[i])
        return key % 127

    def Insertar(self, value): #Insertar elementos a la tabla Hash
        hash = self.Hash_function(value)
        if self.table[hash] is None:
            self.table[hash] = value
            
    def Buscar(self, value): #Buscar un valor en la tabla Hash
        hash = self.Hash_function(value)
        if self.table[hash] is None:
            return None
        else:
            print(hex(id(self.table[hash]))) 
        
    def Eliminar(self, value): #Eliminar un elemento de la tabla Hash
        hash = self.Hash_function(value)
        if self.table[hash] is None:
            print("No hay elementos con el valor", value)
        else:
            print("El elemento con el valor", value, "ha sido eliminado")
            self.table[hash] is None
            
    def Mostrar_Todos(self): #Mostrar todos los elementos de la Tabla Hash
        for i in range(len(self.table)):
            if self.table[i] is not None:
                print(hex(id(self.table[i])), self.table[i])


"lista"
class Proveedor:
    def __init__(self, numero, id_producto):
        self.numero = numero
        self.id_producto = id_producto

proveedor1 = Proveedor(numero=1, id_producto=101)
proveedor2 = Proveedor(numero=2, id_producto=102)

lista_proveedores = [proveedor1, proveedor2]

for proveedor in lista_proveedores:
    print(f"Número: {proveedor.numero}, ID del Producto: {proveedor.id_producto}")


"almacen"
from datetime import datetime

class Almacen:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, codigo, nombre, descripcion, cantidad, fecha_llegada):
        if codigo not in self.inventario:
            self.inventario[codigo] = {
                'nombre': nombre,
                'descripcion': descripcion,
                'cantidad': cantidad,
                'fecha_llegada': fecha_llegada
            }
            print(f"Producto con código {codigo} agregado al inventario.")
        else:
            print(f"Ya existe un producto con el código {codigo} en el inventario. Use el método modificar_producto para actualizar la información.")

    def modificar_producto(self, codigo, nombre=None, descripcion=None, cantidad=None, fecha_llegada=None):
        if codigo in self.inventario:
            if nombre is not None:
                self.inventario[codigo]['nombre'] = nombre
            if descripcion is not None:
                self.inventario[codigo]['descripcion'] = descripcion
            if cantidad is not None:
                self.inventario[codigo]['cantidad'] = cantidad
            if fecha_llegada is not None:
                self.inventario[codigo]['fecha_llegada'] = fecha_llegada
            print(f"Producto con código {codigo} modificado.")
        else:
            print(f"No hay ningún producto con el código {codigo} en el inventario. Use el método agregar_producto para añadirlo.")

    def obtener_producto(self, codigo):
        if codigo in self.inventario:
            return self.inventario[codigo]
        else:
            print(f"No hay ningún producto con el código {codigo} en el inventario.")

    def mostrar_inventario(self):
        print("Inventario:")
        for codigo, producto in self.inventario.items():
            print(f"Código: {codigo}")
            for clave, valor in producto.items():
                print(f"{clave.capitalize()}: {valor}")
            print("=" * 20)


almacen = Almacen()
almacen.agregar_producto(1, 'Producto1', 'Descripción del producto 1', 10, datetime.now())
almacen.agregar_producto(2, 'Producto2', 'Descripción del producto 2', 15, datetime.now())

almacen.mostrar_inventario()

almacen.modificar_producto(1, nombre='NuevoNombre', cantidad=20)

print(almacen.obtener_producto(1))

"Arbol"
class Nodo:
    def _init_(self, dato):
        self.dato=dato
        self.arbol=["comida", "verdura", "fruta"]
        self.baseV=["verdura"]#Añadir id de cada verdura
        self.baseF=["fruta"]#Añadir id de cada fruta
      
    def insertar(self, raiz, padre, nodo):
        if raiz.dato==padre:
            raiz.arbol.append(nodo)
        else:
            l=len(raiz.arbol)
            for i in range(l):
                if raiz.arbol[i].dato==padre:
                    insertar(raiz.arbol[i], padre, nodo)
                else:
                    insertar(raiz.arbol[i], padre, nodo)


"""class Inventario:
    def __init__(self):
        self.raiz = None

    def insertar(self, producto):
        self.raiz = self._insertar_recursivo(self.raiz, producto)

    def _insertar_recursivo(self, nodo, producto):
        if nodo is None:
            return Producto(producto.codigo, producto.nombre, producto.categoria,producto.marca,producto.stock,producto.min_stock)

        if producto.codigo < nodo.codigo:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, producto)
        elif producto.codigo > nodo.codigo:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, producto)
        #else:
            # Actualizar la cantidad si el producto ya existe
            #nodo.nombre = producto.nombre

        return nodo

    def buscar(self, codigo):
        return self._buscar_recursivo(self.raiz, codigo)

    def _buscar_recursivo(self, nodo, codigo):
        if nodo is None or nodo.codigo == codigo:
            return nodo
        if codigo < nodo.codigo:
            return self._buscar_recursivo(nodo.izquierda, codigo)
        return self._buscar_recursivo(nodo.derecha, codigo)
 
    
    def obtener_productos(self):
        productos = []
        self._obtener_productos_recursivo(self.raiz, productos)
        return productos

    def _obtener_productos_recursivo(self, nodo, lista_productos):
        if nodo is not None:
            # Recorrer el subárbol izquierdo
            self._obtener_productos_recursivo(nodo.izquierda, lista_productos)
            
            # Agregar el producto actual a la lista
            lista_productos.append({
                "codigo": nodo.codigo,
                "nombre": nodo.nombre,
                "categoria": nodo.categoria,
                "marca": nodo.marca,
                "stock": nodo.stock,
                "min_stock": nodo.min_stock
            })

            # Recorrer el subárbol derecho
            self._obtener_productos_recursivo(nodo.derecha, lista_productos)"""
