"""
Solving (Almost) Any Graphs Problem

0. Spot that you might use a graph to solve it
- Shortest path
- spot that there are things connected to other things

1. Describe the problem using graphs terminology
- What are my nodes here?
- What are my edges? aka when is there an edge, when is a node connected to another node? When not?

2. Build your graph, or write getNeighbors

3. Choose your fighter, traverse your graph


Given two words (begin_word and end_word), and a dictionary's word list, 
return the shortest transformation sequence from begin_word to end_word, such that:

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


0. Spot that we might use a graph: "shortest transformation sequence" is a lot like shortest path

1. Describe the problem using graphs terminology
- What are my nodes here?
--- words! if in the word list
--- letters??

- What are my edges? aka when is there an edge, when is a node connected to another node? When not?

--- two words are "connected" if they're just one letter different
---- in other words, all letters same, except one
---- and the same length!

2. Build your graph, or write getNeighbors

3. Choose your fighter, traverse your graph
BFS to get shortest
DFS/T to see how far we go
Combine them: DFS to find the target word, then BFS to select the shortest path
"""
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

# do it in one go, but not lowercase them: set(f.read().split())

# be able to access words
f = open('words.txt', 'r')
giant_list_of_words = f.read().split('\n')
word_set = set()
for word in giant_list_of_words:
    word_set.add(word.lower())

f.close()

# build graph, or write getNeighbors
## somehow we need to find all the neighbors of a word...

# for word in giant_list_of_words:
#     if word not in my_graph.vertices:
#         my_graph.add_node(word)
#         for other_word in giant_list_of_words:
#             if is_edge(word, other_word):
#                 my_graph.add_edge(word, other_word)

import string
# "sail"
# "aail", "bail", "cail", "dail"
# "sail", "sbil", "scil"
# O(26 * n)
# O( # of letters * Alphabet)
# ["bail", "dail", "sall", "hail", "soil"]

def getNeighbors(word):
    neighbors = []
# iterate over each letter of the word
    for letter in range(len(word)):
## for each letter, swap out a letter of the alphabet
        for other_letter in string.ascii_lowercase:
            ## swap them out
            ### turn it into a list
            word_now_a_list = list(word)
            word_now_a_list[letter] = other_letter
            # turn back into a string
            maybe_neighbor = ""
            for l in word_now_a_list:
                maybe_neighbor += l

### check if the resulting "word" is in the word list/set
            if maybe_neighbor in word_set:
#### if so, it's a neighbor
##### append to a list of neighbors
                neighbors.append(maybe_neighbor)

    return neighbors


# use BFS
def bfs(start_node, target_node):
    q = Queue()

    visited = set()

    q.enqueue([start_node])

    while q.size() > 0:

        current_path = q.dequeue()

        current_node = current_path[-1]

        if current_node == target_node:
            return current_path

        if current_node not in visited:
            visited.add(current_node)

            neighbors = getNeighbors(current_node)

            for neighbor in neighbors:

                path_copy = list(current_path)

                path_copy.append(neighbor)

                q.enqueue(path_copy)

begin_word = "hit"
end_word = "cog"

print(bfs(begin_word, end_word))

begin_word = "sail"
end_word = "boat"

print(bfs(begin_word, end_word))