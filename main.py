import graph
import utilities
import time
import random

def is_solvable(g, path=[], depth=0, known_false={}):
    if utilities.colors_to_string(g) in known_false:
        return path, False, known_false
    
    s = g.size
    if s - list(g.colors.values()).count(0) == 1:
        return path, True, known_false
    
    possible_moves = []
    for node in g.graph:
        if g.colors[node] == 0:
            for neighbor in g.graph[node]:
                if g.colors[neighbor] == 0:
                    continue
                for n2 in g.graph[neighbor]:
                    if g.colors[n2] != 0:
                        possible_moves.append((node, neighbor, n2))
    
    for move in possible_moves:
        c0 = g.colors[move[0]]
        c1 = g.colors[move[1]]
        c2 = g.colors[move[2]]
        g.colors[move[0]] = g.colors[move[2]]
        g.colors[move[1]] = (g.colors[move[2]] + g.colors[move[1]]) % 3
        g.colors[move[2]] = 0
        p, valid, known_false = is_solvable(g, path=(path + [utilities.colors_to_string(g)]), depth=depth+1, known_false=known_false)
        if valid:
            path = p
            return path, True, known_false
        g.colors[move[0]] = c0
        g.colors[move[1]] = c1
        g.colors[move[2]] = c2
    
    known_false[utilities.colors_to_string(g)] = True
    return path, False, known_false

def test_random_cycle(n):
    g = utilities.make_cycle(n)
    g.colors[0] = 0
    for i in range(1, n):
        g.colors[i] = random.randint(1, 2)
    print(utilities.colors_to_string(g))
    path, value, known_false = is_solvable(g, path=[], depth=0)
    if value:
        for p in path:
            print(p)
    else:
        print("No solution")

def all_length_n_cycle(n):
    g = utilities.make_cycle(n)

    known_false = {}

    for i in range(0, 2 ** (n - 2)):
        g.colors[0] = 0
        s = bin(i)[2:]
        while len(s) < n - 1:
            s = "0" + s
        for j in range(1, n):
            g.colors[j] = int(s[j - 1]) + 1
        path, value, known_false = is_solvable(g, path=[], depth=0, known_false=known_false)
        if not value:
            print("No solution")
            print(utilities.colors_to_string(g))
            return False
    
    return True

def test_specific_cycle(n, colors):
    g = utilities.make_cycle(n)
    for i in range(0, n):
        g.colors[i] = colors[i]
    print(utilities.colors_to_string(g))
    path, value, known_false = is_solvable(g, path=[], depth=0)
    if value:
        for p in path:
            print(p)
    else:
        print("No solution")

def test_specific_path(n, colors):
    g = utilities.make_path(n)
    for i in range(0, n):
        g.colors[i] = colors[i]
    print(utilities.colors_to_string(g))
    path, value, known_false = is_solvable(g, path=[], depth=0)
    if value:
        for p in path:
            print(p)
    else:
        print("No solution")

def test_random_path(n):
    g = utilities.make_path(n)
    zero_location = random.randint(0, n - 1)
    g.colors[zero_location] = 0
    for i in range(0, n):
        if i == zero_location:
            continue
        g.colors[i] = random.randint(1, 2)
    print(utilities.colors_to_string(g))
    path, value, known_false = is_solvable(g, path=[], depth=0)
    if value:
        for p in path:
            print(p)
    else:
        print("No solution")
        
def all_length_n_path(n):
    g = utilities.make_path(n)

    known_false = {}

    print("The following have no solution: ")
    count = 0

    for zero_location in range(0, n):
        for i in range(0, 2 ** (n - 2)):
            g.colors[zero_location] = 0
            s = bin(i)[2:]
            while len(s) < n - 1:
                s = "0" + s
            offset = 0
            for j in range(0, n):
                if j == zero_location:
                    offset = 1
                    continue
                g.colors[j] = int(s[j - offset]) + 1
                
            path, value, known_false = is_solvable(g, path=[], depth=0, known_false=known_false)
            if not value:
                count += 1
                print(utilities.colors_to_string(g))
    
    return count

# MAIN FUNCTION HERE
# USAGE: set n to the number of nodes in the cycle
#        set the colors of the nodes in the cycle
#        run the program
if __name__ == "__main__":
    t, t2 = 0, 0

    # change this to the number of nodes in the cycle
    n = 4

    # tests if a random coloring of the cycle is solvable
    # t = time.time()
    # test_random_cycle(n)
    # t2 = time.time()

    # tests if a specific coloring of the cycle is solvable
    # t = time.time()
    # test_specific_path(n, [0, 1, 2, 1, 2, 1, 2])
    # t2 = time.time()

    # tests if the cycle length is fully solvable
    t = time.time()
    print(all_length_n_path(n))
    t2 = time.time()
    
    # outputs the time taken to run the program
    print(f"Time: {t2 - t}")