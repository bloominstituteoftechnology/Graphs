from room import Room
from player import Player
from world import World
from util import Stack
from util import Queue
import random
from ast import literal_eval



# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
#map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
#map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

print("travel", player.travel('n',True))
print("travel1", player.current_room.id)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
player_graph = {}

# , create a graph
# traverse the graph using dft
# keep track of the direction and the node you visited

visited = set()
s = Stack()
s.push(player)  # [player class, ]

print("start", player.current_room)
visited_new = set()

while s.size() > 0:
    player = s.pop()
    print("current room", player.current_room.id)
#     # get the directions to go to from the current room

    valid_directions = player.current_room.get_exits()

    if player.current_room.id not in visited:
        visited.add(player.current_room.id)
        directions_to_go_to = {}
        for direction in valid_directions:
            directions_to_go_to[direction] = '?'
    # {0: n: ?}
    # # add the directions to move and the room id to the player_graph {n: ?}
        player_graph[player.current_room.id] = directions_to_go_to
    # {0:{n:1, s, e, w}, 1:{n:?, s:0}}

    player_direction = player_graph[player.current_room.id]

    # {n: 1, s: ?, e: ?, w: ?}

    unexplored_routes = [
        key for key in player_direction if player_direction[key] == '?']
    #['n', 's']

    if len(unexplored_routes) > 0:
        key = random.choice(unexplored_routes)
        # key = 'n'
        print(
            f'key for room {player.current_room.id} is {key} with value {player_direction[key]}')
        if player_direction[key] == '?':

            player_direction[key] = player.current_room.get_room_in_direction(
                key).id
            traversal_path.append(key)
            # [n,]

            room = player.current_room.get_room_in_direction(key)
            new_player = Player(room)  # player class (1) which is n

            s.push(new_player)
            # [player-room 1]
            # {0: n:1, s, e , w}
    else:
        visited_bfs = set()

        q = Queue()

        q.enqueue(player)
        path = [player.current_room.id]

        while q.size() > 0:
            path = q.dequeue()
            player = path[-1]
           

            if player not in visited_bfs:
                visited_bfs.add(player)
                player_direction = player_graph[player] # {n:1,s:5,e:7, w:4}
                
                
                unexplored_routes =[key for key in player_direction if player_direction[key] == '?']
                if len(unexplored_routes) > 0:
                    s.push(player)
                    break

                neighbors = player_graph(player.current_room.id) #{n:1,e:7,w:3,s:5}
                # for key in neighbors:
                #     new_path.append(key, neighbors[key])
                #     new_path = list(path)
                #     new_path.append(neighbors[key])
        
                    #   room = player.current_room.get_room_in_direction(key)
                    #   new_player = Player(room)
                    # q.enqueue(new_path)


print("visited", visited)
print("traversal", traversal_path)
print(player_graph)


player.current_room.get_room_in_direction(key).id


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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
