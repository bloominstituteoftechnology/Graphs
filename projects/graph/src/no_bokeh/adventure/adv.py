import random
from room import Room

def random_direction(room):
	directions = []
	if room.n_to is None:
		directions.append('n')
	if room.s_to is None:
		directions.append('s')
	if room.w_to is None:
		directions.append('w')
	if room.e_to is None:
		directions.append('e')
	random.shuffle(directions)
	if len(directions) > 0:
		return directions[0]
	else:
		return None

def connections(room, next_room, direction):
	if direction == 'n':
		room.n_to = next_room
		next_room.s_to = room
	elif direction == 'e':
		room.e_to = next_room
		next_room.w_to = room
	elif direction == 'w':
		room.w_to = next_room
		next_room.e_to = room
	elif direction == 's':
		room.s_to = next_room
		next_room.n_to = room
	else:
		print('room connection not valid')
		return None

def mapGenerator(num_rooms):
	rooms = {}

	for i in range(0, num_rooms):
		new_room = Room(f'Room {i}', "You are standing in an empty room.")
		rooms[i] = new_room

		if i > 0:
			get_random = random_direction(rooms[i - 1])

			if get_random is not None:
				connections(rooms[i - 1], rooms[i], get_random)
	return rooms

room_list = mapGenerator(5)

current_room = room_list[0]

res = ['start']

while res[0] != 'q':
	print(current_room)
	current_room.getExits()
	res = input("Where would you like to go?").split(" ")
	current_room = current_room.room_direction(res[0])











