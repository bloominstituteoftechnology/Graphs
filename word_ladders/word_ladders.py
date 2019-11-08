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



f = open('word_ladders/words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
      word_set.add(word.lower())

# 1. Is this a graph problem? If so, translate the problem into graph terminology
# 2. Build the graph
# 3. Traverse the graph

def get_neighbors(word):
    '''
    Return all words from word_list that are exactly 1 letter different
    '''
    # time complexity: O(length_of_begin_word)
    # space complexity: O(number_words)
    neighbors = []
    letter_list = list(word)   # "abc" -> ['a', 'b', 'c']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # For each letter in our word...
    for i in range(len(letter_list)):
        # check each other letter
        for letter in letters:
            temp_word = list(letter_list)
            temp_word[i] = letter
            w = "".join(temp_word)
            # and see if that word is in the set
            if w != word and w in word_set:
                # If so, add to return list
                neighbors.append(w)
    return neighbors

def word_ladder_path(begin_word, end_word):
    q = Queue()
    q.enqueue( [begin_word] )
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            if v == end_word:
                return path
            visited.add(v)
            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None

print(word_ladder_path("hit", "cog"))
# print(word_ladder_path("sail", "boat"))
# print(word_ladder_path("africa", "turkey"))