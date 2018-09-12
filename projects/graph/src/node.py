import random
class Node:
    id = 0
    def __init__(self, x, y, radius = .2):
        self.x = x
        self.y = y
        self.radius = radius
        self.radius = radius
        self.id = Node.id
        self.color = 'white'
        Node.id += 1
    
    def assign_random_color(self):
        r = lambda: random.randint(50,255)
        self.color = '#%02X%02X%02X' % (r(),r(),r())

    @classmethod
    def create_with_random_props(cls, graph_width, graph_height, radius = .2):
        random_x = random.random() * graph_width
        random_y = random.random() * graph_height
        return cls(random_x, random_y, radius)