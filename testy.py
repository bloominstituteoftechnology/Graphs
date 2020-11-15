class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

mapped_dict = {}

def map_array(array):
    for node in array:
        if node[0] in mapped_dict:
            mapped_dict[node[0]].add(node[1])
        else:
            mapped_dict[node[0]] = set()
            mapped_dict[node[0]].add(node[1])

def return_neighbors(node):
    return mapped_dict[node]

def earliest_ancestor(ancestors, starting_node):
    # find the ancestor
    the_ancestor = None
    for ancestor in mapped_dict:
        print(mapped_dict[ancestor])
        if mapped_dict[ancestor] == {starting_node}:
            print(mapped_dict[ancestor])
            the_ancestor = ancestor
            
    # depth first search / traversal
    stack = Stack()
    stack.push({
        'current_node': the_ancestor,
        'path': [the_ancestor]
    })

    visited = set()

    while stack.size() > 0:
        current_object = stack.pop()
        current_path = current_object['path']
        current_node = current_object['current_node']
        
        if current_node not in visited:
            
            visited.add(current_node)
            
            for neighbor in return_neighbors(current_node):
                new_path = list(current_path)
                print(current_path)
                print(new_path)
                new_path.append(neighbor)
                stack.push({
                    'current_node': neighbor,
                    'path': new_path
                    })
            
            
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]   
map_array(test_ancestors)
print(mapped_dict)
earliest_ancestor(test_ancestors, 1)
            