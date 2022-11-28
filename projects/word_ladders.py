import string



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
    def print_list(self):
        return print(self.queue)
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()
word_set = set()

for word in words:
    word_set.add(word.lower())
    
    
def bfs(start_word, end_word):
    q = Queue()
    visited = set()
    
    q.enqueue([start_word])
    
    while q.size()>0:
        current_path = q.dequeue()
        print("DQ",current_path)
        
        curr_word = current_path[-1]
        print("CW", curr_word)
        
        if curr_word == end_word:
            return current_path
         
        if curr_word not in visited:
            visited.add(curr_word)
            
            neighbors = find_neighbors(curr_word)
            
            for n in neighbors:
                path_copy = list(current_path)
                path_copy.append(n)
                q.enqueue(path_copy)
        
def find_neighbors(word):
    print(word)
    neighbors = []
    for i in range(len(word)):
        for alpha in string.ascii_lowercase:
            
            word_list = list(word)
            word_list[i]=alpha
            maybe_neighbor = "".join(word_list)
            
            if maybe_neighbor in word_set and maybe_neighbor !=word:
                neighbors.append(maybe_neighbor)
                return neighbors
            
            
            
print(bfs("goat", "boat"))            
print(bfs('hit', 'cog'))
print(bfs('sail', 'boat'))