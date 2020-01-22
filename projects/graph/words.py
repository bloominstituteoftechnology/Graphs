from util import Stack, Queue  # These may come in handy
import string

"""
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
"""

"""
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
"""

# Build graph
# Words are nodes , one letter apart is edges
# Do a BFS from start word to end word

f = open('words.txt', 'r')
words = f.read().split('\n')
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

print(len(word_set))


def get_neighbors(word):
    """
    Return all the words from word_list that 1 letter different
    """
    # Change on letter to another on the alphabet incrementally
    # Search the graph for that
    # Repeat for each letter in the word

    neighbors = []
    alphabet = list(string.ascii_lowercase)
    # for each letter in the word change it
    for i in range(len(word)):
        #  for each letter in the alphabet
        for letter in alphabet:
            # Change the word letter to the alphabet letter
            list_word = list(word)
            list_word[i] = letter
            w = ''.join(list_word)
            # if the new word is in the word_list
            if w != word and w in word_set:
                neighbors.append(w)
                # Add it to the neighbors
    return neighbors


print(get_neighbors('cat'))


def find_ladders(begin_word, end_word):
    # DO BFS
    # Create queue
    queue = Queue()
    # Enqueue a path to the starting word
    queue.enqueue([begin_word])
    # Create a visited set
    visited = set()
    # While the queue is not empty:
    while queue.size() > 0:
        # Dequeue the path of next path
        path = queue.dequeue()
        # Grab the last word from the path
        v = path[-1]
        # If it's not been visited
        if v not in visited:
            # Check if word is our end word, if so return path
            if v == end_word:
                return path
        # Mark it as visited
            visited.add(v)
        # Enqueue a path to each other
            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                queue.enqueue(path_copy)


print(find_ladders('sail', 'boat'))

