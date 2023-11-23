from django.db import models

class Producto():
    def __init__(self, codigo, nombre, categoria,marca,stock,min_stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.stock = stock
        self.min_stock = min_stock
        self.izquierda = None
        self.derecha = None


"Pila"
"""class Producto:
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
            print(x)"""

"""class Producto:
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
        return self.items[-1]"""





class Inventario:
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
            self._obtener_productos_recursivo(nodo.derecha, lista_productos)
