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

# Uso de la ColaPedidos

cola = ColaPedidos()

# Añadiendo pedidos a la cola
cola.encolar(Pedido(1, "Producto 1", 100, "Cliente 1", "Dirección 1"))
cola.encolar(Pedido(2, "Producto 2", 200, "Cliente 2", "Dirección 2"))

# Ver el frente de la cola
pedido_frente = cola.ver_frente()
print(f"Pedido en frente: {pedido_frente.nombre}")

# Desencolando un pedido
pedido_desencolado = cola.desencolar()
print(f"Pedido desencolado: {pedido_desencolado.nombre}")

# Tamaño de la cola
print(f"Tamaño de la cola: {cola.tamano()}")
