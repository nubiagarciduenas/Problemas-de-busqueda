import time
import random
import math

class Board(object):
    
    def __init__(self, n, randomize = True):        
        self.n = n
        self.queens = []
        if (randomize):
            # Initialize randomly the board
            for q in range(n):
                empty_space = False
                while not empty_space:
                    row = random.choice(range(n))
                    col = random.choice(range(n))
                    if not [row, col] in self.queens:
                        empty_space = True;
                self.queens.append([row, col])
        else:
            # Place the queens on the first row
            for q in range(n):
                self.queens.append([0, q])

    def show(self):                     
        for row in range(self.n):
            for col in range(self.n):
                if [row, col] in self.queens:
                    print (' Q ', end = '')
                else:
                    print (' - ', end = '')
            print('')
        print('')
    
    def cost(self):
        c = 0
        for i in range(self.n):
            queen = self.queens[i]
            safe = True
            for j in range(self.n):
                if i == j:
                    continue
                other_queen = self.queens[j]
                if (queen[0] == other_queen[0]):
                    # The queens are on the same row
                    safe = False
                elif (queen[1] == other_queen[1]):
                    # The queens are on the same column
                    safe = False
                elif abs(queen[0]-other_queen[0]) == abs(queen[1]-other_queen[1]):
                    # The queens are on the same diagonal
                    safe = False
            if not safe:
                c += 1
        return c

    def neighbor(self):
        # Copy current board
        new_board = Board(self.n, False)
        for i in range(self.n):
            new_board.queens[i][0] = self.queens[i][0]
            new_board.queens[i][1] = self.queens[i][1]
             
        # Select one empty position randomly
        valid_position = False
        while not valid_position:            
            new_row = random.choice(range(self.n))
            new_col = random.choice(range(self.n))
            
            valid_position = True
            for q in range(self.n):
                if new_board.queens[q][0] == new_row and new_board.queens[q][1] == new_col:
                    valid_position = False
                    break
        
        # Update one queen selected randomly
        queen_index = random.choice(range(self.n))
        new_board.queens[queen_index][0] = new_row
        new_board.queens[queen_index][1] = new_col

        return new_board
    
def random_walk(n, max_steps=10000):
    board = Board(n, True)
    steps = 0
    start_time = time.time()
    while steps < max_steps:
        if board.cost() == 0:
            return True, steps, time.time() - start_time
        board = board.neighbor()
        steps += 1
    return False, steps, time.time() - start_time

def hill_climbing(n, max_steps=10000):
    board = Board(n, True)
    steps = 0
    start_time = time.time()
    while steps < max_steps:
        if board.cost() == 0:
            return True, steps, time.time() - start_time
        neighbor = board.neighbor()
        if neighbor.cost() < board.cost():
            board = neighbor
        steps += 1
    return False, steps, time.time() - start_time

def simulated_annealing(n, max_steps=10000, alpha=0.9995, t0=1):
    board = Board(n, True)
    steps = 0
    t = t0
    start_time = time.time()
    while steps < max_steps and t > 0.005:
        if board.cost() == 0:
            return True, steps, time.time() - start_time
        neighbor = board.neighbor()
        cost_diff = neighbor.cost() - board.cost()
        if cost_diff < 0 or math.exp(-cost_diff / t) >= random.random():
            board = neighbor
        t = t0 * (alpha ** steps)
        steps += 1
    return False, steps, time.time() - start_time

def compare_algorithms(n, runs=10):
    algorithms = {
        "Random Walk": random_walk,
        "Hill Climbing": hill_climbing,
        "Simulated Annealing": simulated_annealing
    }
    results = {}
    
    for name, algo in algorithms.items():
        successes, total_steps, total_time = 0, 0, 0.0
        for _ in range(runs):
            success, steps, exec_time = algo(n)
            if success:
                successes += 1
            total_steps += steps
            total_time += exec_time
        results[name] = {
            "Exito": successes / runs,
            "Paso promedio": total_steps / runs,
            "Tiempo promedio(s)": total_time / runs
        }
    
    for algo, res in results.items():
        print(f"{algo}: Exito = {res['Exito']:.2%}, Paso promedio = {res['Paso promedio']:.2f}, Tiempo promedio(s) = {res['Tiempo promedio(s)']:.4f}s")

random.seed(time.time()*1000)

if __name__ == "__main__":
    board=Board(8,True)
board.show()
compare_algorithms(8)