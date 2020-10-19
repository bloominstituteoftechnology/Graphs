"""Given two words (begin_word and end_word), and a dictionary's word list, 
return the shortest transformation sequence from begin_word to end_word, such that:​
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
​
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
You may not remove or add extra letters
​
Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
​
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
​
beginWord = "hungry"
endWord = "happy"
None
"""
f = open('words.txt', 'r')
words = f.read().split("\n")  


all_words = set()
for word in words:
  all_words.add(word.lower())

def get_neighbors(current_word):
  # Should return a list of neighbors
  pass

  # Generate all possible "words" by replacing one letter at a time
    # check if any of those words are valid
    #  if they are valid append to a neighbors list


def find_path_bfs(start_word, end_word):
  queue = [ [start_word]]
  visited = set()

  while len(queue) > 0:
    # pop the latest word
    current_path = queue.pop()
    current_word = current_path[-1]

    if current_word not in visited:
      #compare if the current word is the end_word
      # return current path
      if current_word == end_word:
        return current_path
      visited.add(current_word)  

      for neighbor in get_neighbors(current_word):
        current_path.copy = list(current_path)
        current_path.copy.append(neighbor)  
        queue.append(current_path.copy)
  return None      
