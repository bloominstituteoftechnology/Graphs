from util import Stack, Queue  # These may come in handy

# Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
# Note:
# Return None if there is no such transformation sequence.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume begin_word and end_word are non-empty and are not the same.


f = open("words.txt")
words = f.read()
words = words.split("\n")
f.close()

wordSet = set([w.lower() for w in words])

# print(wordSet)

def getNeighbors(word):
    alpha = list("abcdefghijklmnopqrstuvwxyz")

    neighbors = set()
    for index in range(len(word)):
        wordCopy = list(word)
        for letter in alpha:
            wordCopy[index] = letter
            guessWord = "".join(wordCopy)
            if word != guessWord and guessWord in wordSet:
                neighbors.add(guessWord)
    return neighbors

def findLadders(startWord, endWord):
    q = Queue()
    q.enqueue([startWord])
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        word = path[-1]
        if word == endWord:
            return path
        if word not in visited:
            visited.add(word)
            for neighbor in getNeighbors(word):
                newPath = path.copy()
                newPath.append(neighbor)
                q.enqueue(newPath)
    return None

print(findLadders("bacon", "happy"))
