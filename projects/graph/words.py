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

# read txt
# put each word into graph with key as length of word
from graph import Graph
import sys

start_word = 'sail'
end_word = 'boat'

first = [start_word[0], end_word[0]]
last = [start_word[-1], end_word[-1]]

length = len(start_word)

f = open("projects/graph/words.txt", 'r')
all_words_length = [word for word in f.read().splitlines()
                    if len(word) == length and word.islower()]
f.close()

gr = Graph()

for word in all_words_length:
    if word[0] in first and word[-1] in last:
        gr.add_vertex(word)

for v1 in gr.vertices:
    for v2 in gr.vertices:
        oneOff = 0
        for i in range(0, len(v1)):
            if v1[i] == v2[i]:
                oneOff += 1
        if oneOff == len(v1) - 1:
            gr.add_edge(v1, v2)

print(gr.bfs(start_word, end_word))
