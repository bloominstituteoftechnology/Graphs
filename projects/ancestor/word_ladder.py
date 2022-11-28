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


with open('words.txt', "r") as f:
    words = f.read().split("\n")
word_set = set()
for word in words:
    word_set.add(word.lower())
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def get_neighbors(word):
    neighbors = []

    #turn word into a letters list
    string_word = list(word)

    # for each letters
    for i in range(len(string_word)):
        # Swap each letter
        for letter in letters: # because this part of the loop is the same, overall O(n). word length stays same
            temp_word = list(string_word) #make a copy
            temp_word[i] = letter # each letter being changed
            w = "".join(temp_word)

            if w != word and w in word_set: # haven't created yet
                neighbors.append(w)

    return neighbors 



# BFS with path
def find_ladders(begin_word, end_word):
    q = Queue()
    visited = set()
    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        last_vertex = path[-1]

        if last_vertex not in visited:
            visited.add(last_vertex)
            
            if last_vertex == end_word:
                return path

            for neighbor in get_neighbors(last_vertex): # haven't made it yet, but top-down does this
                path_copy = list(path)
                path_copy.append(neighbor)

                q.enqueue(path_copy)

print(find_ladders("dog", "cat"))