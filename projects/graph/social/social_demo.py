#!/usr/bin/python

"""
Demonstration of Graph functionality.
"""

from sys import argv

from social import User, SocialGraph

# {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }

# {
#     '0': {'1', '3'},
#     '1': {'0', '4'},
#     '2': set(),
#     '3': {'0', '5'}
#     '4': {'0', '1'}
#     '5': {'0', '3'}
# }

        # self.vertices = {
        #                   "A": {"B"},
        #                   "B": {"C", "D"},
        #                   "C": {"E"},
        #                   "D": {"F", "G"},
        #                   "E": {"C"},
        #                   "F": {"C"},
        #                   "G": {"A", "F"}
        #                 }

def main():
  social = SocialGraph()
  # user = User()  # Instantiate your graph
    # graph.add_vertex('0')
    # graph.add_vertex('1')
    # graph.add_vertex('2')
    # graph.add_vertex('3')
    # # graph.add_vertex('3')     # checked if multiple values would be added
    # graph.add_edge('0', '1')
    # graph.add_edge('0', '3')
    # # graph.add_edge('0', '4') # raise IndexError("No vertex")
    # print(graph.vertices)


if __name__ == '__main__':
    # TODO - parse argv
    # main(sys.argv[1:])
    main()