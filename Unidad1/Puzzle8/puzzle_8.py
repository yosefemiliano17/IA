import time
from queue import PriorityQueue

class Tablero: 

    def __init__(self,val,distancia,f):
        self.val = tuple(tuple(row) for row in val)
        self.distancia = distancia
        self.f = f
    
    def __lt__(self, other):
        return self.f < other.f

    def __hash__(self):
        return hash(self.val)  
    
    def __eq__(self, other):
        return self.val == other.val  
        
    def buscar_cero(self): 
        for i in range(3): 
            for j in range(3): 
                if self.val[i][j] == 0: 
                    return [i,j]
        return None

    def puedo_mover(self,i,j): 
        if i >= 0 and i < 3 and j >= 0 and j < 3: 
            return True
        return False

    def duplicar(self): 
        temp = []
        for i in self.val:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp  

    def generar_tableros_resultantes(self):
        x = [0,0,1,-1]
        y = [1,-1,0,0]

        resultado = []
        coordenadas = self.buscar_cero()

        for i in range(4):
            if self.puedo_mover(coordenadas[0] + x[i], coordenadas[1] + y[i]): 
                tablero_aux = self.duplicar()
                temporal = tablero_aux[coordenadas[0]][coordenadas[1]]
                tablero_aux[coordenadas[0]][coordenadas[1]] = tablero_aux[coordenadas[0]+x[i]][coordenadas[1]+y[i]]
                tablero_aux[coordenadas[0]+x[i]][coordenadas[1]+y[i]] = temporal
                resultado.append(Tablero(tablero_aux,self.distancia+1,0))

        return resultado


class Puzzle: 

    def __init__(self):
        self.tablero_inicial = None 
        self.tablero_final = None
        self.posiciones_finales = None

    def leer_tablero_inicial(self): 
        self.tablero_inicial = [list(map(int, input().split())) for _ in range(3)]

    def leer_tablero_final(self): 
        self.tablero_final = [list(map(int, input().split())) for _ in range(3)]
    
    def obtener_posiciones(self): 
        posiciones = {}
        for i in range(3):
            for j in range(3):
                posiciones[self.tablero_final[i][j]] = (i,j)
        return posiciones

    def distancia_manhattan(self,x1,y1,x2,y2): 
        return abs(x1-x2) + abs(y1-y2)

    def h(self,tablero_actual): 
        sumatoria = 0
        for i in range(3):
            for j in range(3): 
                if tablero_actual[i][j] != self.tablero_final[i][j] and tablero_actual[i][j] != 0:
                    casilla_final = self.posiciones_finales[tablero_actual[i][j]]
                    sumatoria += self.distancia_manhattan(i,j,casilla_final[0],casilla_final[1])
        return sumatoria

    def reconstruir_camino(self,actual,padres): 
        camino = []
        while actual: 
            camino.append(actual)
            actual = padres.get(actual)
        return reversed(camino)

    def jugar(self): 
        print("---- INGRESA LA CONFIGURACION DEL TABLERO INICIAL ----")
        self.leer_tablero_inicial()
        print("---- INGRESA LA CONFIGURACION DEL TRABLERO FINAL ----")
        self.leer_tablero_final()
        print("\n\n")

        self.posiciones_finales = self.obtener_posiciones()

        inicio = Tablero(self.tablero_inicial,0,0)
        inicio.f = self.h(inicio.val) + inicio.distancia

        pq = PriorityQueue()
        pq.put(inicio)

        distancias = {inicio: 0}
        padres = {inicio: None}

        tiempo_inicio = time.time()

        while not pq.empty(): 
            actual = pq.get()

            if self.h(actual.val) == 0: 
                tiempo_fin = time.time()
                duracion = tiempo_fin - tiempo_inicio
                print("\n¡Solución encontrada!\n")
                camino = list(self.reconstruir_camino(actual, padres))
                paso = 0
                for tablero in camino:
                    print("Movimiento", paso, ":")
                    for fila in tablero.val:
                        print(*fila)
                    print("")
                    paso += 1
                print("CANTIDAD DE MOVIMIENTOS:", paso - 1)
                print(f"Tiempo de ejecución: {duracion:.4f} segundos")
                return True
            
            for i in actual.generar_tableros_resultantes(): 
                i.f = self.h(i.val) + i.distancia
                if i not in distancias or distancias[i] > i.f: 
                    distancias[i] = i.f
                    pq.put(i)
                    padres[i] = actual
        return False

puzzle_8 = Puzzle()

if not puzzle_8.jugar(): 
    print("No hay solucion")
