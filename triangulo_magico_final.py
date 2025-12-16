from simpleai.search import SearchProblem, depth_first, breadth_first

class TrianguloMagico(SearchProblem):
    #        A
    #       / \
    #      B   F
    #     /     \
    #    C---D---E

    def __init__(self):
        
        
        SearchProblem.__init__(self, (0,0,0,0,0,0))
        
    def actions(self, state):
        
        act = []
        next_num = max(state)+1
        
        for i in range(len(state)):
            if state[i] == 0:
                act.append((i, next_num))
                                   
        return act
    
    def result(self, state, action):
        
        new_state = list(state)
        new_state[action[0]] = action[1]
        return tuple(new_state)
    
    def is_goal(self, state):
        if 0 in state:
            return False
        
        if state[0] + state[1] + state[2] != 10:
            return False
        if state[2] + state[3] + state[4] != 10:
            return False
        if state[0] + state[4] + state[5] != 10:
            return False        
        return True    
    
result = depth_first(TrianguloMagico(), graph_search=True, viewer=None)

result1 = breadth_first(TrianguloMagico(), graph_search=True)


if result1 is None:
    print("No se encontró una solución.")
else:
    for i, (action, state) in enumerate(result1.path()):
        if action is None:
            print("Initial configuration:", state)
        elif i == len(result1.path()) - 1:
            print(f"After moving {action}, Goal achieved! {state} with {i} steps an using breadth_first")
        else:
            print(f"After moving {action}, new state: {state}")
    

    
if result is None:
    print("No se encontró una solución.")
else:
    for i, (action, state) in enumerate(result.path()):
        if action is None:
            print("Initial configuration:", state)
        elif i == len(result.path()) - 1:
            print(f"After moving {action}, Goal achieved! {state} with {i} steps an using depth_first")
        else:
            print(f"After moving {action}, new state: {state}")
