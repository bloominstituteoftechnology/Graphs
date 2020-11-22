# read words in from a file

import string

word_set = set()
with open("words.txt", "r") as f:
    for word in f:
        word_set.add(word.strip().lower())

words_by_length = {}
for w in word_set:
    l = len(w)

    if l not in words_by_length:
        words_by_length[l] = []

    words_by_length[l].append(w)


def get_neighbors(word):
    neighbors = []
    word_letters = list(word)
    for i in range(len(word_letters)):
        for letter in list(string.ascii_lowercase):
            # make a copy or word
            temp_word = list(word_letters)
            # substitute the letter into the word copy
            temp_word[i] = letter
            # make it a string
            temp_word_str = "".join(temp_word)
            # if it is a real word, add it to the return set
            if temp_word_str != word and temp_word_str in word_set:
                neighbors.append(temp_word_str)


def get_neighbors2(word):

    def word_diff_by_1(w1, w2):
        if len(w1) != len(w2):
            return False
        diff_count = 0

        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff_count += 1

        return diff_count == 1

    neighbors = []

    for word2 in words_by_length[len(word)]:
        if word_diff_by_1(word, word2):
            neighbors.append(word2)
    return neighbors
    # look for words of same length

    # if they differ by one letter, add to the return set


def find_word_ladder(begin_word, end_word):
    visited = set()
    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        last_word = path[-1]

        if last_word not in visited:
            visited.add(last_word)

            if last_word == end_word:
                return path

            for neighbor in get_neighbors(last_word):
                path_copy = path + [neighbor]
                q.enqueue(path_copy)

    # If we get here and haven't found it:
    return None
