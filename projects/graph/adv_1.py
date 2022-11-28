traversal_path = []

visited = {} # we can use a dictionary here with
            # keys being rooms we visited, values being a dictionary of exits

# will need a way to get back. Log it, and a dictionary to translate the reverse
reverse_direction = {"n": "s", "s": "n", "e": "w", "w": "e"}

# Let's start with a modified BFT  function to explore the graph
def breadth_first_traversal(visited, starting_room):
    """
    Takes a graph of visited rooms and finds a route after a dead end
    Seek a room with ? exits
    """
    q = Queue()
    visited = {}
    path_to_unexplored = []
    q.enqueue([starting_room])

    while q.size() > 0:
        path = q.dequeue()
        latest_room = path[-1]
        if latest_room not in visited:
            visited[latest_room] = {}

            # check each direction to see if you have unexplored options
            for direction in visited[latest_room]:
                if visited[latest_room][direction] == "?":
                    return path
                # else get the directions you can travel and queue it up to explore back
                else:            
                    path_to_unexplored.append(direction)
                    next_room = visited[latest_room][direction]

                    # use a copy of paths so we can explore alt routes
                    path_copy = path.copy()
                    path_copy.append(next_room)
                    # add it to the q and we can look at the latest room
                    q.enqueue(path_copy)

while len(visited) < len(room_graph): # should be 500 rooms
    current_room = player.current_room.id

    if current_room not in visited: # remember, this visited is a dictionary of dicts
        visited[current_room] = {} # initialize the room
        for direction in player.current_room.get_exits():
            visited[current_room][direction] = "?" # set that direction intially to ?

    for path in visited[current_room]:
        if path not in visited[current_room]:
            break

        if visited[current_room][path] == "?":
            exit_path = path
            if exit_path:
                traversal_path.append(exit_path)
                player.travel(exit_path)
                
                next_room = player.current_room.id
                if next_room not in visited: # initialize just like above
                    visited[next_room] = {}
                    for direction in player.current_room.get_exits():
                        visited[current_room][direction] = "?"

            visited[current_room][exit_path] = next_room
            # set the reverse path as known
            visited[next_room][reverse_direction[exit_path]] = current_room
            current_room = next_room

    # Now that we explored all ?s
    paths = breadth_first_traversal(visited, current_room)
    if paths is not None:
        for room_number in paths:
            for room in visited[current_room]:
                if visited[current_room][room] == room_number:
                    traversal_path.append(room)
                    player.travel(room)
    current_room = player.current_room.id