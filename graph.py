class Graph:
    def __init__(self):
        self.graph = {}
        self.colors = {}
        self.size = 0

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set(())
            self.colors[u] = 0
            self.size += 1
        self.graph[u].add(v)

    def delete_edge(self, u, v):
        self.graph[u].remove(v)

    def make_copy(self):
        g = Graph()
        g.graph = self.graph.copy()
        g.colors = self.colors.copy()
        g.size = self.size
        return g

    
    def print_graph(self):
        for node in self.graph:
            print(f'{node} ({self.colors[node]}): {self.graph[node]}')

    def set_color(self, node, color):
        self.colors[node] = color

    def get_neighbors(self, node):
        return self.graph[node]
    
    def get_dist_two(self, node):
        neighbors = self.get_neighbors(node)
        dist_two = set(())
        for neighbor in neighbors:
            dist_two = dist_two.union(self.get_neighbors(neighbor))
        return dist_two
    
    @staticmethod
    def make_from_file(filename):
        g = Graph()
        with open(filename, 'r') as f:
            for line in f:
                u, neighbors = line.split(':')
                for v in neighbors.strip().split(','):
                    g.add_edge(u, v)
                    g.add_edge(v, u)

        return g