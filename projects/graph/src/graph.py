"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = { }

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, vertex_a, vertex_b ):
        if vertex_a in self.vertices.keys() and vertex_b in self.vertices.keys():
            self.vertices[vertex_a].add(vertex_b)
            self.vertices[vertex_b].add(vertex_a)
        else:
            print ("Can't find all vertices")
    def bft(self, start_v = None):
        queue = [start_v] if start_v else [list(self.vertices.keys())[0]]
        if start_v in self.vertices:
            pass
        else:
            raise KeyError('The vertex passed does not exist in the graph')  #error handling

        visited = []

        while queue:
            current = queue[0]
            for v in self.vertices[current]:
                if v not in visited and v not in queue:
                    queue.append(v)
            visited.append(queue.pop(0))
        return  visited

    def bfs(self, element):
        start_v = list(self.vertices.keys())[0]
        queue = [start_v]
        visited = []

        while queue:
            current = queue[0]
            if current == element:
                visited.append(current)
                print ('here')
                print ('path:', visited)
                return True
            for v in self.vertices[current]:
                if v not in visited and v not in queue:
                    queue.append(v)
            visited.append(queue.pop(0))
        print ('path:', visited)
        return False

    def dft(self, start_v = None):
        stack = [start_v] if start_v else [list(self.vertices.keys())[0]]
        if start_v in self.vertices:
            pass
        else:
            raise KeyError('The vertex passed does not exist in the graph')  #error handling

        visited = []

        while stack:
            current = stack[0]
            pre_stack = []
            for v in self.vertices[current]:
                if v not in visited and v not in stack and v not in pre_stack:
                    print ('v:', v)
                    pre_stack.append(v)
                    print ('here pre:', pre_stack)
            print ('Round 1')
            print ('stack:', stack)
            print ('pre_stack:', pre_stack)
            print ('visited:', visited)
            visited.append(current)
            stack.remove(current)
            stack = pre_stack + stack
            print ('Round 2')
            print ('stack:', stack)
            print ('pre_stack:', pre_stack)
            print ('visited:', visited)
        print ('path:', visited)
        return False

    def dfs(self, element):
        start_v = list(self.vertices.keys())[0]
        stack = [start_v]
        visited = []
        while stack:
            current = stack[0]
            if current == element:
                visited.append(current)
                print ('path:', visited)
                return True
            for v in self.vertices[current]:
                if v not in visited and v not in stack:
                    stack.insert(0, v)
            visited.append(current)
            stack.remove(current)
        print ('path:', visited)
        return False

graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '5')
graph.add_edge('1', '3')
graph.add_edge('3', '4')
graph.add_edge('3', '6')
graph.add_edge('4', '6')
graph.add_edge('5', '6')

print(graph.vertices)
# print (graph.bfs('1'))
# print (graph.bfs('6'))
# print (graph.bfs('7'))

print (graph.dft('1'))
print (graph.dft('6'))
print (graph.dft('7'))




{'0': {'5', '1', '3'}, '1': {'0', '3'}, '2': set(), '3': {'6', '0', '4', '1'}, '4': {'6', '3'}, '5': {'6', '0'}, '6': {'4', '5', '3'}}