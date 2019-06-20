
def traverse():
    # Start with a visited set
    visited = set()
    # Declare an instance of Queue
    queue = Queue()
    # Get integers from Room.name
    room_name_list = player.currentRoom.name.split()
    room_name_list = [int(i) for i in room_name_list if i in letter_to_int_dict]
    # Add initial path to queue
    queue.enqueue(room_name_list)
    # While queue is not empty
    while queue.size() > 0:
        # Dequeue the first path
        path = queue.dequeue()
        # Grab the vertex from the end of the path
        vertex = path[-1]
        # If vertex not in visited
        if vertex not in visited:
            # Add vertex to visited set and to traversalPath
            visited.add(vertex)
            # For every vertex neighbor, add path of neighbor to the back of the queue
            for key in roomGraph[vertex][1]:
                # Copy the path
                path_copy = path.copy()
                print(path_copy)
                # Append neighbor to the back of the copy
                path_copy.append(roomGraph[vertex][1][key])
                # Append direction to the traversal path
                traversalPath.append(key)
                print(traversalPath)
                # Enqueue the copy
                queue.enqueue(path_copy)
