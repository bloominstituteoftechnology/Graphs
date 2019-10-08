#!/usr/bin/env python
from util import Queue
from typing import List
'''
Given two words (beginWord and endWord), and a dictionary's word list, return the shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return None if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Sample:
beginWord = "hit"
endWord = "cog"
return: ['hit', 'hot', 'cot', 'cog']

beginWord = "sail"
endWord = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None
'''

# words - vertex
# letters different - edges
# shortest transformation sequence -- bfs/path
# dictionary - list of vertices
# beginWord - starting vertex
# endWord - destination vertex
# no duplicates -
# same length - edges (part)

# in order of easiness:
# 1. load input
# 2. implement queue
#
#
with open("words.txt", "r") as w:
    WORDS = set(x.lower().strip() for x in w.readlines())

# ffind/create all nodes/edges for words with one letter different
# replaces entry in adjacney list for that node
def get_neighbors(word: str) -> List[str]:
    global WORDS
    neighbors = list()
    string_word = list(word)
    for i in range(len(string_word)):
        for letter in "abcdefghijklmnopqrstuvwxyz":
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "".join(temp_word)
            if w != word and w in WORDS:
                neighbors.append(w)

    return neighbors

def find_word_ladder(begin_word: str, end_word: str) -> List[str]:
    qq = Queue()
    visited = set()
    qq.enqueue([begin_word])
    while qq.size() >0:
        path = qq.dequeue()
        word = path[-1] # vertex is our word
        if word not in visited:
            # here's where we do the thing
            if word == end_word:
                return path
            else:
                visited.add(word)
                for next_word in get_neighbors(word):
                    path_copy = list(path)
                    path_copy.append(next_word)
                    qq.enqueue(path_copy)

if __name__=='__main__':

    print(find_word_ladder("sail", "boat"))
