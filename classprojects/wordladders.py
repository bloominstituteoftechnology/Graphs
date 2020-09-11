import string
​
words = set()
​
with open("words.txt") as f:
    for word in f:
        words.add(word.lower().strip())
​
class Queue():
    def __init__(self):
        self.queue = []
​
    def enqueue(self, value):
        self.queue.append(value)
​
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
​
    def size(self):
        return len(self.queue)
​
cache = {}
​
def get_neighbors(word):
    if word not in cache:
        neighbors = []
​
        # O(26680*n) == O(n)
        for w in words: # O(26680)
            if len(w) != len(word):
                continue
​
            diffs = 0
​
            for i in range(len(w)): # O(n) over the length of the word
                if w[i] != word[i]:
                    diffs += 1
​
            if diffs == 1:
                neighbors.append(w)
​
            cache[word] = neighbors
​
    return cache[word]
​
def get_neighbors_2(word):     # word = "sail"
    word_letters = list(word)  # word_letters = ['s', 'a', 'i', 'l']
​
    neighbors = []
​
    # O(26*n) == O(n)
    for i in range(len(word)):  # i from 0 to 3   O(n) over the length of the word
        for l in string.ascii_lowercase:  # l from a...z  O(26)
            candidate_letters = list(word_letters) # make a copy of word_letters = ['s', 'a', 'i', 'l']
            candidate_letters[i] = l  # ['s', 'a', 'i', 'l'] -> ['a', 'a', 'i', 'l']
            candidate = "".join(candidate_letters)  # ['a', 'a', 'i', 'l'] -> "aail"
​
            if candidate != word and candidate in words:  # is "aail" in the dictionary?
                neighbors.append(candidate)
​
    return neighbors
​
def bfs(begin_word, end_word):
    visited = set()
    q = Queue()
​
    q.enqueue([begin_word])
​
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
​
        if v not in visited:
            visited.add(v)
​
            if v == end_word:
                return path
​
            for neighbor in get_neighbors_2(v):
                q.enqueue(path + [neighbor])  # Makes a new list
                #path_copy = list(path)
                #path_copy.append(neighbor)
                #q.enqueue(path_copy)
​
print(bfs("sail", "boat"))