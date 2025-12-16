from simpleai.search import SearchProblem, breadth_first

GOAL=5

class Contar(SearchProblem):
    def __init__(self):
        estado_inicial=0
        SearchProblem.__init__(self,estado_inicial)
    
    def actions (self,state):
        acciones=[]
        
        if state<GOAL:
            acciones.append("sumar 1")
            
        return acciones
    
    def result (self, state, action):
        if action=="sumar 1":
            return state + 1
        return state
    
    def is_goal (self, state):
        return state==GOAL
    
resultado = breadth_first(Contar())

for i, (accion, estado) in enumerate(resultado.path()):
    if accion is None:
        print(f"Estado inicial: {estado}")
    elif i == len(resultado.path()) - 1:
        print(f"Después de '{accion}': {estado} → ¡Objetivo alcanzado!")
    else:
        print(f"Después de '{accion}': {estado}")