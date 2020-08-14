#
#Write a function that, given the dataset and the ID of an individual in the dataset,
#  returns their earliest known ancestor – the one at the farthest distance from the input individual.
#  If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
# If the input individual has no parents, the function should return -1.
import collections
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    new_parents_by_child = {}
    
    for parent, child in ancestors:
        if child in new_parents_by_child:
            
