class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} : {self.adj_list[vertex]}")

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v2 in self.adj_list.keys() and v1 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, v):
        if v in self.adj_list.keys():
            for vertex in self.adj_list[v]:
                self.adj_list[vertex].remove(v)
            del self.adj_list[v]
            return True
        return False

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(3,4)
g.add_edge(2,4)
g.print_graph()
# print(g.remove_edge(2, 3))
print(g.remove_vertex(4))
g.print_graph()
