import graph

def make_cycle(n):
    g = graph.Graph()
    for i in range(n):
        g.add_edge(i, (i + 1) % n)
        g.add_edge((i + 1) % n, i)
    return g

def make_path(n):
    g = graph.Graph()
    for i in range(n - 1):
        g.add_edge(i, i + 1)
        g.add_edge(i + 1, i)
    return g

def colors_to_string(g):
    s = ""
    for node in g.graph:
        s += f"{g.colors[node]} "
    return s

def print_path_colors(g):
    for node in g.graph:
        print(f"{g.colors[node]}", end=" ")
    print()