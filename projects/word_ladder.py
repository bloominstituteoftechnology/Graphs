# word ladder- transform one word into another only by changing
# one letter at a time, eg hit -> cog
# hit -> hot -> hog -> cog

# this is assuming the graph and queue classes are already created

def find_ladders(begin_word, end word):
    visited = set()
    q = Queue()
    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path

            for neighbors in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    return None

# assumes having a dictionary txt file named words.txt
word_set = set()

with open['words.txt'] as f:
    for line in f:
        word = line.strip()
        word_set.add(word)

import string   # python library
letters = list(string.ascii_lowercase)

def get_neighbors(word):
    neighbors = []

    string_word = list(word)

    for in range(len(string_word)):
        for letter in letters:
            temp_word = list(string_word)

            temp_word[i] = letter

            w = "".join(temp_word)

            if w == word:
                continue
            
            if w in word_set:
                neighbors.append(w)

    return neighbors
