from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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
        return len(self.queue)

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

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "maps/test_loop.txt"
map_file = "projects/adventure/maps/test_loop_fork.txt"
# map_file = "projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Global variables
player_starting_room = player.current_room
stack = Stack()
queue = Queue()
visited = {}
bfs_visited = {}
path_taken = []
opposite_dir_dict = {'n' : 's', 'e' : 'w', 'w' : 'e', 's' : 'n'}
first = True

def get_oposite_direction():
    if path_taken[-1] == 'n':
        return 's'
    elif path_taken[-1] == 's':
        return 'n'
    elif path_taken[-1] == 'e':
        return 'w'
    elif path_taken[-1] == 'w':
        return 'e'

def get_random_course(room):
    # get random direction to start traversing
    random_array = room.get_exits()
    random.shuffle(random_array)
    going_to = room.get_room_in_direction(random_array[-1])
    
    return (going_to, random_array[-1])

def room_exits(room):
    exits = room.get_exits()

    # if the len of exits is greater than one we have not reached the end of the path 
    exits_string ='nswe'
    if len(exits) > 1:
        for x in exits_string:
            if x not in exits:
                visited[room.id][x][0] = None
                visited[room.id][x][1] = None

        # remove the direction in which we just came from so that we don't repeat ourselves
        # exits.remove(get_oposite_direction())

        # add it to the dictionary for the previous direction as the previous room
        visited[room.id][get_oposite_direction()][0] = room.get_room_in_direction(get_oposite_direction())
        visited[room.id][get_oposite_direction()][1] = visited[room.id][get_oposite_direction()][0].id

        # loop through the exits until finding an unexplored path
        for x in exits:
            if visited[room.id][x][0] == '?':
                return (False, x)

        # if you cannot find an unexplored path then it is a room that has already been visited and needs to do a bfs to find another room to visit
        return 'noQuestionMarks'

    # we have reached the end of a path 
    else:
        for x in exits_string:
            if x not in exits:
                visited[room.id][x][0] = None
        return(True, exits[0])


def get_room_status(room):
    for exits in visited[room.id]:
        if visited[room.id][exits][0] == '?':
            return True
    
    return False

def afterReturnExits(exits):
    


def traverseWorld():
    # creating dict entry for starting room
    visited[player_starting_room.id] = {'n': ['?',''], 's': ['?',''], 'w': ['?',''], 'e' : ['?','']}

    # get random room to start traversing
    starting_route = get_random_course(player_starting_room)

    # get the next room and move the player there
    going_to_room = starting_route[0]

    # get the direction were going and append it to the path
    direction_to = starting_route[1]
    visited[player_starting_room.id][direction_to][0] = going_to_room
    visited[player_starting_room.id][direction_to][1] = going_to_room.id
    path_taken.append(direction_to)
    player.travel(direction_to)

    result = traverse_path(player.current_room)
    return result


def traverse_path(room):
    stack.push(room)
    while stack.size() > 0:
        current_room = stack.pop()

        if current_room.id not in visited or get_room_status(current_room):
            if current_room.id not in visited: 
                visited[current_room.id] = {'n': ['?',''], 's': ['?',''], 'w': ['?',''], 'e' : ['?','']}
            
            exits = room_exits(current_room)

            # in the case that there is no exits that it can travel that have yet to be explored it will return none
            if exits == 'noQuestionMarks':
                # We need to do a bfs in order to find another room that has question marks because 
                # we have hit a room after bf-sing that has not question marks
                path = find_unexplored_room(player.current_room)
                
                if path == None:
                    return path_taken

                # CHECK IF PATH IS NOT EQUAL TO THE PLAYERS CURRENT ROOM
                if path[-1] != player.current_room:
                    # REMOVE THE CURRENT ROOM FROM THE PATH 
                    path.remove(player.current_room)
                    # CONVERT THE LIST TO A PATH
                    for room in path:
                        for direct in visited[player.current_room.id]:
                            room_to_go_to = player.current_room.get_room_in_direction(direct)
                            if room_to_go_to == room:
                                player.travel(direct)
                                path_taken.append(direct)
                                break

                    # LOOK FOR THE DIRECTION WITH THE QUESTION MARK
                    for x in visited[player.current_room.id]:
                        if visited[player.current_room.id][x][0] == '?':
                            room_going_to = player.current_room.get_room_in_direction(x)
                            stack.push(room_going_to)

                            # setting our current rooms dictionary correctly with the room we are heading to 
                            visited[player.current_room.id][x][0] = room_going_to
                            visited[player.current_room.id][x][1] = visited[player.current_room.id][x][0].id

                            # need to add the direction to the bfs visited that we just went


                            # setting the room in which were headings previous direction to the current room
                            # visited[room_going_to][x][0] = player.current_room
                            # visited[room_going_to][x][1] = visited[room_going_to][x][0].id
                            # if len(path_taken) > 33:
                            #     print("ok")
                            player.travel(x)
                            path_taken.append(x)
                            # # TRAVEL THE PATH
                            # travel_path_player(path)

                            break

                # PATH IS EQUAL TO CURRENT ROOM
                else:
                    # LOOK FOR THE DIRECTION WITH THE QUESTION MARK
                    for x in visited[player.current_room.id]:
                        if visited[player.current_room.id][x][0] == '?':
                            room_going_to = player.current_room.get_room_in_direction(x)
                            stack.push(room_going_to)

                            # setting our current rooms dictionary correctly with the room we are heading to 
                            visited[player.current_room.id][x][0] = room_going_to
                            visited[player.current_room.id][x][1] = visited[player.current_room.id][x][0].id

                            # need to add the direction to the bfs visited that we just went


                            # setting the room in which were headings previous direction to the current room
                            # visited[room_going_to][x][0] = player.current_room
                            # visited[room_going_to][x][1] = visited[room_going_to][x][0].id
                            # if len(path_taken) > 33:
                            #     print("ok")
                            player.travel(x)
                            path_taken.append(x)
                            # # TRAVEL THE PATH
                            # travel_path_player(path)

                            break

        
            # if we have not reached the end of our path do this
            elif exits[0] == False:
                # add that direction to the path 
                path_taken.append(exits[1])
                # move your player if it's a place he has not yet been
                player.travel(exits[1])

                # add the room to the dictionaries direction
                visited[current_room.id][exits[1]][0] = player.current_room
                visited[current_room.id][exits[1]][1] = player.current_room.id 

                # add the room to the stack
                stack.push(player.current_room)


            # if we have reached the end do this
            else:
                if current_room.id == 285:
                    print("")
                # we append the move to the next room that's not the end of the path to our path taken
                path_taken.append(exits[1])
                # we then add the direction to the bfs visited so that it will not go back that way
                bfs_visited[current_room.id] = [exits[1]]
                # we then travel to the room that's not the end of the path
                player.travel(exits[1])
                # modify the current rooms dictionary to accomadate the move
                visited[current_room.id][exits[1]][0] = player.current_room
                visited[current_room.id][exits[1]][1] = player.current_room.id

                # we then add the current room we just arrived in (player's current room) to the bfs dict
                # making sure we do not return to the room we just came from
                # by adding the direction opposite of what we just moved.
                if player.current_room.id not in bfs_visited:
                    bfs_visited[player.current_room.id] = [get_oposite_direction()]

                # else:
                #     bfs_visited[player.current_room.id].append(get_oposite_direction())
                


                # here instead of traveling to the next room we need to just find a new room from our current room
                path = find_unexplored_room(player.current_room)
                if path == None:
                    return path_taken

                # CHECK IF PATH IS NOT EQUAL TO THE PLAYERS CURRENT ROOM
                if path[-1] != player.current_room:
                    # REMOVE THE CURRENT ROOM FROM THE PATH 
                    path.remove(player.current_room)
                    # CONVERT THE LIST TO A PATH
                    for room in path:
                        for direct in visited[player.current_room.id]:
                            room_to_go_to = player.current_room.get_room_in_direction(direct)
                            if room_to_go_to == room:
                                player.travel(direct)
                                path_taken.append(direct)
                                break


                    

                    # LOOK FOR THE DIRECTION WITH THE QUESTION MARK
                    for x in visited[player.current_room.id]:
                        if visited[player.current_room.id][x][0] == '?':
                            room_going_to = player.current_room.get_room_in_direction(x)
                            stack.push(room_going_to)

                            # setting our current rooms dictionary correctly with the room we are heading to 
                            visited[player.current_room.id][x][0] = room_going_to
                            visited[player.current_room.id][x][1] = visited[player.current_room.id][x][0].id

                            # need to add the direction to the bfs visited that we just went


                            # setting the room in which were headings previous direction to the current room
                            # visited[room_going_to][x][0] = player.current_room
                            # visited[room_going_to][x][1] = visited[room_going_to][x][0].id
                            # if len(path_taken) > 33:
                            #     print("ok")
                            player.travel(x)
                            path_taken.append(x)
                            # # TRAVEL THE PATH
                            # travel_path_player(path)

                            break

                # PATH IS EQUAL TO CURRENT ROOM
                else:
                    # LOOK FOR THE DIRECTION WITH THE QUESTION MARK
                    for x in visited[player.current_room.id]:
                        if visited[player.current_room.id][x][0] == '?':
                            room_going_to = player.current_room.get_room_in_direction(x)
                            stack.push(room_going_to)

                            # setting our current rooms dictionary correctly with the room we are heading to 
                            visited[player.current_room.id][x][0] = room_going_to
                            visited[player.current_room.id][x][1] = visited[player.current_room.id][x][0].id

                            # need to add the direction to the bfs visited that we just went


                            # setting the room in which were headings previous direction to the current room
                            # visited[room_going_to][x][0] = player.current_room
                            # visited[room_going_to][x][1] = visited[room_going_to][x][0].id
                            # if len(path_taken) > 33:
                            #     print("ok")
                            player.travel(x)
                            path_taken.append(x)
                            # # TRAVEL THE PATH
                            # travel_path_player(path)

                            break

                
                        

def find_unexplored_room(room):
    queue.queue = []
    queue.enqueue([room])
    path = []
    rooms = []
    direction_boi = None
    

    while queue.size() > 0:
        path = queue.dequeue()
        current_location = path[-1]
        if current_location.id == 354:
            print("")

        rooms.append(current_location.id)

        if current_location.id not in bfs_visited:
            bfs_visited[current_location.id] = []
            if direction_boi != None:
                bfs_visited[current_location.id].append(direction_boi)
                direction_boi = None
        else:
            if direction_boi != None:
                bfs_visited[current_location.id].append(direction_boi)
                direction_boi = None

        exits = current_location.get_exits()

        for direction in visited[current_location.id]:
            if visited[current_location.id][direction][0] == '?':
                bfs_visited[current_location.id].append(direction)
                return path

        for x in exits:
            if x not in bfs_visited[current_location.id]:
                if direction_boi == None:
                    direction_boi = x
                room_in_direction = current_location.get_room_in_direction(x)
                new_path = list(path)
                new_path.append(room_in_direction)
                # bfs_visited[current_location.id].append(x) # DANGER APPENDING IT EVERYTIME CAUSES PROBLEMS BECAUSE YOU MAY NOT VISIT THE PATH
                queue.enqueue(new_path)

    return None


traversal_path = traverseWorld()


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

print(traversal_path)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
