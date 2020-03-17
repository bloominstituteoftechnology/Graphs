# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.

# Sample:
# begin_word = "hit"
# end_word = "cog"
# return: ['hit', 'hot', 'cot', 'cog']
# begin_word = "sail"
# end_word = "boat"
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# beginWord = "hungry"
# endWord = "happy"
# None


# 1. Translate the problem into graph terminology
# 2. Build your graph
# 3. Traverse your graph

# undirected, cyclic, sparse
# nodes are words, edges/neighbors are words that differ by one and only one letter
from util import Stack, Queue  # These may come in handy


f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set([w.lower() for w in words])

print(word_set)
print(len(word_set))


def get_neighbors(w):
    '''
    Return all words in word_set that have 1 and only 1 letter different
    '''
    neighbors = []
    # For each letter in the word
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_list = list(w)
    for i in range(len(letter_list)):
        # For each letter in the alphabet
        for letter in alphabet:
            # Replace the word letter with the alphabet letter
            temp_word = list(letter_list)
            temp_word[i] = letter
            new_word = "".join(temp_word)
            # Check if the resulting word is in the word_set
            # (Ignore if equal to the original word)
            if new_word in word_set and new_word != w:
                # If so, add to neighbor list
                neighbors.append(new_word)
    return neighbors


# get_neighbors("sail")


# bat

# cat, eat, fat, hat, lat, mat, oat, pat....
# bet, bit...
# bad, bae


def find_ladders(begin_word, end_word):
    '''
    Find a word transformation between begin and end word
    Use BFS
    '''
    q = Queue()
    # Enqueue path to starting word
    q.enqueue([begin_word])
    visited = set()
    # While queue is not empty...
    while q.size() > 0:
        # Dequeue path
        path = q.dequeue()
        # Grab last word from path
        w = path[-1]
        # Check if it's target word, if so return path
        if w == end_word:
            return path
        # Check if it's been visited. If not...
        if w not in visited:
            # Mark it as visited
            visited.add(w)
            # Enqueue a path to each neighbor
            for neighbor in get_neighbors(w):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None


print(find_ladders("sail", "boat"))
