#                                        #
#      017       002       014           #
#       |         |         |            #
#       |         |         |            #
#      016--015--001--012--013           #
#                 |                      #
#                 |                      #
#      008--007--000--003--004           #
#       |         |                      #
#       |         |                      #
#      009       005                     #
#       |         |                      #
#       |         |                      #
#      010--011--006                     #


"""
I am going to need to modify my bfs so that it can handle the repeats, like the going back to the node it just came from
"""
























def travel_path_player(path):
    for x in path:
        player.travel(x)
        path_taken.append(x)

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
        exits.remove(get_oposite_direction())

        # add it to the dictionary for the previous direction as the previous room
        visited[room.id][get_oposite_direction()][0] = room.get_room_in_direction(get_oposite_direction())
        visited[room.id][get_oposite_direction()][1] = visited[room.id][get_oposite_direction()][0].id

        # loop through the exits until finding an unexplored path
        for x in exits:
            if visited[room.id][x][0] == '?':
                return (False, x)

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
            if exits == None:
                return path_taken
        
            # if we have not reached the end of our path do this
            if exits[0] == False:
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
                if current_room.id == 341:
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

                else:
                    bfs_visited[player.current_room.id].append(get_oposite_direction())
                


                # here instead of traveling to the next room we need to just find a new room from our current room
                path = find_unexplored_room(player.current_room)
                if path == None:
                    return path_taken
                
                travel_path_player(path)

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


                        break
                        

def find_unexplored_room(room):
    queue.enqueue(room)
    path = []
    direct = []
    last_direct = ''

    while queue.size() > 0:
        
        current_location = queue.dequeue()
        if len(direct) > 0:
            path.append(direct[0])
            
        
        if current_location.id not in bfs_visited:
            bfs_visited[current_location.id] = [opposite_dir_dict[path[0]]]
        
        if len(direct) > 0:
            direct.remove(direct[0])

        exits = current_location.get_exits()

        for direction in visited[current_location.id]:
            if visited[current_location.id][direction][0] == '?':
                bfs_visited[current_location.id].append(direction)

                return path

        for x in exits:
            if x not in bfs_visited[current_location.id]:
                room_in_direction = current_location.get_room_in_direction(x)
                if room_in_direction != player.current_room: 
                    queue.enqueue(current_location.get_room_in_direction(x))
                    direct.append(x)
                    bfs_visited[current_location.id].append(x)

                    if room_in_direction.id not in bfs_visited:
                        bfs_visited[room_in_direction.id] = [opposite_dir_dict[x]]
                    else:
                        bfs_visited[room_in_direction.id].append(opposite_dir_dict[x])

    return None