"""
Implementation of a partial map in our adventure game as a graph.
"""
# Import libraries, packages, modules, classes/functions:
from data_structures import Stack, Queue
from numpy import NaN

# Fixed constants:
directions = ["n", "s", "w", "e"]


class Map:
    """
    Represent a map as an adjacency list (dictionary of graph vertices/rooms with connecting edges/routes).
    """
    def __init__(self):
        # Initiate as empty adjacency list:
        self.rooms = {}
    
    def add_room(self, room):
        """
        Add room to our map.
        """
        # Check to make sure the provided room isn't already in the map:
        if room not in self.rooms:
            # Add it:
            self.rooms[room] = {key:NaN for key in directions}
        else:
            raise IndexError(f"Room {room} is already in the map!")

    def add_edge(self, room_a, direction:str, room_b):
        """
        Add a bidirectional edge (route between adjacent rooms) to the map, from room_a to room_b.
        """
        # Make sure both rooms are in the map before adding the edge that connects them:
        if room_a in self.rooms and room_b in self.rooms:
            self.rooms[room_a][direction] = room_b
            self.rooms[room_b][direction] = room_a  # For bidirectional edge
        else:
            raise IndexError("Room does not exist in the map!")

    def get_neighbors(self, room):
        """
        Get all neighboring rooms (with connecting edges) of the given room on the map.
        """
        return self.rooms[room]

    # def bft(self, starting_room_id):
    #     """
    #     Traverse and print each room in breadth-first order (a BFT) beginning from starting_room.
    #     """
    #     # Initialize empty queue and set of visited nodes:
    #     queue = Queue()
    #     visited = set()

    #     # Check if provided starting room is in our map:
    #     if starting_room_id in self.rooms.keys():
    #         # If so, add starting room to queue:
    #         queue.enqueue(starting_room_id)
    #     else:
    #         return IndexError(f"Provided starting room {starting_room_id} does not exist in map!")

    #     # Process all rooms via BFT:
    #     while queue.size() > 0:
    #         # Get next room to process as first item in queue:
    #         current_room = queue.dequeue()
    #         # If the current room has not already been visited+processed, process it:
    #         if current_room not in visited:
    #             # Process current room:
    #             print(current_room)
    #             # Add adjacent rooms to queue for future processing:
    #             for adjacent_room in self.get_neighbors(current_room):
    #                 queue.enqueue(adjacent_room)
    #             # Mark current room as "visited" by adding to our set of visited rooms:
    #             visited.add(current_room)

    # def dft(self, starting_room_id):
    #     """
    #     Traverse and print each room in depth-first order (DFT) beginning from starting_room.
    #     """
    #     # Initialize empty stack and set of visited nodes:
    #     stack = Stack()
    #     visited = set()

    #     # Check if provided starting room is in our map:
    #     if starting_room_id in self.rooms.keys():
    #         # If so, add starting room to stack:
    #         stack.push(starting_room_id)
    #     else:
    #         return IndexError(f"Provided starting room {starting_room_id} does not exist in map!")

    #     # Process all rooms via BFT:
    #     while stack.size() > 0:
    #         # Get next room to process as first item in stack:
    #         current_room = stack.pop()
    #         # If the current room has not already been visited+processed, process it:
    #         if current_room not in visited:
    #             # Process current room:
    #             print(current_room)
    #             # Add adjacent rooms to stack for future processing:
    #             for adjacent_room in self.get_neighbors(current_room):
    #                 stack.push(adjacent_room)
    #             # Mark current room as "visited" by adding to our set of visited rooms:
    #             visited.add(current_room)

    # def bfs(self, starting_room, target_room):
    #     """
    #     Return a list containing the shortest path from starting_room to destination_room, 
    #     after searching for and finding it with a breadth-first search (BFS) algorithm.
    #     """
    #     # Initialize empty queue and set of visited nodes:
    #     queue = Queue()
    #     visited = set()

    #     # Initialize path (we will add the rest of the path from starting room to target room below):
    #     path = [starting_room]

    #     # Check if provided starting room is in our map:
    #     if starting_room in self.rooms.keys():
    #         # If so, add starting room to queue:
    #         queue.enqueue(path)
    #     else:
    #         return IndexError(f"Provided starting room {starting_room} does not exist in map!")

    #     # Process all rooms via BFT:
    #     while queue.size() > 0:
    #         # Get next room to process as first item in queue:
    #         current_path = queue.dequeue()
    #         current_room = current_path[-1]
    #         # If the current room has not already been visited+processed, check and process it:
    #         if current_room not in visited:
    #             # Check if it is the target --> if so, return its full path:
    #             if current_room == target_room:
    #                 return current_path
    #             # If not, then get its neighbor rooms and add their paths to the queue for future processing:
    #             for adjacent_room in self.get_neighbors(current_room):
    #                 adjacent_room_path = current_path + [adjacent_room]
    #                 queue.enqueue(adjacent_room_path)
    #             # Mark current room as "visited" by adding to our set of visited rooms:
    #             visited.add(current_room)
        
    #     # If no path found in entire map, return None:
    #     return None

    # def dfs(self, starting_room, target_room):
    #     """
    #     Return a list containing the shortest path from starting_room to destination_room, 
    #     after searching for and finding it with a depth-first search (DFS) algorithm.
    #     """
    #     # Initialize empty stack and set of visited nodes:
    #     stack = Stack()
    #     visited = set()

    #     # Initialize path (we will add the rest of the path from starting room to target room below):
    #     path = [starting_room]

    #     # Check if provided starting room is in our map:
    #     if starting_room in self.rooms.keys():
    #         # If so, add starting room to stack:
    #         stack.push(path)
    #     else:
    #         return IndexError(f"Provided starting room {starting_room} does not exist in map!")

    #     # Process all rooms via BFT:
    #     while stack.size() > 0:
    #         # Get next room to process as first item in stack:
    #         current_path = stack.pop()
    #         current_room = current_path[-1]
    #         # If the current room has not already been visited+processed, check and process it:
    #         if current_room not in visited:
    #             # Check if it is the target --> if so, return its full path:
    #             if current_room == target_room:
    #                 return current_path
    #             # If not, then get its neighbor rooms and add their paths to the stack for future processing:
    #             for adjacent_room in self.get_neighbors(current_room):
    #                 adjacent_room_path = current_path + [adjacent_room]
    #                 stack.push(adjacent_room_path)
    #             # Mark current room as "visited" by adding to our set of visited rooms:
    #             visited.add(current_room)
        
    #     # If no path found in entire map, return None:
    #     return None


if __name__ == '__main__':
    # map = Map()  # Instantiate your map
    # # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    # map.add_room(1)
    # map.add_room(2)
    # map.add_room(3)
    # map.add_room(4)
    # map.add_room(5)
    # map.add_room(6)
    # map.add_room(7)
    # map.add_edge(5, 3)
    # map.add_edge(6, 3)
    # map.add_edge(7, 1)
    # map.add_edge(4, 7)
    # map.add_edge(1, 2)
    # map.add_edge(7, 6)
    # map.add_edge(2, 4)
    # map.add_edge(3, 5)
    # map.add_edge(2, 3)
    # map.add_edge(4, 6)

    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    # print(map.rooms)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    # map.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    # map.dft(1)
    # map.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    # print(map.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    # print(map.dfs(1, 6))
    # print(map.dfs_recursive(1, 6))

    map = Map()  # Instantiate your map
    map.add_room(room=0)
    map.add_room(room=1)
    map.add_room(room=2)
    map.add_edge(room_a=0, direction="n", room_b=1)
    map.add_edge(room_a=1, direction="n", room_b=2)
    
    # map.add_room('1')
    # map.add_room('2')
    # map.add_room('3')
    # map.add_edge('0', '1')
    # map.add_edge('1', '0')
    # map.add_edge('0', '3')
    # map.add_edge('3', '0')
    print(map.rooms)
    # map.add_edge('0', '4')  # Should throw IndexError.
