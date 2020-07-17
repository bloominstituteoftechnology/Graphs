from util import Queue


class Player:
    def __init__(self, starting_room, rooms):
        self.current_room = starting_room
        self.entered = {starting_room}
        self.rooms = rooms
        self.traversal_path = []

    def travel(self, direction, show_rooms=False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            self.traversal_path.append(direction)
            self.entered.add(self.current_room)
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")

    def bfs(self):
        q = Queue()
        q.enqueue((self.current_room, []))

        visited = set()

        while q.size() > 0:
            current, path = q.dequeue()

            if current not in self.entered:
                return path

            elif current not in visited:
                visited.add(current)

                for exit in current.get_exits():
                    path_copy = path.copy()
                    path_copy.append(exit)
                    q.enqueue((current.get_room_in_direction(exit), path_copy))

        raise ValueError('Room not found')

    def commense_run(self):
        while len(self.entered) < self.rooms:
            path = self.bfs()
            for direction in path:
                print('direction: ', direction)
                self.travel(direction)
                print(self.current_room)
