class Node:
    id = 0
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.radius = radius
        self.id = Node.id
        self.color = 'white'
        Node.id += 1
        self.color = 'white'
        Node.id += 1
    
    def assign_random_color(self):
        r = lambda: random.randint(50,255)
        self.color = '#%02X%02X%02X' % (r(),r(),r())

