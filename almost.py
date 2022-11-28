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
                visited[room][x][0] = None
                visited[room][x][1] = None

        # remove the direction in which we just came from so that we don't repeat ourselves
        exits.remove(get_oposite_direction())

        # add it to the dictionary for the previous direction as the previous room
        visited[room][get_oposite_direction()][0] = room.get_room_in_direction(get_oposite_direction())
        visited[room][get_oposite_direction()][1] = visited[room][get_oposite_direction()][0].id

        # loop through the exits until finding an unexplored path
        for x in exits:
            if visited[room][x][0] == '?':
                return (False, x)

    # we have reached the end of a path 
    else:
        for x in exits_string:
            if x not in exits:
                visited[room][x][0] = None
        return(True, exits[0])


def get_room_status(room):
    for exits in visited[room]:
        if visited[room][exits][0] == '?':
            return True
    
    return False


def traverseWorld():
    # creating dict entry for starting room
    visited[player_starting_room] = {'n': ['?',''], 's': ['?',''], 'w': ['?',''], 'e' : ['?','']}

    # get random room to start traversing
    starting_route = get_random_course(player_starting_room)

    # get the next room and move the player there
    going_to_room = starting_route[0]

    # get the direction were going and append it to the path
    direction_to = starting_route[1]
    visited[player_starting_room][direction_to][0] = going_to_room
    visited[player_starting_room][direction_to][1] = going_to_room.id
    path_taken.append(direction_to)
    player.travel(direction_to)

    result = traverse_path(player.current_room)
    return result


def traverse_path(room):
    stack.push(room)
    while stack.size() > 0:
        current_room = stack.pop()

        if current_room not in visited or get_room_status(current_room):
            if current_room not in visited: 
                visited[current_room] = {'n': ['?',''], 's': ['?',''], 'w': ['?',''], 'e' : ['?','']}
            
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
                visited[current_room][exits[1]][0] = player.current_room
                visited[current_room][exits[1]][1] = player.current_room.id 

                # add the room to the stack
                stack.push(player.current_room)


            # if we have reached the end do this
            else:
                
                path_taken.append(exits[1])
                player.travel(exits[1])
                visited[current_room][exits[1]][0] = player.current_room
                visited[current_room][exits[1]][1] = player.current_room.id

                # here instead of traveling to the next room we need to just find a new room from our current room
                path = find_unexplored_room(player.current_room)
                travel_path_player(path)

                for x in visited[player.current_room]:
                    if visited[player.current_room][x][0] == '?':
                        room_going_to = player.current_room.get_room_in_direction(x)
                        stack.push(room_going_to)

                        # setting our current rooms dictionary correctly with the room we are heading to 
                        visited[player.current_room][x][0] = room_going_to
                        visited[player.current_room][x][1] = visited[player.current_room][x][0].id

                        # setting the room in which were headings previous direction to the current room
                        # visited[room_going_to][x][0] = player.current_room
                        # visited[room_going_to][x][1] = visited[room_going_to][x][0].id
                        player.travel(x)
                        path_taken.append(x)


                        break
                        




def find_unexplored_room(room):

    # removing the exit we just came from as it is an end of path so we don't want to go back ever
    op_direction = get_oposite_direction()
    temp = ""
    direc = ""
    if op_direction == 'n':
        direc = 'n'
        temp = room.n_to
        room.n_to = None
    elif op_direction == 's':
        direc = 's'
        temp = room.s_to
        room.s_to = None
    elif op_direction == 'w':
        direc = 'w'
        temp = room.w_to
        room.w_to = None
    elif op_direction == 'e':
        direc = 'e'
        temp = room.e_to
        room.e_to = None

    bfs_visited[room] = []
    queue.enqueue(room)
    path = []
    direct = []

    while queue.size() > 0:

        if len(direct) > 0:
            path.append(direct[0])
            direct.remove(direct[0])

        current_location = queue.dequeue()
        
        if current_location not in bfs_visited:
            bfs_visited[current_location] = []

        # I think we need to check the room given to see if it has unexplored paths
        exits = current_location.get_exits()

        # looping through the exits of the room to see which direction is unexplored
        for direction in visited[current_location]:
            if visited[current_location][direction][0] == '?':

                # probably just return the room and the path to get there



                # visited[current_location][direction][0] = current_location.get_room_in_direction(direction)
                # visited[current_location][direction][1] = visited[current_location][direction][0].id
                # # path.append(direction)
                # bfs_visited[current_location].append(direction)
                # stack.stack = []
                # stack.push(current_location.get_room_in_direction(direction))
                # travel_path_player(path) 

                # queue.queue = [] # empty the queue
                if direc == 'n':
                    room.n_to = temp
                elif direc == 's':
                    room.s_to = temp
                elif direc == 'e':
                    room.w_to = temp
                elif direc == 'e':
                    room.e_to = temp

                
                return path

        for x in exits:
            if x not in bfs_visited[current_location]:
                room_in_direction = current_location.get_room_in_direction(x)
                if room_in_direction != player.current_room: 
                    queue.enqueue(current_location.get_room_in_direction(x))
                    direct.append(x)
                    bfs_visited[current_location].append(x)
                # will need to figure out something to pass up the direction that is being traveled
                # like every time that it is executed
        
        # break












#                                                        434       497--366--361  334--384--435  476                                                        #
#                                                         |                   |    |              |                                                         #
#                                                         |                   |    |              |                                                         #
#                                              477--443  425            386--354--321  338  313  380--445--446                                              #
#                                                    |    |              |         |    |    |    |    |                                                    #
#                                                    |    |              |         |    |    |    |    |                                                    #
#                                                   408  350  483  385  388  285  304  278  287--353  480                                                   #
#                                                    |    |    |    |    |    |    |    |    |                                                              #
#                                                    |    |    |    |    |    |    |    |    |                                                              #
#                                    442  461  426  392--281  223--169  257  253  240  196--224  255  373                                                   #
#                                     |    |    |         |         |    |    |    |    |         |    |                                                    #
#                                     |    |    |         |         |    |    |    |    |         |    |                                                    #
#                                    417  422--394--318--199--197--165--163--228  233--152  192--239--336--421                                              #
#                                     |              |                   |              |    |                                                              #
#                                     |              |                   |              |    |                                                              #
#                          491  453--351  444  374--340  328--200--204  148--178  143  147--154--184  282  363  389                                         #
#                           |         |    |                   |         |         |    |              |    |    |                                          #
#                           |         |    |                   |         |         |    |              |    |    |                                          #
#                          489  441  332  387  341--316  195  175--141  121--123--138--139--176  136--231--294--311--499                                    #
#                           |    |    |    |         |    |         |    |                        |                                                         #
#                           |    |    |    |         |    |         |    |                        |                                                         #
#                     396--391  319  295  331  307  292--185--155  107  111--114--120  172  146  109  186--262--390--398                                    #
#                           |    |    |    |    |              |    |    |              |    |    |    |              |                                     #
#                           |    |    |    |    |              |    |    |              |    |    |    |              |                                     #
#           452--428--411--324--289--250  277  208--166  140  082  102--064  101  093  132  086--095  098  245--343  487                                    #
#                 |                   |    |         |    |    |         |    |    |    |    |         |    |                                               #
#                 |                   |    |         |    |    |         |    |    |    |    |         |    |                                               #
#           451--429  397  357--342--221--174  210  161  063--061  033  060  091  051  073  084  078--090--142  381--431                                    #
#                      |                   |    |    |         |    |    |    |    |    |    |    |              |                                          #
#                      |                   |    |    |         |    |    |    |    |    |    |    |              |                                          #
#      492--400--399--358  352  297--207  124--112--106--079--046--017--028  037--042  056--067  075--088--125--238--293                                    #
#                      |    |         |                             |    |    |         |         |    |    |                                               #
#                      |    |         |                             |    |    |         |         |    |    |                                               #
#           414--365--333--303  171--168--137  085  074  032  047--014  030  031  027--055  048--053  103  198--270--300--320                               #
#                 |         |              |    |    |    |         |         |    |         |                             |                                #
#                 |         |              |    |    |    |         |         |    |         |                             |                                #
#                447  301--187--167--108--081--045--040--019--015--013--009  020--026  035--044--059--189--275--283--376  471                               #
#                                          |                             |    |         |                             |                                     #
#                                          |                             |    |         |                             |                                     #
#                436  470  227--194--128--092  069--041--036--021  004  007--012--018--034--039--071--150--251  325  468                                    #
#                 |    |              |    |    |    |         |    |    |         |         |    |              |                                          #
#                 |    |              |    |    |    |         |    |    |         |         |    |              |                                          #
#           465--368--284--254--205--162  100  072  076  011--003--000--001--022  024--025  052  115--160--214--246--412                                    #
#                      |                        |         |         |    |         |    |                                                                   #
#                      |                        |         |         |    |         |    |                                                                   #
#           479--418--349  274--222--190--129  089  083--080  016--008  002--010  029  043--049--119--131--329--407                                         #
#                 |                        |    |    |                   |    |    |    |         |                                                         #
#                 |                        |    |    |                   |    |    |    |         |                                                         #
#                463--458  379  226--225--105--104  099  058--023--006--005  038  054  077--130  219--305--330--454                                         #
#                      |    |    |              |    |         |    |    |                        |         |                                               #
#                      |    |    |              |    |         |    |    |                        |         |                                               #
#           486--462  359  266--260  235--158--126  122  068--057  062  050--070--087  182--211  242  326  348                                              #
#                 |    |                   |    |              |    |    |    |    |    |    |    |    |                                                    #
#                 |    |                   |    |              |    |    |    |    |    |    |    |    |                                                    #
#                367--344--230  243  180--164  135  145--113--094  065  066  116  117--170  248  286--288--498                                              #
#                           |    |              |    |         |    |    |    |    |         |    |                                                         #
#                           |    |              |    |         |    |    |    |    |         |    |                                                         #
#                339--314--220--215--177--156--149  183  153--097  134  096  159  127--173  272  309--377--456                                              #
#                 |                        |    |              |    |    |         |    |         |                                                         #
#                 |                        |    |              |    |    |         |    |         |                                                         #
#           482--404  258--236--216--213--209  191  188  157--110  144  179--201  212  202--249  371--430--440                                              #
#            |              |         |         |    |         |    |    |    |    |    |                                                                   #
#            |              |         |         |    |         |    |    |    |    |    |                                                                   #
#           484  433--372--263  271--217  241--193  151--133--118--218  181  206  229  267--302--402--403--439                                              #
#                           |    |         |    |         |         |         |    |                                                                        #
#                           |    |         |    |         |         |         |    |                                                                        #
#      494--457--355--312--299  310  327--256  203  247--234--259  252  244--232  237--370  364--401--427--474                                              #
#                      |    |         |    |    |    |    |    |    |    |    |              |    |    |                                                    #
#                      |    |         |    |    |    |    |    |    |    |    |              |    |    |                                                    #
#                437--347  356  469--362  279  269  369  280  291  261  264  265--273--298--360  420  438                                                   #
#                      |    |         |    |    |              |    |    |    |    |              |    |                                                    #
#                      |    |         |    |    |              |    |    |    |    |              |    |                                                    #
#                393--375  405  423--395  323  315--335--378  306  345  290  268  296--308--337  464  448--490                                              #
#                      |    |                   |    |    |    |    |         |    |    |    |         |                                                    #
#                      |    |                   |    |    |    |    |         |    |    |    |         |                                                    #
#           493--478--413  432--473       410--406  346  466  415  409  322--276  382  317  383       475                                                   #
#                      |    |                             |         |    |    |    |    |    |         |                                                    #
#                      |    |                             |         |    |    |    |    |    |         |                                                    #
#                     419  449--450                      472--495  488  424  459  455  416  460       496                                                   #
#                                                         |                   |                                                                             #
#                                                         |                   |                                                                             #
#                                                   485--481                 467                                                                            #
#                                                                                                                                                           #
