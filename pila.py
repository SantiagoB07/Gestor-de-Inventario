class Producto:
    def __init__(self, Id, nombre, precio):
        self.Id=Id
        self.nombre=nombre
        self.precio=precio


class Pila:
    def __init__(self):
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
