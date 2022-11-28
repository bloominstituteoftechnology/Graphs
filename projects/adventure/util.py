
# Note: This Queue class is sub-optimal. Why?
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph():
    def __init__(self):
       self.rooms = {} 
    def add_room(self, room_id, exits = None):
        self.rooms[room_id] ={}
        
        if exits:
            for ex in exits:
                self.rooms[room_id][ex]= None
            else:
                self.rooms[room_id] = {}  
    def get_room_exits(self, room) :
        return self.rooms[room.id].items()        
    
    def has_room(self, room):
        if self.rooms.get(room.id):
            return True
        return False
    
    def add_exit(self, next_room, ex, current_room):
        self.rooms[next_room.id][ex]= current_room.id 
        
    def size(self):
        return len(self.rooms)   