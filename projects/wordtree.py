from util import Stack, Queue  # These may come in handy

f = open('words.txt', 'r')
words = f.read().split("\n")
words = [w.lower() for w in words]
f.close()


word_set = set(words)




letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Get neighbors function
def get_neighbors(word):
    # Create an empty neighbors list
    neighbors = []
    # turn our word into an array of characters
    string_word = list(word)
    # For each letter in the word
    for i in range(len(string_word)):
        # For each letter in the alphabet...
        for letter in letters:
            # Swap that letter with a letter in the alphabet
            temp_word = list(string_word)
            temp_word[i] = letter
            # Reform it into a word string and check if it's in word_set
            w = "".join(temp_word)
            # If it doesn't equal the original word and it's in the set, add to neighbors
            if w != word and w in word_set:
                neighbors.append(w)
    return neighbors




# Implement our traversal
def find_ladders(beginWord, endWord):
    visited = set()
    q = Queue()
    q.enqueue( [beginWord] )
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            if v == endWord:
                return path
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None



print(find_ladders("sail", "boat"))
