import random
from room import Room
from item import Treasure
import random


# def __init__(self, name, description, score_amount):

golden_idol = Treasure('golden idol', 'it apears to be a golden idol in the form of a bird claw', 100)

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

def game_generator(num_rooms):
	rooms = {}
	cordinates = [0,0]
	occupied = set()

	for i in range(0, num_rooms):
		new_room = Room(f'Room {i}', "You are standing in an empty room.", i)
		rooms[i] = new_room

		if i > 0:
			get_random = random_direction(rooms[i - 1])
			new_cords = get_cords(get_random, cordinates)

			if get_random is not None and tuple(new_cords) not in occupied:
				connections(rooms[i - 1], rooms[i], get_random)
				occupied.add(tuple(new_cords))

	#here I will pick a room at random and put a treasure object into it
	random_num = random.randint(0, len(rooms) - 1)
	rooms[random_num].items.append(golden_idol)

	print()
	for i in rooms:
		print(f'room number: {rooms[i].id}, exits: {rooms[i].getExits()}')

	#I will loop through all my rooms
	for i in rooms:
		#I will give each room an edge list based on the rooms they connect to
		for j in rooms[i].getExits():
			connected = rooms[i].room_direction(j)
			edge = connected.id
			rooms[i].edges.append(edge)

		#to do this I will need to 

	print()
	for i in rooms:
		print(f'room id: {rooms[i].id}, room edge list: {rooms[i].edges}')

	return rooms


room_list = game_generator(3)
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