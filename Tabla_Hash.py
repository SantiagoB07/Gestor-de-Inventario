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
