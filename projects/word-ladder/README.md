# Given two words (beginWord and endWord), and a dictionary's word list, return the shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

# Note:
# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Breakdown
# Shortest - BFS
# One letter at a time - vertexes
# Word list/words
# ReturnNone
# BeginWord and #EndWord
# No duplicates
# Same length
# Transformation sequence

# If we organize the word list in a graph
# with words as vertexes and edges between
# two words that are 1 letter different,
# then
# if we do a BFS from a BeginWord to EndWord
# the result path will be the shortest
# using the transformation sequence
