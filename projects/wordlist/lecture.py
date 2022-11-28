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
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
["hit", "hot", "dot", "dog", "cog"]

beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log"]
[]

PLAN:
Translate in Graph terminology
Build Graph
Traverse graph 

Vertex : Word
Edge: a possible 1 letter transformation from a word to another word
Weights: None 
Path: 1 letter Transformations from begin word to end word 

Build Graph:
Creating all possible transformations in an adjecency list will be too expensive
how to find out next vertex by determining if its a valid vertex from word list.
we should visit a vertex if its in the wordlist

Traverse graph :
Shortest -> BFS
start from begin word and generate word transformations from it
enqueue transformations that are in the word list, ignore rest
once we find endword, return path we took to get there
"""
from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findLadders(beginWord,endWord,wordlist):
    words = set(wordlist)
    visited = set()
    queue = deque()
    queue.append([beginWord])

    while len(queue)>0:
        currPath = queue.popleft()
        currWord = currPath[-1]
        if currWord in visited:
            continue

        visited.add(currWord)

        if currWord == endWord:
            return currPath

        for i in range (len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i]+ letter + currWord[i+1:]
                if transformedWord in wordlist:
                    newPath = list(currPath)
                    newPath.append(transformedWord)
                    queue.append(newPath)
                    
    return []

print (findLadders("hit","cog",["hot","dot","dog","lot","log","cog"]))