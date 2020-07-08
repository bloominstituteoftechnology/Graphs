#!/usr/bin/env python3

from util import Queue, Stack


__opposites = {
    'n': 's',
    's': 'n',
    'e': 'w',
    'w': 'e'
}


def traverse(player, path, graph={}, breadcrumbs=Stack()):
    room = player.current_room
    if room.id not in graph.keys():
        exits = room.get_exits()

        graph[room.id] = {direction: '?' for direction in exits}

        for direction in exits:
            if graph[room.id][direction] == '?':
                breadcrumbs.push(direction)
                path.append(direction)
                player.travel(direction)
                traverse(player, path, graph, breadcrumbs)
    last_dir = breadcrumbs.pop()
    if last_dir is None:
        return
    back_dir = __opposites[last_dir]
    player.travel(back_dir)
    path.append(back_dir)
