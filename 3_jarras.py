#Problema de las 3 jarras
from simpleai.search import SearchProblem, breadth_first

class jarras(SearchProblem):
    def __init__(self):
        SearchProblem.__init__(self,(8,0,0))
        self.capacidades = (8,5,3)
    
    def actions (self,state):
        A,B,C = state
        acciones = []
        
        if A>0:
            if B < self.capacidades[1]: #A->B
                acciones.append(("A","B"))
            if C < self.capacidades[2]: #A->C
                acciones.append(("A","C"))
        
        if B>0:
            if A < self.capacidades[0]: #B->A
                acciones.append(("B","A"))
            if C < self.capacidades[2]: #B->C
                acciones.append(("B","C"))
        
        if C>0:
            if A < self.capacidades[0]: #C->A
                acciones.append(("C","A"))
            if B < self.capacidades[1]: #C->B
                acciones.append(("C","B"))
                
        return acciones
    
    def result(self, state, action):
        A,B,C = state
        origen,destino=action
        capacidades=self.capacidades
        nuevo_estado=list(state)
        
        idx_origen =["A","B","C"].index(origen)
        idx_destino =["A","B","C"].index(destino)
        
        cantidad_transferible=min(nuevo_estado[idx_origen],capacidades[idx_destino] - nuevo_estado[idx_destino])
        
        nuevo_estado[idx_origen]-=cantidad_transferible
        nuevo_estado[idx_destino]+=cantidad_transferible
        
        return tuple(nuevo_estado)
    
    def is_goal(self,state):
        return state==(4,4,0)
    
result = breadth_first(jarras())

for i, (action, state) in enumerate(result.path()):
    print()
    if action is None:
        print('Configuración inicial')
    elif i == len(result.path()) - 1:
        print('Después de mover', action, '¡Objetivo alcanzado!')
    else:
        print('Después de mover', action)
    print(state)
    