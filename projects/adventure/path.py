opposite_directions = {
                        'n': 's', 
                        's': 'n', 
                        'e': 'w',
                        'w': 'e'
                        }

class Path:
    """
    Path along which a Player walks 
    in a World of Rooms
    """

    def recursive_traverse(self, room, visited=None):
        """
        Method to recursively traverse the path, 
        visiting all rooms in a given map
        """

        # If no rooms have been visited, 
        # create a set to store visited room ids
        if visited is None:
            visited = set()
        
        # Create an empty list to store the path already taken
        path_taken = []

        # Add current room id to visited
        visited.add(room.id)

        # Loop thru each room exit for current room
        for room_exit in room.get_exits():

            # Set pointer for next room in direction of room exit
            next_room = room.get_room_in_direction(room_exit)

            # If the room is yet to be visited
            if next_room.id not in visited:

                # Use recursion to visit other rooms
                unvisited = self.recursive_traverse(next_room, visited)

                # If there are rooms left to traverse/visit
                if unvisited:

                    # Update path using exit and walking direction information
                    current_path = [room_exit] + \
                                   unvisited + \
                                   [opposite_directions[room_exit]]

                # If there are no rooms left to traverse/visit
                else:

                    # Backtrack where necessary
                    current_path = [
                        room_exit, 
                        opposite_directions[room_exit]
                        ]

                # Update taken path with current path information
                path_taken = path_taken + \
                             current_path

        # Return final path taken
        return path_taken