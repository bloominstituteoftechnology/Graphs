"""
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

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
# 1. Translate the problem into graph terminology
# 2. Build your graph
# 3. Traverse your graph

# undirected, cyclic, sparse
# nodes are words, edges/neighbors are words that differ by one and only one letter
from util import Stack, Queue


f = open('projects/graph/words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set([w.lower() for w in words])
# print(word_set)

def get_neighbors(w):
    '''
    retrun all words in word_set that have 1 and only 1 letter different
    '''
    neighbors = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letter_list = list(w)
    # For each letter in the word:
    for i in range(len(letter_list)):
        # For each letter in the alphabet:
        for letter in alphabet:
            # Replace the word letter with the alphabet letter
            temp_word = list(letter_list)
            temp_word[i] = letter
            new_word = "".join(temp_word)
            # Check if the resulting word is in the word_set
            if new_word in word_set and new_word != w:
                # If so, add to neighbor list
                neighbors.append(new_word)
    return neighbors 


def find_ladders(begin_word, end_word):
    '''
    Find a word transformation between begin and end word
    Use BFS
    '''
    # Make empty queue
    q = Queue()
    # Add the first word
    q.enqueue([begin_word])
    # Create an empty set
    visited = set()
    # while the queue is not empty
    while q.size() > 0:
        # dequeue path
        path = q.dequeue()
        # grab last word from path
        w = path[-1]
        # check if it's the target word
        if w == end_word:
            return path
        if w not in visited:           
            visited.add(w)
            for neighbor in get_neighbors(w):
                new_path = path + [neighbor]
                q.enqueue(new_path)

print(find_ladders("bacon", "happy"))