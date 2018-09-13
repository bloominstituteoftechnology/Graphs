import random
import math
class Node:
    id = 0
    def __init__(self, x, y, radius = .2, value = None):
        self.x = x
        self.y = y
        self.radius = radius
        self.id = Node.id
        self.color = 'white'
        self.value = value
        Node.id += 1
    
    def assign_random_color(self):
        r = lambda: random.randint(50,255)
        self.color = '#%02X%02X%02X' % (r(),r(),r())

    @classmethod
    def create_with_random_props(cls, graph_width, graph_height, radius = .2, value = None):
    
        random_x = random.random() * graph_width
        random_y = random.random() * graph_height
        if random_x + radius > graph_width:
            random_x -= radius
        if random_y + radius > graph_height:
            random_y -= radius
        
        
        return cls(random_x, random_y, radius, value)