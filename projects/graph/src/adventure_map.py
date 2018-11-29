import graph
import random

class Map:
    def __init__(self, *argv):
        self.graph = graph.Graph()
        self.directions = ['n','e','s','w']
        self.room_size = 9
        if len(argv)==1:
            self.room_size = argv[0]
        self.generate_random_map()

    def generate_random_map(self):
        queue = [(0,0)]
        while len(self.graph.vertices)<self.room_size:
            current_room = queue.pop(0)
            self.add_room(current_room)
            amount_to_add = random.randint(1,4)
            directions_to_add = self.choose_edges(amount_to_add)
            for direction in directions_to_add:
                queue.append(self.create_key(direction, current_room))
    
    def create_key(self, direction, room):
        x, y = room
        if direction == 'n':
            y += 1
        elif direction == 'e':
            x += 1
        elif direction == 's':
            y += -1
        elif direction == 'w':
            x += -1
        else:
            raise 'Direction given is an invalid option.', direction
        return (x, y)

    def choose_edges(self, amount):
        rooms_to_add = []
        directions_copy = []
        for direction in self.directions:
            directions_copy.append(direction)
        if amount == 4:
            return directions_copy
        for x in range(amount):
            rooms_to_add.append(directions_copy.pop(random.randint(0,len(directions_copy)-1)))
        return rooms_to_add
    
    def add_room(self, room):
        self.graph.add_vertex(room)
        x, y = room
        if (x, y+1) in self.graph.vertices:
            self.graph.add_edge(room, (x, y+1))
        if (x+1, y) in self.graph.vertices:
            self.graph.add_edge(room, (x+1, y))
        if (x, y-1) in self.graph.vertices:
            self.graph.add_edge(room, (x, y-1))
        if (x-1, y) in self.graph.vertices:
            self.graph.add_edge(room, (x-1, y))
    
    def drop_a_random_treasure(self):
        room_number = random.randint(0, self.room_size-1)
        count  = 0
        for vertex in self.graph.vertices:
            if count == room_number:
                if  'items' not in self.graph.vertices[vertex]:
                    self.graph.vertices[vertex]['items'] = set()
                self.graph.vertices[vertex]['items'].add('treasure')
                return
            count += 1

# Tests
map = Map(100)
map.drop_a_random_treasure()
print(map.graph.vertices)
# print(map.graph.breadth_first_traversal((0,0)))
# print(map.graph.depth_first_traversal((0,0)))
# print(map.graph.vertices[(1,1)])
# print(map.graph.vertices[(1,1)]['edges'])
# map = Map(4)