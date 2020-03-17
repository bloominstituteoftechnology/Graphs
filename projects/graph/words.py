from util import Stack, Queue



f = open('words.txt', 'r')
words = f.read().lower().split("\n")
f.close()

def words_are_neighbors(w1, w2):
    '''
    return True if words are one letter apart
    False otherwise
    '''
    list_word = list(w1)
    # Go through each letter in the word
    for i in range(len(list_word)):
        # swap with each letter in the alphabet
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            # Check if that equals given word
            temp_word = list_word.copy()
            temp_word[i] = letter
            if "".join(temp_word) == w2:
                return True
    return False
def words_are_neighbors(w1, w2):
    if len(w1) != len(w2):
        return False
    for i in range(len(w1)):
        if w1[:i] == w2[:i] and w1[i+1:] == w2[i+1:]:
            return True
    return False

def word_ladder(self, begin_word, end_word):
    q = Queue()

    q.enqueue([begin_word])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        w = path[-1]

        if w == end_word:
            return path
        
        if w not in visited:
            for i in get_neighbors():
                path_copy = path.copy()
                path_copy.append(i)
                n.enqueue(path_copy)
