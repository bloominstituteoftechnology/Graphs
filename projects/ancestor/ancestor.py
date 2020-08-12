class Ancestors:
    def __init__(self):
        self.generations = {}

    def add_generation(self, generation_id):
        if generation_id not in self.generations:
            self.generations[generation_id] = set()

    def add_relationship(self, child, parent):
        if child in self.generations and parent in self.generations:
            self.generations[child].add(parent)
    
    def get_parents(self, child):
        if child in self.generations:
            return self.generations[child]
    

    # def get_ancestor_path(self, starting_node, path=None):
    #     if path is None:
    #         path = []
        
    #     path.append(starting_node)

    #     if len(self.get_parents(starting_node)) is 0:
    #         return path
        
    #     for p in self.get_parents(starting_node):
    #         return self.get_ancestor_path(p, path)

    def extend_path(self, path):
        node = path[-1]

        if len(self.get_parents(node)) is 0:
            return path
        
        paths = []
        for p in self.get_parents(node):
            new_path = list(path)
            new_path.append(p)
            # print('calling for', new_path)
            path2 = self.extend_path(new_path)
            new_items = []
            for item in path2:
                if isinstance(item,list):
                    # append nested items to the path directly
                    paths.append(item)
                else:
                    # group together non-nested items
                    new_items.append(item)
            if len(new_items) > 0:
                # print('new items', new_items)
                paths.append(new_items)
        # print('returning', paths, 'for', path)
        return paths

    
    def find_genealogy(self, starting_node):
        path = [starting_node]
        genealogies = self.extend_path(path)
        
        return genealogies
        
    # finds the longest path - does not work for tie
    # def find_genealogy(self, starting_node, path=None):
    #     if path is None:
    #         path=[starting_node]
    #     node = path[-1]

    #     if len(self.get_parents(node)) is 0:
    #         return path
        
    #     longest_path = path
    #     for p in self.get_parents(node):
    #         new_path = list(path)
    #         new_path.append(p)
    #         path2 = self.find_genealogy(starting_node, new_path)
    #         if len(path2) > len(longest_path):
    #             longest_path = path2
            
    #     return longest_path

def earliest_ancestor(ancestors, starting_node):
    # create a graph of generations
    family_tree = Ancestors()

    for pair in ancestors:
        for generation in pair:
            family_tree.add_generation(generation)
        family_tree.add_relationship(pair[1], pair[0])
    
    if len(family_tree.get_parents(starting_node)) is 0:
        return -1
    
    genealogy = family_tree.find_genealogy(starting_node)

    # print('**', starting_node, genealogy)
    # print('##', family_tree.generations)
    
    
    longest_ancestory = 0
    for item in genealogy:
        if len(item) > longest_ancestory:
            longest_ancestory = len(item)
    
    oldest_ancestors = []
    for item in genealogy:
        if len(item) == longest_ancestory:
            oldest_ancestors.append(item[-1])
    
    if len(oldest_ancestors) is 1:
        return oldest_ancestors[0]
    
    a = oldest_ancestors[0]
    for i in oldest_ancestors:
        if i < a:
            a = i
    return a



# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# print(earliest_ancestor(test_ancestors, 8))


