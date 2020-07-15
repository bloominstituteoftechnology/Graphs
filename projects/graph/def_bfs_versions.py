def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
        # create an empty queue and enqueue A PATH to the starting vertex 
        q = Queue()
        q.enqueue([starting_vertex])
        # create a SET to store visited vertices
        visisted = set()

        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path (front or back?)
            current_path = q.dequeue()
            # Grab the last vertex from the PATH
            current_vertex = current_path[-1]
            
            # if that vertex has not been visited
            if current_vertex not in visisted:
                # check if it's the target
                if current_vertex == destination_vertex:
                    # if so, return path
                    return current_path
                # Mark as visited
                visisted.add(current_vertex)
                # add PATHs neighbors to the back of the queue
                neighbors = self.get_neighbors(current_vertex)
                for neighbor in neighbors:
                    # copy the PATH
                    current_path.append(neighbor)
                    # append neighbor to the back
                    q.enqueue(current_path)

def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # pass  # TODO
        # create an empty queue and enqueue a path to the starting vertex 
        q = Queue()
        # enqueue the starting path
        q.enqueue([starting_vertex])

        # empty set to store the visited vertices
        visited = set()

        # while the queue isn't empty
        while q.size() > 0:
        ## dequeue the first path
            current_path = q.dequeue()
            print("C1:", current_path)
        ## pop the last vertex from this path
            current_node = current_path[-1]
            print("C2:",current_node)
            print(visited)
            # print(current_node)
        ## if we haven't visited this node yet,
            if current_node not in visited:
        ## check if it's the target
                if current_node == destination_vertex:
                    print("THIS:", current_path)
                    return current_path
                    break
        ### else mark as visited
                else:
                    visited.add(current_node)
                    # print(f"Visited {current_node}")

        ### add path to neighbors to back of queue
                neighbors = self.get_neighbors(current_node)
        ### for each of the neighbors,
                for neighbor in neighbors:
        #### add to queue
                    current_path.append(neighbor)
                    print("path:", current_path)
                    q.enqueue(current_path)