from room import Room
from player import Player
from world import World
import collections
from ast import literal_eval
import random


seeds = []
traversal_path = []
reverse = {"n": "s", "s": "n", "e": "w", "w": "e"}
maze_graph = {}
directions = ["n", "s", "e", "w"]
keep_going = True
rando = 511483


count = 1

while keep_going:
    # Load world
    world = World()
    # seed = random.randint(1, 1600000)
    # You may uncomment the smaller graphs for development and testing purposes.
    # map_file = "maps/test_line.txt"
    # map_file = "maps/test_cross.txt"
    # map_file = "maps/test_loop.txt"
    # map_file = "maps/test_loop_fork.txt"
    map_file = "maps/main_maze.txt"

    # Loads the map into a dictionary
    room_graph=literal_eval(open(map_file, "r").read())
    # room_graph = {
    #   0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
    #   1: [(3, 6), {'s': 0, 'n': 2, 'e': 12, 'w': 15}],
    #   2: [(3, 7), {'s': 1}],
    #   3: [(4, 5), {'w': 0, 'e': 4}],
    #   4: [(5, 5), {'w': 3}],
    #   5: [(3, 4), {'n': 0, 's': 6}],
    #   6: [(3, 3), {'n': 5, 'w': 11}],
    #   7: [(2, 5), {'w': 8, 'e': 0}],
    #   8: [(1, 5), {'e': 7}],
    #   9: [(1, 4), {'n': 8, 's': 10}],
    #   10: [(1, 3), {'n': 9, 'e': 11}],
    #   11: [(2, 3), {'w': 10, 'e': 6}],
    #   12: [(4, 6), {'w': 1, 'e': 13}],
    #   13: [(5, 6), {'w': 12, 'n': 14}],
    #   14: [(5, 7), {'s': 13}],
    #   15: [(2, 6), {'e': 1, 'w': 16}],
    #   16: [(1, 6), {'n': 17, 'e': 15}],
    #   17: [(1, 7), {'s': 16}]
    # }

    world.load_graph(room_graph)
    # Print an ASCII map
    # world.print_rooms()
    player = Player(world.starting_room)

    # Helper function to add starting room
    def starting_room():
        direction_dict = {}
        room = player.current_room
        exits = player.current_room.get_exits()
        for way_out in exits:
            direction_dict[way_out] = "?"
        maze_graph[room.id] = direction_dict
        print(maze_graph)

    # Helper function to move and explore next room, works with first solution and 2nd pass recursive solution
    def explore(direction):
        direction_dict = {}
        current = player.current_room.id
        room = player.current_room.get_room_in_direction(direction)
        player.travel(direction)
        maze_graph[current][direction] = room.id
        if room.id not in maze_graph:
            for way_out in room.get_exits():
                some_room = room.get_room_in_direction(way_out)
                if some_room.id not in maze_graph:
                    direction_dict[way_out] = "?"
                elif way_out is reverse[direction]:
                    direction_dict[way_out] = current
                elif maze_graph[some_room.id][reverse[way_out]] is "?":
                    maze_graph[some_room.id][reverse[way_out]] = room.id
            maze_graph[room.id] = direction_dict
        traversal_path.append(direction)

    # Revised helper function to map current room in maze graph
    def explore2():
        direction_dict = {}
        for way_out in player.current_room.get_exits():
            some_room = player.current_room.get_room_in_direction(way_out)
            if some_room.id in maze_graph:
                direction_dict[way_out] = some_room.id
            else:
                direction_dict[way_out] = "?"
        maze_graph[player.current_room.id] = direction_dict

    # Helper function to move and add move to traversal path, as well as update previous rooms direction
    def move(direction):
        room = player.current_room
        player.travel(direction)
        traversal_path.append(direction)
        maze_graph[room.id][direction] = player.current_room.id

    # When current room has no unexplored paths, helper bfs function to find nearest "?" and returns path to it
    def closest_unexplored_path(room_id):
        queue = collections.deque([])
        path = []
        queue.append([(room_id, None)])
        checked_rooms = set()
        while queue:
            path = queue.popleft()
            room_tuple = path[-1]
            for direction, room in maze_graph[room_tuple[0]].items():
                if room not in checked_rooms:
                    shortest = list(path)
                    shortest.append((room, direction))
                    checked_rooms.add(room)
                    queue.append(shortest)
                    if room is "?":
                        shortest.pop(0)
                        path = [item[1] for item in shortest]
                        return path
        return []

    # First naive iterative solution
    def complete_maze(start):
        stack = collections.deque([])
        stack.append(start)
        starting_room()
        while stack:
            print(f"Length of maze graph: {len(maze_graph.keys())}")
            if len(maze_graph.keys()) is len(room_graph.keys()):
                return 
            direction = stack.pop()
            room = player.current_room
            next_room = room.get_room_in_direction(direction)
            print(f"Players Current Room: {player.current_room.id}")
            exits = set(room.get_exits())
            if next_room:
                explore(direction)
                print(f"Players Current Room: {player.current_room.id}")
                stack.append(direction)
            if not stack:
                for way_out in exits:
                    if maze_graph[room.id][way_out] is "?":
                        explore(way_out)
                        print(f"Players Current Room: {player.current_room.id}")
                        stack.append(way_out)
                        break
            if not stack:
                path_to_unexplored = closest_unexplored_path(player.current_room.id)
                for i in range(len(path_to_unexplored)):
                    explore(path_to_unexplored[i])
                    if i is len(path_to_unexplored) - 1:
                        stack.appendleft(path_to_unexplored[i])
        print(f"Length of maze graph: {len(maze_graph.keys())}")
    
    # Second pass recursive solution, completes in 1008 moves everytime
    def complete_maze2(direction):
        if len(maze_graph) is 0:
            starting_room()
        if len(maze_graph) is len(room_graph):
            return
        if player.current_room.get_room_in_direction(direction):
            explore(direction)
            print(f"Players Current Room: {player.current_room.id}")
            return complete_maze2(direction)
        if not player.current_room.get_room_in_direction(direction):
            for way_out in player.current_room.get_exits():
                if maze_graph[player.current_room.id][way_out] is "?":
                    explore(way_out)
                    print(f"Players Current Room: {player.current_room.id}")
                    return complete_maze2(way_out)
                else:
                    path_to_unexplored = closest_unexplored_path(player.current_room.id) 
                    for i in range(len(path_to_unexplored)):
                        explore(path_to_unexplored[i])
                        print(f"Players Current Room: {player.current_room.id}")  
                        if i is len(path_to_unexplored) - 1:
                            return complete_maze2(path_to_unexplored[i]) 

    # Optimized iterative solution, best so far is maze complete in 954 moves
    # Good seeds: 915, 6593, 9738, 34226, *BEST SO FAR* 132967
    def complete_maze3(seed):
        stack = collections.deque([])
        random.seed(seed)
        directions = ["n", "s", "e", "w"]
        start = random.choice(directions)
        stack.append(start)
            
        while len(maze_graph) is not len(room_graph):
            if stack:
                explore2()
                direction = stack.pop()
                move(direction)
            explore2()
            paths = []
            for way_out in player.current_room.get_exits():
                if maze_graph[player.current_room.id][way_out] is "?":
                    paths.append(way_out)
            if len(paths) > 0:
                choice = random.choice(paths)
                move(choice)
            else:
                path_to_unexplored = closest_unexplored_path(player.current_room.id)
                if len(path_to_unexplored) is 0:
                    return 
                for i in path_to_unexplored:
                    move(i)

    # Optimized recursive solution, best so farn is maze complete in 963 moves
    # Good Seeds: 504517, 511483
    def complete_maze4(seed, direction=None):
        if len(maze_graph) is len(room_graph):
            return
        if len(maze_graph) is 0:
            directions = ["n", "s", "e", "w"]
            random.seed(seed)
            start = random.choice(directions)
            explore2()
            move(start)
            explore2()
        if direction:
            move(direction) 
            explore2()
        paths = []
        for way_out in player.current_room.get_exits():
            if maze_graph[player.current_room.id][way_out] is "?":
                paths.append(way_out)
        if len(paths) > 0:
            choice = random.choice(paths)  
            return complete_maze4(seed ,choice)
        else:
            path_to_unexplored = closest_unexplored_path(player.current_room.id)
            for i in range(len(path_to_unexplored)):
                if i is len(path_to_unexplored) - 1:
                    return complete_maze4(seed, path_to_unexplored[i])
                move(path_to_unexplored[i])

    # Fill this out with directions to walk
    # traversal_path = ['n', 'n']
    
    # complete_maze2("n")
    # complete_maze3(seed)
    complete_maze4(rando)

    # TRAVERSAL TEST
    visited_rooms = set()
    player.current_room = world.starting_room
    visited_rooms.add(player.current_room)
    for move in traversal_path:
        player.travel(move)
        visited_rooms.add(player.current_room)
    if len(visited_rooms) == len(room_graph):
        x = 3
        # print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
    else:
        print("TESTS FAILED: INCOMPLETE TRAVERSAL")
        print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")
    
    if len(traversal_path) < 954:
        print(f"Seed {rando} for {len(traversal_path)} moves")
        print(f"*** End Of Loop *** Last Ran is Seed: {rando} completed in {len(traversal_path)} moves")
        seeds.append((rando, len(traversal_path)))
        break
    
    if count % 1000 is 0:
        print(f"Count: {count}")
    
    if len(traversal_path) < 963:
        print(f"Seed {rando} for {len(traversal_path)} moves")
        seeds.append((rando, len(traversal_path)))
        
    # if count > 1000:
    #     print(f"*** End Of Loop *** Last Ran is Seed: {rando} completed in {len(traversal_path)} moves")
    #     break
    
    count += 1
    rando += 1
    
    traversal_path = []
    maze_graph = {}
print(seeds)

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
