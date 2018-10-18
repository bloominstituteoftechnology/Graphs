"""
Simple graph implementation compatible with BokehGraph class.
"""

class Graph:
    def __init__(self):
        self.vertices = {}
        self.id = -1
        self.answer = []
    def createID(self):
        self.id += 1
        return self.id
    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = Vertex(name, self.createID())
        else:
            print("that vertex already exists")

    def depth_first(self, start, firstrun=True):
        if firstrun == True:
            self.answer = []
        self.answer.append(start.name)
        if start.edges:
            for edge in start.edges:
                if edge not in self.answer:
                    self.depth_first(self.vertices[edge], False)
            return self.answer

    def breadth_first(self, start):
        queue = []
        def helper(start, firstrun=True):
            if firstrun == True:
                self.answer = []
            if len(queue) > 0:
                del queue[0]
            self.answer.append(start.name)
            if start.edges:
                for edge in start.edges:
                    print(edge)
                    if edge not in self.answer:
                        queue.append(edge)
            if len(queue) > 0:
                print(queue)
                helper(self.vertices[queue[0]], False)
        helper(start)
        return self.answer



class Vertex:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.edges = []
    def __repr__(self):
        return f"ID: {self.id}, Edges: {self.edges}, Name: {self.name}\n"
    def add_edge(self, destination):
        if destination not in self.edges:
            self.edges.append(destination)
        else:
            print("that edge already exists")


boop = Graph()
boop.add_vertex(3)
boop.vertices[3].add_edge(3)
boop.add_vertex(1)
boop.vertices[1].add_edge(2)
boop.add_vertex(2)
boop.vertices[2].add_edge(0)
boop.vertices[2].add_edge(3)
boop.add_vertex(0)
boop.vertices[0].add_edge(2)
boop.vertices[0].add_edge(1)

print(boop.breadth_first(boop.vertices[2]))
