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
            path2 = self.extend_path(new_path)
            # print('path2', path2, path)
            # for item in path2:
            #     print(item)
            #     if isinstance(item,list):
            #         print('nested', item)
            #         paths.append(item)
                # else:
                #     print('non-nested', item)
                #     paths.append([item])
            paths.append(path2)
        return paths

    
    def find_genealogy(self, starting_node):
        path = [starting_node]
        genealogies = self.extend_path(path)
        for item in genealogies:
            # print('123', item)
            if isinstance(item,list):
                print('here', item)
            else:
                print('item', item)
        return genealogies


def earliest_ancestor(ancestors, starting_node):
    # create a graph of generations
    family_tree = Ancestors()

    for pair in ancestors:
        for generation in pair:
            family_tree.add_generation(generation)
        family_tree.add_relationship(pair[1], pair[0])
    
    genealogy = family_tree.find_genealogy(starting_node)

    print('**', genealogy)
    print('##', family_tree.generations)
    print('Hello', family_tree.extend_path([6,3]))
    # if genealogy:
    #     return genealogy[0]
    
    # return -1



test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))

# a1 = []
# a2 = [[10]]
# a1.extend(a2[0])
# print(a1)

