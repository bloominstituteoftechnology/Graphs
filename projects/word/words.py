import string

## demo for method computing neighbors on the fly

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


# Read words in from the file, add to set of words

word_set = set()

with open("words.txt", "r") as f:
    for word in f:
        word_set.add(word.strip().lower())

# print(word_set)

def get_neighbors_1(word):

    neighbors = []
    word_letters = list(word)

    # solution 1
    for i in range(len(word_letters)):
        for letter in list(string.ascii_lowercase):

            # make a copy of the word
            temp_word = list(word_letters)

            # sub the new leter into the word copy
            temp_word[i] = letter

            # make it a string
            temp_word_str = "".join(temp_word)

            # if it is real, add it to return set
            if temp_word_str != word and temp_word_str in word_set:
                neighbors.append(temp_word_str)

    return neighbors

def get_neighbors_2(word):
    # look for words the same length
    # if they differ by one letter, add to return set
    def word_diff_by1(w1, w2):
        if len(w1) != len(w2):
            return False
        
        diff_count = 0

        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff_count += 1

        return diff_count == 1

    neighbors = []

    for word2 in word_set:
        if word_diff_by1(word, word2):
            neighbors.append(word2)
    
    return neighbors

get_neighbors = get_neighbors_1

def find_word_ladder(begin_word, end_word):  # BFS to find shortest path
    visited = set()
    q = Queue()

    q.enqueue(begin_word)

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    # if we get here no path found.

    return None

print(find_word_ladder("sail", "boat"))


