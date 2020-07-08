#!/usr/bin/env python3

from util import Queue, Stack


__opposites = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}


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
