from collections import defaultdict


def earliest_ancestor(ancestors, starting_node):
    """
    The ancestors dataset must be formatted as a list of (parent, child) pairs,
    where each individual is assigned a unique integer identifier.

    Additional restrictions:
        - The input will not be empty.
        - There are no cycles in the input.
        - There are no "repeated" ancestors – if two individuals are connected,
        it is by exactly one path.
        - IDs will always be positive integers.
        - A parent may have any number of children.

    Given such a dataset and the ID of an individual in that dataset, this
    function returns their earliest known ancestor – the one at the farthest
    distance from the input individual. If there is more than one ancestor tied
    for "earliest", it returns the one with the lowest numeric ID. If the input
    individual has no known parents, the function returns -1.
    """
    # Re-format the ancestors dataset as a dictionary.
    # Key: child
    # Value: list of all known parents for that child
    parent_dict = defaultdict(list)
    for pair in ancestors:
        parent_dict[pair[1]].append(pair[0])

    # Special case for an individual with no known parent.
    if starting_node not in parent_dict:
        return -1

    def recursive_ancestor(child, level=0):
        """
        Helper function that recursively finds the earliest answer of an
        individual using our newly defined parent dictionary. Uses the 'level'
        argument to track the number of generations between the original
        child node and the ancestor under current examination. If the
        individual has no known parents, this function returns a tuple of the
        form (id, 0) - essentially, that individual is considered their own
        earliest ancestor.
        """
        nonlocal parent_dict

        # Base case: no earlier ancestors along this branch of the family tree.
        if child not in parent_dict:
            return (child, level)

        # Recursive case: find the earliest ancestor of each parent, then
        # compare. In a tie, return the ancestor with the lowest numeric ID.
        else:

            # Initialize a list to track earliest ancestors of parent nodes.
            candidates = []
            for parent in parent_dict[child]:

                # Increment the level once for each recursive call, which
                # corresponds to a generation.
                candidates.append(recursive_ancestor(parent, level + 1))

            # Comparison & return: sort first on level (descending), then on
            # ancestor id (ascending). Return the first result.
            return sorted(candidates, key=lambda x: (-x[1], x[0]))[0]

    # If we know the starting node has at least one parent, we can return just
    # the ancestor id from our helper function defined above.
    return recursive_ancestor(starting_node)[0]
