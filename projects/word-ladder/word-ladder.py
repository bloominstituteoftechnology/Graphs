f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()
​
word_set = set()
for word in words:
    word_set.add(word.lower())
​
# Instead of converting the world list into a graph
# I'm going to make a helper function that looks up
# What neighbors or edges a word would have in the graph
​
​
# Calculate a small part of the graph to find edges and vertexes relevant to 
# our current problem
def get_neighbors(word):
    neighbors = []
    word_list = list(word)
    # represents our word as [w, o, r, d]
    for i in range(len(word_list)):
        for letter in list('abcdefghijklmnopqrstuvwxyz'):
            temp_word = list(word_list)
            temp_word[i] = letter
            w = "".join(temp_word) # Join the list version of the world back into a string
            if w != word and w in word_set:
                neighbors.append(w)
    
    return neighbors
​
​
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
​
​
# Use a BFS variant to find our answer
def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])
    while q.size() > 0:
        path = q.dequeue()
        current = path[-1]
        if current not in visited:
            visited.add(current)
            if current == end_word:
                return path
            for new_word in get_neighbors(current):
                new_path = list(path)
                new_path.append(new_word)
                q.enqueue(new_path)
​
​
print(find_word_ladder("sail", "boat"))
print(find_word_ladder("sail", "boats"))
print(find_word_ladder("sail", "bbbb"))
# print(find_word_ladder("sail", "boat"))