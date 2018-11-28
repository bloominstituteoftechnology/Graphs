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

def get_cords(direction, xy):
	if direction == "n":
		xy[1] += 1
	elif direction == "s":
		xy[1] -= 1
	elif direction == "e":
		xy[0] += 1
	elif direction == "w":
		xy[0] -= 1
	return xy

def mapGenerator(num_rooms):
	rooms = {}
	cordinates = [0,0]
	occupied = []

	for i in range(0, num_rooms):
		new_room = Room(f'Room {i}', "You are standing in an empty room.")
		rooms[i] = new_room

		if i > 0:
			get_random = random_direction(rooms[i - 1])
			new_cords = get_cords(get_random, cordinates)
			print(new_cords)

			if get_random is not None and new_cords not in occupied:
				connections(rooms[i - 1], rooms[i], get_random)
				occupied.append(list(new_cords))

	print(occupied)
	return rooms

room_list = mapGenerator(5)
current_room = room_list[0]
res = ['start']

while res[0] != 'q':
	print(current_room)
	exits = current_room.getExits()
	res = input("Where would you like to go?").split(" ")

	if res[0] not in exits and res[0] != 'q':
		print('you may not head in that direction')
	else:
		current_room = current_room.room_direction(res[0])