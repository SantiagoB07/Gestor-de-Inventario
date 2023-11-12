class Pedido(Producto):
    def __init__(self, Id, nombre, precio, nombre_cliente, direccion):
        super().__init__(Id, nombre, precio)
        self.nombre_cliente = nombre_cliente
        self.direccion = direccion
