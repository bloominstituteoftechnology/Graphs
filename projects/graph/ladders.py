# 1) How to solve almost any graph problem:
#     - What are your nodes?
#     - What are your edges?
#     - Where are the two nodes connected to each other?
#     - Are there connected components?
    
# 2) Build your graph OR define a get_neighbors function

# 3) Choose your graph algorithm and run 


#Given two words (begin_word, and end_word), and a dictionary's words list,
#return the shortest transfrotmation sequence from begin_word to end_word, such that:

#only one letter can be changed at a time
#each transformed word my exist in the word ist. Note that the begin_word is NOT a transformed word

from util import Stack, Queue 
import string
f = open('word.txt', 'r')
words = f.read().split('\n')
f.close

word_set = set()
for word in words:
    word_set.add(word.lower())

def get_neighbors(word):
    neighbors = []
    for i in range(len(word)):
        for alpha in string.ascii_lowercase:
            word_list = list(word)
            word_list = alpha
            maybe_neighbor = "".join(word_list)
            
            if maybe_neighbor in word_set and maybe_neighbor != word:
                neighbors.append(maybe_neighbor)
    return neighbors
    
    

def find_ladders(start_word, end_word):
    q = Queue()
    visited = set()
    
    q.enqueu([start_word])
    while q.size() > 0:
        current_path = q.dequeue()
        current_node = current_path[-1]
        
        if current_node == end_word:
            return current_path
        
        if current_node not in visited:
            neighbors = get_neighbors(current_node)
            
            for neighbor in neighbors:
                path_copy = list(current_path)
                path_copy.append(neighbor)
                
                q.enqueue(path_copy)
    
    

find_ladders("hit", "cog")