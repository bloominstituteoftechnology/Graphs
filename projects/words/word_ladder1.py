# Given two words (begin_word and end_word), and a dictionary's word list, 
# return the shortest transformation sequence from begin_word to end_word, such that:

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

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

# create a set of words, for easy lookup
words_set = set()
for word in words:
    words_set.add(word)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def get_neighbors(word):
    neighbors = []
    # for each letter in word
    list_of_chars = list(word)
    for i in range(len(list_of_chars)):
        # change that letter with every letter of alphabet
        for letter in alphabet:
            new_word = list(list_of_chars)
            new_word[i] = letter
            # check if the new word exists in our word_set
            new_word_string = "".join(new_word)
            if (new_word_string != word and new_word_string in words_set):
                # if yes, add the word as a neighbor
                neighbors.append(new_word_string)
    # return a list of neighbors
    return neighbors


def find_path(begin_word, end_word):
    visted = set()
    words_to_visit = Queue()
    words_to_visit.enqueue([begin_word])
    while words_to_visit.size() > 0:
        # remove the current vertex and path from queue
        path = words_to_visit.dequeue() 
        current_word = path[-1]
        # make sure we havent visited this word
        if current_word not in visted:
            # add to visited
            visted.add(current_word)
            # check if this current_word is our target
            if current_word == end_word:
                return path
            # otherwise, find all neighbors and create new paths
            for neighbor in get_neighbors(current_word):
                path_copy = list(path)
                path_copy.append(neighbor)
                words_to_visit.enqueue(path_copy)
            

begin_word = "hit"
end_word = "cog"
print(find_path(begin_word, end_word))
# return: ['hit', 'hot', 'cot', 'cog']

begin_word = "sail"
end_word = "boat"
print(find_path(begin_word, end_word))
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

