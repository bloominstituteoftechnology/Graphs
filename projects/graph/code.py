from util import Stack, Queue
import string

# MONDAY CODE CHALLENGE
# ------------------------------------------------------
# Print out all of the strings in the following array in alphabetical order, each on a separate line:

test = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'

# STRETCH
# ------------------------------------------------------
# Print out all of the strings in the following array in alphabetical order sorted by the middle letter of each string, each on a separate line. If the word has an even number of letters, choose the later letter, i.e. the one closer to the end of the string.

# function to use as the key for sorting
def middle(s):
    # find the middle letter of the string
    middle = len(s) // 2

    # find the letter at the index of middle
    letter = s[middle]

    return letter.lower()

# function to sort the array
def sort_alphabetical(S):
    # S.sort()
    S.sort(key=middle)

    # iterate through the list of strings
    for i in S:
        print(i)

sort_alphabetical(test)

# WORD LADDER PROBLEM
# ------------------------------------------------------
word_set = set()

with open("words.txt") as f:
    for word in f: # for each line in the file
        word_set.add(word.strip().lower())

def get_neighbors(word):
    neighbors = []
    word_letters = list(word)

    for i in range(len(word_letters)):
        for letter in list(string.ascii_lowercase):
            # make a copy of the word
            temp_word = list(word_letters)

            # substitute the letter in the copied word
            temp_word[i] = letter

            # make it a string
            temp_word_str = "".join(temp_word)

            # if it's a real word, add it to the returned set
            if temp_word_str != word and temp_word_str in word_set: # time = O(1)
                neighbors.append(temp_word_str)

    return neighbors

def get_neighbors_2(word):
    def word_diff_by_1(w1, w2):
        if len(w1) != len(w2):
            return False

        diff_count = 0

        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff_count += 1

        return diff_count == 1
    
    neighbors = []

    for word2 in word_set:
        if word_diff_by_1(word, word2):
            neighbors.append(word2)

    return neighbors

# get_neighbors = get_neighbors_2

def find_word_ladder(start_word, end_word): # BFS
    visited = set()

    q = Queue()

    q.enqueue([start_word])

    while q.size() > 0:
        path = q.dequeue()

        v = path[-1]

        if v not in visited:
            visited.add(v)

            if v == end_word:
                return path
            
            for neighbor in get_neighbors(v):
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    # if this is reached, it means the path was not found
    return None

print(find_word_ladder("sail", "boat"))