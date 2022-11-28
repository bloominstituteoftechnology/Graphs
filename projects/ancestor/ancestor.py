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
        if node[1] in mapped_dict:
            mapped_dict[node[1]].add(node[0])
        else:
            mapped_dict[node[1]] = set()
            mapped_dict[node[1]].add(node[0])

def return_neighbors(node):
    if mapped_dict.get(node, '00') != '00':
        return mapped_dict[node]
    else:
        return None

def earliest_ancestor(ancestors, starting_node):
    map_array(ancestors)
    
    if mapped_dict.get(starting_node, '00') == '00':
        return -1
    
    stack = Stack()
    stack.push({
        'current_node': starting_node,
        'path': [starting_node]
    })

    visited = set()
    
    no_parents = False
    
    count = 0

    while stack.size() > 0:
        current_object = stack.pop()
        current_path = current_object['path']
        current_node = current_object['current_node']
        
        print(f"C_O {current_object}")
        
        if current_node not in visited:
            
            visited.add(current_node)
            if return_neighbors(current_node) == None:
                no_parents = True
                if stack.size() > 0:
                    if return_neighbors(stack.stack[-1]['current_node']) == None:
                        if current_node > stack.stack[-1]['current_node']:
                            return stack.stack[-1]['current_node']
                        else:
                            return current_node
                    
            if no_parents:
                print("")
                no_parents = False
                count += 1
            else:
                for neighbor in return_neighbors(current_node):
                    new_path = list(current_path)
                    print(current_path)
                    new_path.append(neighbor)
                    print(new_path)
                    stack.push({
                        'current_node': neighbor,
                        'path': new_path
                        })
                
                print(stack.stack)
                        
    
    return current_path[-1]
            
            