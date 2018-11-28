import graph
import random

class Map:
    def __init__(self, *argv):
        self.graph = graph.Graph()
        self.amount_of_rooms = 0
        self.directions = ['n','e','s','w']
        if len(argv)>0:
            self.generate_random_map(self.graph, argv[0])
        else:
            self.generate_random_map(self.graph)

    def generate_random_map(self, graph, *argv):
        room_size = 9
        if len(argv)==1:
            room_size = argv[0]
        queue = [(0,0)]
        while self.amount_of_rooms<room_size:
            current_room = queue.pop(0)
            self.add_room(current_room)
            amount_to_add = random.randint(1,5)
            directions_to_add = self.choose_edges(amount_to_add)
            for direction in directions_to_add:
                queue.append(self.create_key(direction, current_room))
    
    def create_key(self, direction, room):
        x, y = room
        if direction == 'n':
            y += 1
        else if direction == 'e':
            x += 1
        else if direction == 's':
            y += -1
        else if direction == 'w':
            x += -1
        else:
            raise 'Direction given is an invalid option.', direction
        return (x, y)

    def choose_edges(self, amount):
        rooms_to_add = []
        directions_copy = []
        for direction in self.directions:
            directions_copy.append(direction)
        for x in range(amount):
            rooms_to_add.append(directions_copy.pop(random.randint(0,len(directions_copy)-1)))
        return rooms_to_add
    
    def add_room(self, room):
        self.graph.add_vertex(room)
        self.amount_of_rooms += 1

# Tests
map = Map()
# print(map.graph.vertices)
# print(map.graph.vertices[(1,1)])
# print(map.graph.vertices[(1,1)]['edges'])
# map = Map(4)