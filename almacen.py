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

# Ejemplo de uso
almacen = Almacen()
almacen.agregar_producto(1, 'Producto1', 'Descripción del producto 1', 10, datetime.now())
almacen.agregar_producto(2, 'Producto2', 'Descripción del producto 2', 15, datetime.now())

almacen.mostrar_inventario()

almacen.modificar_producto(1, nombre='NuevoNombre', cantidad=20)

print(almacen.obtener_producto(1))
