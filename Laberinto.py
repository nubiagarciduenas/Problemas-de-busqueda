from simpleai.search import SearchProblem, astar
from math import sqrt

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print("".join(fila))

laberinto = [
    list("++++++++++++++++++++++"),
    list("+ O +   ++ ++        +"),
    list("+     +     +++++++ ++"),
    list("+ +    ++  ++++ +++ ++"),
    list("+ +   + + ++         +"),
    list("+          ++  ++  + +"),
    list("+++++ + +      ++  + +"),
    list("+++++ +++  + +  ++   +"),
    list("+          + +  + +  +"),
    list("+++++ +  + + +     X +"),
    list("++++++++++++++++++++++")
]


imprimir_laberinto(laberinto)

class LaberintoAStar(SearchProblem):
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        self.inicio = None
        self.objetivo = None
        
        for i in range(self.filas):
            for j in range(self.columnas):
                if laberinto[i][j] == 'O':
                    self.inicio = (i, j)
                elif laberinto[i][j] == 'X':
                    self.objetivo = (i, j)

        if self.inicio is None or self.objetivo is None:
            raise ValueError("El laberinto debe contener un punto de inicio 'O' y un objetivo 'X'.")

        super().__init__(initial_state=self.inicio)

    def actions(self, state):
        """Devuelve las acciones posibles desde la posición actual (arriba, abajo, izquierda, derecha)."""
        acciones = []
        fila, columna = state
        movimientos = [
            ("arriba", (-1, 0)), 
            ("abajo", (1, 0)), 
            ("izquierda", (0, -1)), 
            ("derecha", (0, 1))
        ]

        for direccion, (df, dc) in movimientos:
            fila_nueva, columna_nueva = fila + df, columna + dc

            if 0 <= fila_nueva < self.filas and 0 <= columna_nueva < self.columnas:
                if self.laberinto[fila_nueva][columna_nueva] != '+':
                    acciones.append((direccion, (fila_nueva, columna_nueva)))

        return acciones
    
    def result(self, state, action):
        """Devuelve el nuevo estado después de aplicar una acción."""
        return action[1]  # Devuelve la nueva posición

    def is_goal(self, state):
        """Verifica si el estado actual es el objetivo."""
        return state == self.objetivo

    def heuristic(self, state):
        """Función heurística: distancia euclidiana al objetivo."""
        fila, columna = state
        fila_objetivo, columna_objetivo = self.objetivo
        return sqrt((fila - fila_objetivo) ** 2 + (columna - columna_objetivo) ** 2)

# Resolver el laberinto con A*
problema = LaberintoAStar(laberinto)
resultado = astar(problema, graph_search=True)

if resultado is None:
    print("No se encontró una solución.")
else:
    print("\nSolución encontrada:")
    for i, (accion, estado) in enumerate(resultado.path()):
        if accion is None:
            print(f"Estado inicial: {estado}")
        elif i == len(resultado.path()) - 1:
            print(f"Después de moverse {accion}, ¡meta alcanzada! {estado} en {i} movimientos")
        else:
            print(f"Después de moverse {accion}, nuevo estado: {estado}")
