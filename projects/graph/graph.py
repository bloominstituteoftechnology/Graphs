"""
Simple graph implementation
"""

from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = []

    def add_edge(self, v1, v2):
        self.vertices[v1].append(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

        
    def bft_recursive(self, explored, prospects = set()):
        # These first two lines are just here to mutate the argument formating
        # If the method was called like this.. dft_recursive(1)
        # It would reformat to... dft_recursive(set([1]), set([**insert neighbors of 1 here**]))
        # The explored arg serves as a set of "seen" verts
        # The prospects arg serves as a set of neighboring vertices that have the potential to be "explored"
        if type(explored) != set: 
            return self.dft_recursive( set([explored]), set(self.get_neighbors(explored)) )

        # Uncomment these if you want a visual representation of the recursion inside the console
        #print(f'explored:{explored}')
        #print(f'exploring:{prospects}')

        # This is our base case, if there are no prospects every vert has been explored
        if prospects != set():
            # Filter out verts we have already explored
            last_explored_verts = prospects.difference(explored)
            # Add unexplored prospects to our explored set 
            explored = explored.union(prospects)
            # Clear our prospects set
            prospects.clear()
            
            # For each of our most recently explored verts
            for vert in last_explored_verts:
                # Add each of their neighbor verts as prospects
                for prospect in self.get_neighbors(vert):
                    prospects.add(prospect)
            
            # Recurse until our prospects set is empty
            return self.dft_recursive(explored, prospects)
        else: 
            return explored
        
    def bft(self, starting_vertex):
        # Create an empty que and add the starting_vertex 
        q = Queue()
        q.enqueue([starting_vertex])
        # Create an empty set to track visited verticies
        seen = set()
        # while the que is not empty: 
        while q.size():
            verts = q.dequeue()
            for vert in verts:
                if vert not in seen:
                    seen.add(vert)
                    q.enqueue(self.get_neighbors(vert))
        print(seen)
        
    def dft_recursive(self, current_vert, seen_verts=set() ):
            seen_verts.add(current_vert)                                # add current vert to seen verts
            if seen_verts == self.vertices.keys(): print(seen_verts)    # [BASE CASE!] if seen verts == self.vertices print
            for vert in self.get_neighbors(current_vert):               # for vert in current vert's neighbors
                if vert in seen_verts: return                           # if vert has been seen return
                else: self.dft_recursive(vert, seen_verts)              # else recurse with that vert as new current_vert

    def dft(self, starting_vertex):
        # Create a stack with the starting vert
        s = Stack()
        s.push([starting_vertex])
        # Create an empty set to track visited verticies
        seen = set()
        # while the que is not empty: 
        while len(seen) != len(self.vertices):
            verts = s.pop()
            for vert in verts:
                if vert not in seen:
                    seen.add(vert)
                    s.push(self.get_neighbors(vert))
        print(seen)

    def bfs(self, starting_vert, target_vert):
        #create queue to hold array of paths (array of arrays or verts)
        q = []
        it = 0
        # push the first path into the queue
        q.append([starting_vert])
        while q:
            # get the first path from the queue
            path = q.pop(0)
            # get the last_vert from the path
            last_vert = path[-1]
            it += 1
            print(f'\nCurrent Itteration: {it}\nCurrent Queue: {q}\nCurrent Path: {path}')
            # Last vert of path is target?
            if last_vert == target_vert: return path
            # enumerate all adjacent vert, construct a new path and push it into the queue
            for neighbor in self.get_neighbors(last_vert):
                new_path = list(path)
                new_path.append(neighbor)
                q.append(new_path)
                print(f'Appending {neighbor}, neighbor of {last_vert} to current path.\nAdding updated path: {new_path} to the back of the queue.')

    def dfs(self, starting_vert, target_vert):
        #create stack to hold array of verts
        s = [starting_vert]
        seen = set()
        while len(seen) != len(self.vertices):
            if s[-1] in seen: s.pop()                       # top of the stack has been seen? -> pop from stack
            elif s[-1] == target_vert: return s             # top of the stack is the target? -> return stack
            else: seen.add(s[-1])                           # else add top of the stack to seen
            prospect = False                                # we have not discovered a prospect for next generation
            for neighbor in self.get_neighbors(s[-1]):      # for neighbor of top of the stack
                if neighbor not in seen:                    # if neighbor has not been seen
                    prospect = neighbor                     # neighbor is a prospect
            if (prospect): s.append(prospect)               # if we found a prospect add it to the top of the stack

    #def dfs_recursive(self, stack, target_vert, seen_verts=set() ):


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
