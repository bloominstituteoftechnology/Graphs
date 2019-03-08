world.loadGraph(roomGraph)
player = Player("Name", world.startingRoom)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return (len(self.queue))


# FILL THIS IN
traversalPath = []

graph = {}

print("*****\n")

print(player.currentRoom.id)
print(player.currentRoom.getExits())

directions = ('n', 's', 'e', 'w')

inverseDirections = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


def traverseMap(player, direction=''):

    # Check if all rooms have been explored and stop if they have.
    if len(graph.keys()) == 500:
        return
    # While the map is not completely explored
    # If the room doesn't exist

    currentRoom = player.currentRoom.id

    if player.currentRoom.id not in graph:
            # Initialize in your room graph with '?' exits
        graph[player.currentRoom.id] = {}
        for exit in player.currentRoom.getExits():
            graph[player.currentRoom.id][exit] = '?'

    # If coming from another room
    if direction is not '':
        # find opposite direction of current travel
        opposite = inverseDirections[direction]
        # set prevRoom using Room method 'getRoomInDirection'
        prevRoom = player.currentRoom.getRoomInDirection(opposite)
        # Update the graph the entry for previous room
        graph[currentRoom][opposite] = prevRoom.id

    new_direction = '?'

    # If there is an unexplored exit in the current room (i.e. a '?' exit), travel in that direction
    for exit in player.currentRoom.getExits():
        if graph[currentRoom][exit] == '?':
            # if the current room has an unexplored exit set the new_direction to that exit
            new_direction = exit
            # travel there and append the current exit to the traversal path
            player.travel(exit)
            traversalPath.append(exit)
            # set new_room to the player's current room and set the previous room's exit to the new room
            new_room = player.currentRoom.id
            graph[currentRoom][exit] = new_room
            # Walk there
            traverseMap(player, exit)
            break

    # Else, find the nearest room using BFS with an unexplored exit and travel there
    # Set a travel_path
    travel_path = []

    if new_direction is '?':
        # Setup a new Queue with the currentRoom
        q = Queue()
        visited = set()
        q.enqueue([currentRoom])

        while q.size() > 0:
            # While there is something in the Queue take out the last item and set current room to the last item in path
            path = q.dequeue()
            currentRoom = path[-1]

            if currentRoom not in visited:
                visited.add(currentRoom)

                # If currentRoom has an unexplored exit
                if '?' in graph[currentRoom].values():
                    # Return path to that room and reset the queue
                    travel_path = path
                    q = Queue()
                    break

                for neighbor in graph[currentRoom].values():
                    # for every direction in the current room add it to the path to search through and add it to the queue
                    new_path = list(path)
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    for r in travel_path:
        # for every room in the travel path
        room = player.currentRoom.id
        g_keys = graph[room].keys()
        for d in g_keys:
            # For every room we walked along add the values that match to that room to our traversal path
            if graph[room][d] == r:
                player.travel(d)
                traversalPath.append(d)

    # Explore the map again now that we are at a room with an unexplored exit
    traverseMap(player)


traverseMap(player)


# print(graph)
print(traversalPath)
print("\n*****")


# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(
        f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
```
