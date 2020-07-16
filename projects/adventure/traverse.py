#!/usr/bin/env python3

from util import Queue, Stack


__opposites = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}


def get_room_from_path(starting_room, path):
    room = starting_room
    for direction in path:
        room = room.get_room_in_direction(direction)
    return room

def to_nearest_unexplored(starting_room, graph):
    explored = set()
    queue = Queue()
    queue.enqueue([])

    while queue.size() != 0:
        path = queue.dequeue()
        room = get_room_from_path(starting_room, path)
        exits = room.get_exits()

        for direction in exits:
            new_path = path.copy()
            new_path.append(direction)
            if graph[room.id][direction] == '?':
                return new_path
            if (room, direction) not in explored:
                queue.enqueue(new_path)
            explored.add((room, direction))

def add_to_graph_if_needed(room, graph):
    adjacent_rooms = graph.get(room.id)
    if adjacent_rooms is None:
        adjacent_rooms = {direction:'?' for direction in room.get_exits()}
        graph[room.id] = adjacent_rooms

def traverse2(player):
    graph = {}
    path = []
    room = player.current_room
    add_to_graph_if_needed(room, graph)

    while True:
        exits = room.get_exits()
        path_to_unexplored = to_nearest_unexplored(room, graph)
        if path_to_unexplored is None or len(path_to_unexplored) == 0:
            return path
        for direction in path_to_unexplored:
            new_room = room.get_room_in_direction(direction)
            path.append(direction)
            graph[room.id][direction] = new_room.id
            add_to_graph_if_needed(new_room, graph)
            graph[new_room.id][__opposites[direction]] = room.id
            room = new_room


def traverse(player):
    graph = {}
    breadcrumbs = Stack()
    unexplored = set()
    done = False
    path = []

    def travel(direction):
        player.travel(direction)
        new_room_id = room.get_room_in_direction(direction).id
        if new_room_id in unexplored:
            unexplored.remove(new_room_id)
        graph[room.id][direction] = new_room_id
        path.append(direction)

    def get_new_direction():
        for direction in player.current_room.get_exits():
            if graph[player.current_room.id][direction] == '?':
                return direction
        return None

    def add_graph_entry(room):
        graph_entry = {}
        if breadcrumbs.size() > 0:
            last_dir = breadcrumbs.pop()
            backtrack = __opposites[last_dir]
            graph_entry[backtrack] = room.get_room_in_direction(backtrack)
            breadcrumbs.push(last_dir)
        for direction in exits:
            if direction in graph_entry:
                continue
            new_room = room.get_room_in_direction(direction).id
            graph_entry[direction] = '?'
            unexplored.add(new_room)
        graph[room.id] = graph_entry

    while not done:
        room = player.current_room
        exits = room.get_exits()
        if room.id not in graph:
            add_graph_entry(room)
        if len(unexplored) == 0:
            done = True
        else:
            direction = get_new_direction()
            if direction is None:
                prev = breadcrumbs.pop()
                travel(__opposites[prev])
            else:
                # print(direction)
                travel(direction)
                breadcrumbs.push(direction)
    return path
