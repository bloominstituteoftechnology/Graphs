
# vertex is just an obnoxiously smart word for node
# peeps need to spend the extra effort blabbering polysyllabic
# words to make themselves feel smarter I guess
# as for me, I stay humble and try to find the smallest 
# and fewest words possible when explaining something
# vertex is two syllables; node is one.
# why work harder than we absolutely have to? just saying...
# okay so now that I understand what's going on in a graph more
# I'll take a stab a breadth first search and then depth first search
# I love Lambda School. I hope we all make it...


class Vertex:
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)


class Graph:
    def __init__(self):
        # this is a dictionary of sets
        # essentially, this is the graph
        self.vertices = {}

    def insert_edge_bi_directional(self, start, end):
        if start not in self.vertices and end not in self.vertices:
            raise ValueError("No entries!")
        else:
            self.vertices[start].add(end)
            self.vertices[end].add(start)

    def insert_edge_uni_directional(self, from_vertex, to_vertex):
        if from_vertex not in self.vertices:
            raise ValueError("from_vertex does not exist!")
        elif to_vertex not in self.vertices:
            raise ValueError("to_vertex does not exist!")
        else:
            self.vertices[from_vertex].add(to_vertex)


    def insert_vertex(self, vertex):
        if vertex not in self.vertices:
            # turning the vertex into a set inside the dictionary
            self.vertices[vertex] = set()
        else:
            raise ValueError("Vertex already exists in set!")

    
my_graph = Graph()


node_one = Vertex('NodeOne')
node_two = Vertex('NodeTwo')
my_graph.insert_vertex(node_one)
my_graph.insert_vertex(node_two)
# my_graph.insert_edge_uni_directional(node_one, node_two)
my_graph.insert_edge_bi_directional(node_one, node_two)
print(my_graph.vertices)




