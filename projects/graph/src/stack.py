class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop_1(self):
        if self.size() > 0:
            return self.stack.pop()
        return None
    
    def size(self):
        return len(self.stack)
        
        
if __name__ == "__main__":
           
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.size())
    print(s.pop_1())
    print(s.pop_1())
    print(s.pop_1())
    print(s.size())