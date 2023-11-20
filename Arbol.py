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
