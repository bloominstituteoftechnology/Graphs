

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        return self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    dict_ancestor = {}
    stack = Stack()
    visited = set()
    longest_path = []

    for i, x in enumerate(ancestors):
        dict_ancestor[i] = x

    for i, v in dict_ancestor.items():
        if v[1] is starting_node:
            stack.push([i])


    size = stack.size()

    if stack.size() > 0:
        while size > 0:
            # print(dict_ancestor)
            # print(stack.stack)
            current_node = stack.pop()
            single_node = current_node[-1]
            size = stack.size()

            if single_node not in visited:
                # print("sn not in visited")
                visited.add(single_node)
                parent = dict_ancestor[single_node][0]
                # print(parent)

                for i, v in dict_ancestor.items():
                    if v[1] is parent:
                        new_path = current_node[:]
                        new_path.append(i)
                        stack.push(new_path)
                        # print("new_path:", new_path)

                        if len(new_path) > len(longest_path):
                            longest_path = new_path
                    elif i == len(dict_ancestor) - 1:
                        longest_path = current_node


                size = stack.size()

        final_answer = (dict_ancestor[longest_path[-1]][0])
        return final_answer 
    else:
        return -1