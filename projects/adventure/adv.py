from room import Room
from player import Player
from world import World

import time
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

reverse_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


def traverse_graph(traversal_path=None, visited=None, next_room=None):
    # Initialize from starting room
    start = world.starting_room
    first_direction = start.get_exits()[0]
    visited = visited or {start.id: {x: '?' for x in start.get_exits()}}
    next_room = next_room or (start.id, first_direction,
                              start.get_room_in_direction(first_direction))
    if traversal_path is None:
        traversal_path = []

    # Helper function to find unvisited rooms upon reaching a dead-end

    def next_unvisited_room(starting_room):
        nonlocal visited, traversal_path
        queue = [[starting_room]]
        # Track rooms we've visited on this traversal to avoid infinite loops
        inner_visited = set()
        while len(queue) > 0:
            current_path = queue.pop(0)
            # Current room is the last item in the tuple
            # for the last entry in the path
            current_room = current_path[-1][-1]

            # Once we find a new room, update the traversal path and return the new room
            if current_room.id not in visited:
                [_, *skipped_rooms, new_room] = current_path
                # Direction is the 2nd item in the tuple
                traversal_path.extend([x[1] for x in skipped_rooms])
                return new_room

            inner_visited.add(current_room.id)
            # Perform a BFS of all unvisited rooms reachable from the current room
            potential_rooms = [(x, current_room.get_room_in_direction(x))
                               for x in current_room.get_exits()]
            for direction, room in potential_rooms:
                if room.id not in inner_visited:
                    queue.append(current_path +
                                 [(current_room.id,
                                   direction,
                                   room)]
                                 )

    while len(visited) < len(room_graph):
        # Extract info and update traversal path and visited graph
        prev_room, direction_moved, current_room = next_room
        traversal_path.append(direction_moved)
        visited[prev_room][direction_moved] = current_room.id

        # If we're in a room for the first time, mark as visited
        if current_room.id not in visited:
            visited[current_room.id] = {
                x: '?' for x in current_room.get_exits()}
        # Add path to previous room to known paths
        visited[current_room.id][reverse_direction[direction_moved]] = prev_room
        # If this room isn't a dead-end, queue up a random unvisited room next
        unvisited_directions = [
            dir_ for dir_, val in visited[current_room.id].items() if val == '?']
        if len(unvisited_directions) > 0:
            next_direction = random.sample(unvisited_directions, 1)[0]
            next_room = (
                current_room.id,
                next_direction,
                current_room.get_room_in_direction(next_direction)
            )
            # The "all paths" solution seems to have time complexity of O(4^n)
            # So it won't complete before the universe ends
            # If there are multiple paths, recurse
            # if len(unvisited_directions) > 0:
            #     for next_direction in unvisited_directions:
            #         traverse_graph([*traversal_path], {x:y for x,y in visited.items()}, (
            #             current_room.id,
            #             next_direction,
            #             current_room.get_room_in_direction(next_direction)
            #         ))

        # If we're at a dead-end, find the path to the next room and add it to the queue
        else:
            next_room = next_unvisited_room(
                (prev_room, direction_moved, current_room)
            )
    # if len(traversal_path) < 1000:
        # print(f"Traversed in {len(traversal_path)} steps")
    return traversal_path


# Keep trying until we get a traversal less than 960 steps long
start_time = time.time()
while True:
    traversal_path = traverse_graph()
    if len(traversal_path) < 960:
        break
print(f"Completed in {(time.time()-start_time):.3f}s")
# traversal_path = sorted(traversal_paths, key=len)[0]

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
