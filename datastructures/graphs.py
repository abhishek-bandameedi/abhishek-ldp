# A graph is a collection of nodes (vertices) and edges connecting pairs of nodes.

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def display(self):
        print("Nodes:", self.nodes)
        print("Edges:", self.edges)

# Using the graph
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.display()
