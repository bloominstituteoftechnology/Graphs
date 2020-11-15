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

f = open('words.text', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

def get_neighbors(word):
    letters = ['a'- 'z']
    neighbors = set()
    # a neighbor is any word thats different by one letter 
    # and is inside the word list
    string_word = list(word)

    for i in range(len(string_word)):
        # swap each character witha a character from the letters list
        for letter in letters:
            new_word = list(string_word)
            # place new letter at current position in the word
            new_word[i] = letter
            # convert word back to a string
            new_word_string = "".join(new_word)

            if new_word_string != word and new_word_string in word_set:
                neighbors.add(new_word_string)

        return neighbors

    # take each leter in alphabet (26)
    # generate EVERY "combination" of characters
    # check that the word exists in word_list, and if it does
    # its a neighbor

    # return all neighbors

def find_word_path(begin_word, end_word):
    # BFS
    # Create a queue
    queue = Queue()
    # create a visited set
    visited = set()
    # add start word to queue (like a path)
    queue.enqueue([begin_word])
    # while queue not empty
    while queue.size() > 0
        # pop the current word off queue
        current_path = queue.dequeue()
        current_word = current_path[-1]
        # if word has not been visited:
        if current_word not in visited:
            if curent_word == end_word:
                return current_path
            # add it to the set
            visited.add(current_word)
            # add neighbors of current word to queue (like a path)
            for neighbor in self.get_neighbors(current_word)
                new_path = list()
                new_path.append(neighbor)
                queue.enqueue(new_path)
