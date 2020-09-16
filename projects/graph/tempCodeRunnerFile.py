stack =Stack()
        stack.push({
            'current_vertex': starting_vertex,
            'path':[starting_vertex]
        })
        #create a set of vistited vertices
        visited_vertex = set()
        #while stack is not empty
        while stack.size()>0:
             #pop the current vetex
             current_obj = stack.pop()
             current_vertex = current_obj['current_vertex']
             current_path = current_obj['path']
             #get the neighbours for the current vertex
             for neighbour_vertex in self.get_neighbors(current_vertex):
                new_path =list(current_path)
                new_path.append(neighbour_vertex)
            #push the neighbour in the stack
                stack.push({
                'current_vertex': neighbour_vertex,
                'path' : new_path
              })