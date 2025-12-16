#   8-puzzle solver using the A* algorithm

from simpleai.search import astar, SearchProblem
import random

def find_empty_space(board): #Finds the 2D location of the empty space in a board.        
    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == 0:
                return i, j
    return -1,-1

def find_number(board, num): #Finds the 2d location of the specifies number in a board

    for i, row in enumerate(board):
        for j, item in enumerate(row):
            if item == num:
                return i, j
    return -1,-1


def random_movements(board, n): #Returns a new board after perfprming n random movements on the specifies board.
    new_board = [list(r) for r in board]
    e_row, e_col = find_empty_space(new_board)
    board_size = len(new_board)    

    for i in range(n):
        mov_ok = False
        while not mov_ok:
            mov = random.randint(1,4)
            if mov == 1 and e_row > 0:
                new_board[e_row][e_col], new_board[e_row-1][e_col] = new_board[e_row-1][e_col], new_board[e_row][e_col]
                e_row-=1
                mov_ok = True
            elif mov == 2 and e_row < board_size-1:    
                new_board[e_row][e_col], new_board[e_row+1][e_col] = new_board[e_row+1][e_col], new_board[e_row][e_col]
                e_row+=1
                mov_ok = True
            elif mov == 3 and e_col > 0:
                new_board[e_row][e_col], new_board[e_row][e_col-1] = new_board[e_row][e_col-1], new_board[e_row][e_col]
                e_col-=1
                mov_ok = True
            elif mov == 4 and e_col < board_size-1: 
                new_board[e_row][e_col], new_board[e_row][e_col+1] = new_board[e_row][e_col+1], new_board[e_row][e_col]
                e_col+=1
                mov_ok = True
    return tuple(tuple(row) for row in new_board);

#   Problem definition

class EightPuzzleProblem(SearchProblem):
    
    def __init__(self, initial_state):
        SearchProblem.__init__(self, initial_state)
        # Define goal state.
        self.goal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))        

    def actions(self, state):
        row_empty, col_empty = find_empty_space(state)

        actions = []
        if row_empty > 0:
            actions.append([row_empty - 1, col_empty])
        if row_empty < 2:
            actions.append([row_empty + 1, col_empty])
        if col_empty > 0:
            actions.append([row_empty, col_empty - 1])
        if col_empty < 2:
            actions.append([row_empty, col_empty + 1])

        return actions
        
    def result(self, state, action):
                
        new_board = [list(r) for r in state]

        row_old, col_old = find_empty_space(state)  # Current empty position
        row_new, col_new = action;                  # New empty position

        # Swap values
        new_board[row_old][col_old], new_board[row_new][col_new] = new_board[row_new][col_new], new_board[row_old][col_old]

        return tuple(tuple(row) for row in new_board)
        
    def is_goal(self, state):
        return state == self.goal

    def cost(self, state, action, state2):
        return 1

    def heuristic(self, state):
        distance = 0

        for row_goal, row in enumerate(self.goal):
            for col_goal, item in enumerate(row):

                target_number = self.goal[row_goal][col_goal]
                row_current, col_current = find_number(state, target_number)

                #Heuristic function 1 (Hamming distance)
                # Is the element in the right position?
                distance += int(row_current != row_goal or col_current != col_goal)
                
                #Heuristic function 2 (Mahattan distance)
                # Distance between the goal position and the current position
                #distance += abs(row_current - row_goal) + abs(col_current - col_goal)
   
        return distance



initial_board = random_movements(((0, 1, 2), (3, 4, 5), (6, 7, 8)), 1000)

result = astar(EightPuzzleProblem(initial_board), graph_search=True)

for i, (action, state) in enumerate(result.path()):
    print()
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('After moving', action, 'into the empty space. Goal achieved!')
    else:
        print('After moving', action, 'into the empty space')

    for row in state:
        for item in row:
            print("{:2}".format(item), end = " ")
        print()