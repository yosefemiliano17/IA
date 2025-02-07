class Nodo: 

    def __init__(self, dato):
        self.dato = dato
        self.nodo_derecho = None
        self.nodo_izquierdo = None

class Arbol: 

    def __init__(self):
        self.raiz = None; 

    def buscarNodo(self, dato):
        nodo_auxiliar = self.raiz
        while nodo_auxiliar is not None: 
            if dato == nodo_auxiliar.dato: 
                return nodo_auxiliar
            if dato < nodo_auxiliar.dato: 
                nodo_auxiliar = nodo_auxiliar.nodo_izquierdo
            if dato > nodo_auxiliar.dato: 
                nodo_auxiliar = nodo_auxiliar.nodo_derecho
        return None


    def vacio(self): 
        return self.raiz is None

    def insertar(self, dato):
        if(self.vacio()): 
            self.raiz = Nodo(dato)
            return
        nodo_auxiliar = self.raiz
        while True: 
            if dato < nodo_auxiliar.dato:
                 if nodo_auxiliar.nodo_izquierdo is None: 
                     nodo_auxiliar.nodo_izquierdo = Nodo(dato)
                     return
                 else: 
                     nodo_auxiliar = nodo_auxiliar.nodo_izquierdo
            if dato > nodo_auxiliar.dato: 
                if nodo_auxiliar.nodo_derecho is None: 
                    nodo_auxiliar.nodo_derecho = Nodo(dato)
                    return
                else: 
                    nodo_auxiliar = nodo_auxiliar.nodo_derecho
        
    def imprimirArbol(self, nodo_actual):
        if nodo_actual is None: 
            return
        self.imprimirArbol(nodo_actual.nodo_izquierdo)
        print(nodo_actual.dato, end=" ")
        self.imprimirArbol(nodo_actual.nodo_derecho)


        
arbol = Arbol()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)

print("Recorrido inorden del árbol:")
arbol.imprimirArbol(arbol.raiz)