import math
import random
import uuid
from room import Room
from player import Player
from world import World



class Explorer:
    def __init__(self, world, player):
        self.world = world
        self.player = player
        self.traveled = set()
        self.bread_crumbs = list()
        self.world_size = len(self.world.rooms)
        self.directions = list()
        self.position = 0
        self.prev_position = None

    def get_progress(self):
        percentage = "{:.2%}".format(len(self.traveled)/self.world_size)
        print(f"{percentage} of the Labrinth has been processed.")

    def get_is_complete(self): return math.floor(len(self.traveled)/self.world_size)

    def join(self, a, b):
        c = a + b
        return c

    def travel(self, path):
        if type(path) != list: path = path.path
        [self.traveled.add(room) for room in path]
        self.bread_crumbs += path
        if self.get_is_complete(): return
        self.position = (path[-1])
        #self.directions += self.get_directions_from(path)
        if len(self.exits_of(self.position)) < 3: self.backtrack(path)

    def backtrack(self, path):
        room = next( neighbor for neighbor in self.exits_of(self.position) if neighbor != self.prev_position )
        self.prev_position = self.position
        self.travel([room])

    def go(self):
        switch = False
        while not self.get_is_complete() and self.bread_crumbs[-3:] != [0,0,0]:
            #if len(self.traveled)/self.world_size < .98 or 
            tail = self.bread_crumbs[-4:]
            if(tail == [6,62,65,134,144] or tail == [65,62,6,6,23]):
                switch = True
            self.get_progress()
            print(f'You have traveled {self.bread_crumbs}')
            x = self.find_dead_ends(self.position)
            print(x)
            self.travel(x) 
            if switch:
                print("BFT!")
                switch = False
                self.travel(self.bfs(self.position, self.bft(self.position)))
        self.get_progress()
        return self.get_directions_from(self.bread_crumbs)

    def bfs(self, room, target_room):
        #create queue to hold array of paths (array of arrays or verts)
        q = []
        it = 0
        # push the first path into the queue

        q.append([room])

        print(q)
        
        while q:
            print("BFS!")
            # get the first path from the queue
            path = q.pop(0)
            # get the last_room from the path
            last_room = path[-1]
            print(last_room)
            it += 1
            print(f'\nCurrent Itteration: {it}\nCurrent Queue: {q}\nCurrent Path: {path}')
            # Last vert of path is target?
            if last_room == target_room:
                print("we returning")
                print(room)
                print(path)
                return path
            # enumerate all adjacent vert, construct a new path and push it into the queue
            
            for neighbor in self.exits_of(last_room):
                if(neighbor) not in set(path):
                    new_path = list(path)
                    print(f'neighhhhhhhhhh {neighbor}')
                    new_path.append(neighbor)
                    q.append(new_path)
                    print(f'\nIt: {it}\n Q: {q}\nPath: {path}')
                    print(f'Appending {neighbor}, neighbor of {last_room} to current path.\nAdding updated path: {new_path} to the back of the queue.')
        
    def bft(self, current_location):
        # Create an que and add the current_location 
        q = [current_location]
        # Create an empty set to track visited verticies
        seen = set()
        # while the que is not empty:
        while q:
            # pull next room in line from que
            room = q.pop(0)
            # if the room is not in seen set
            if room not in seen:
                # add it to seen set
                seen.add(room)
                # get it's neighboring rooms
                neighbors = self.exits_of(room)
                print(f'\ncurrent is {room}: {neighbors}')
                if set(neighbors).difference(self.traveled):
                    print(f'room: {room}')
                    for neighbor in neighbors:
                        if neighbor not in set(self.bread_crumbs):
                            return neighbor

                for neighbor in neighbors:
                    q.append(neighbor)
        print(seen)
    
    def find_closest_dead_end(self, current_location):
        # Create an que and add the current_location 
        q = [current_location]
        # Create an empty set to track visited verticies
        seen = set()
        # while the que is not empty:
        while q:
            # pull next room in line from que
            room = q.pop(0)
            # if the room is not in seen set
            if room not in seen:
                # add it to seen set
                seen.add(room)
                # get it's neighboring rooms
                neighbors = self.exits_of(room)
                # if dead end return current room
                if set(neighbors).issubset(seen) and len(neighbors) < 2: return room
                # else add neighbors to the que
                for neighbor in neighbors:
                    q.append(neighbor)
        print(seen)

    def find_dead_ends(self, current_location):
        print("\n#####################\n# FINDING DEAD ENDS #\n#####################")
        # Create a que of objects.
        # Each array will hold...
        # A set of traveled nodes
        # An ordered list of it's path
        # And a count of routes it's passed 
        q = [Seeker(uuid.uuid4(), [current_location])]
        q[0].seen = set()
        # Create an empty list to store dead ends
        dead_ends = []
        
        # while the que is not empty and less than 2 dead end:
        while q and len(dead_ends) < 2 :
            # pull the next array in line from que
            print('hello')
            print(current_location)
            seekr = q.pop(0)
            print(seekr.seen)
            print(seekr.type)
            # if the seekr is not in the attached seen set
            room = seekr.path.pop()
            if room not in seekr.seen:
                # add it to seen set
                seekr.record(room)
                # get it's neighboring rooms
                neighbors = self.exits_of(room)
                print(f'current is {room}: neighbors:{neighbors} visited: {seekr.seen}')
                if set(neighbors).issubset(seekr.seen) and len(neighbors) < 2:
                    if  not set(neighbors).issubset(self.traveled):
                        #if self.end_checker(seekr):
                            print('dead end')
                            dead_ends.append(seekr)
                if set(neighbors).issubset(seekr.seen) and len(neighbors) > 1 and self.prev_position not in set(neighbors):
                    #if self.end_checker(seekr):
                        print('loop')
                        last_step = [neighbor for neighbor in neighbors if neighbor not in seekr.seen and neighbor is not seekr.path[-2]]
                        if (last_step):
                            seekr.path.append(last_step)
                        seekr.upgrade_type()
                        dead_ends.append(seekr)
                # if we get to a dead end we need to stop adding to the que
                if dead_ends == []:
                    for neighbor in neighbors:
                        if neighbor not in seekr.seen or self.traveled:
                            seekr.path_sum += 1
                        # careful to append the seen set to the new object getting added to the que
                        path = seekr.path.copy()
                        path.append(neighbor)
                        q.append(Seeker(uuid.uuid4(), path, seekr.seen.copy()))

        
        if dead_ends != []:
            [print(f'Dead end discovered: [ Room {end.path[-1]} Path: {end.path} ]') for end in dead_ends]
            if len(dead_ends) > 1: return self.compare_end_types(dead_ends[0], dead_ends[1])
            return dead_ends[0]
        else: self.bfs(current_location, self.bft(current_location))

    def end_checker(self, end):
        if len(set(end.path).difference(self.traveled)) > len(end.path) / 1.75:
            return False
        else: return True



    def exits_of(self, roomID):
        room =  self.world.rooms[roomID]
        neighbors = []

        #if room.n_to is not None: neighbors.append(['n',room.n_to.id])
        #if room.s_to is not None: neighbors.append(['s',room.s_to.id])
        #if room.w_to is not None: neighbors.append(['e',room.e_to.id])
        #if room.e_to is not None: neighbors.append(['w',room.w_to.id])
        if room.n_to is not None: neighbors.append(room.n_to.id)
        if room.s_to is not None: neighbors.append(room.s_to.id)
        if room.e_to is not None: neighbors.append(room.e_to.id)
        if room.w_to is not None: neighbors.append(room.w_to.id)

        return neighbors

    def get_directions_from(self, path):
        # convert to list if seeker is passed
        if type(path) == Seeker: path = path.path
        # this is here incase we are backtracking
        if len(path) == 1 : path.insert(0, self.position)
        #convert path to coords 
        coords = [self.world.rooms[room].get_coords() for room in path]
        # itterate over enumerated coords appending directions
        directions = []
        for i, xy in enumerate(coords):
            if i: # if y value is < next items y value change this coord to north.. ect... ect...
                print(f'comparing {coords[i-1][1]} ')
                if coords[i-1][1] < coords[i][1]: directions.append('n')
                if coords[i-1][1] > coords[i][1]: directions.append('s')
                if coords[i-1][0] < coords[i][0]: directions.append('e')
                if coords[i-1][0] > coords[i][0]: directions.append('w')
        print(f'dir : {directions} and path : {path}')
        return directions

    def compare_end_types(self,a,b = None):
        print(f'compare {a}')
        print(f'compare {b}')
        # if array as input split
        if b == None: 
            b = a[1]
            a = a[0]
        # compare types
        if a.type < b.type: return a
        if a.type > b.type: return b
        # if type == type dig deeper
        return self.compare_ends(a,b)

    def compare_ends(self,a,b = None):
        # if array as input split
        if b == None:
            b = a[1]
            a = a[0]
        # compare lengths
        if len(a.path) < len(b.path): return a.path
        if len(a.path) > len(b.path): return b.path
        # compare path sum
        if a.path_sum < b.path_sum: return a.path
        if a.path_sum > b.path_sum: return b.path
        #compare last node neighbors here
        #if a.path[-1]
        # screw it
        #return random.choice([a,b])
        return a.path

class Seeker:
    def __init__(self, uid, start, seen = set()):
        self.id = uid
        self.seen = seen
        self.path = start
        self.path_sum = 0
        self.passes = 0
        self.type = 0
    def record(self, room):
        self.seen.add(room)
        self.path.append(room)
    def upgrade_type(self):
        if self.type == 2 : self.type = 3
        if self.type == 1 : self.type = 2
        if self.type == 0 : self.type = 1

























"""

class Graph:


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
        q = []
        q.append([starting_vertex])
        # Create an empty set to track visited verticies
        seen = set()
        # while the que is not empty: 
        while len(q):
            verts = q.pop(0)
            for vert in verts:
                if vert not in seen:
                    seen.add(vert)
                    q.append(self.get_neighbors(vert))
        print(seen)
        
    def dft_recursive(self, current_vert, seen_verts=set() ):
            seen_verts.add(current_vert)                                # add current vert to seen verts
            if seen_verts == self.vertices.keys(): print(seen_verts)    # [BASE CASE!] if seen verts == self.vertices print
            for vert in self.get_neighbors(current_vert):               # for vert in current vert's neighbors
                if vert in seen_verts: return                           # if vert has been seen return
                else: self.dft_recursive(vert, seen_verts)              # else recurse with that vert as new current_vert

    def dft(self, starting_vertex):
        # Create a stack with the starting vert
        s = []
        s.append([starting_vertex])
        # Create an empty set to track visited verticies
        seen = set()
        # while the que is not empty: 
        while len(seen) != len(self.vertices):
            verts = s.pop()
            for vert in verts:
                if vert not in seen:
                    seen.add(vert)
                    s.append(self.get_neighbors(vert))
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
"""
