# coding: utf-8
import random

MAP = [(0,0), (0,1), (0,2),
			 (1,0), (1,1), (1,2),
			 (2,0), (2,1), (2,2)]
		
def get_location(MAP):
	# monster = random
	monster = random.choice(MAP)
	# door = random 
	door = random.choice(MAP)
	# start = random
	start = random.choice(MAP)
	
	# if monster, door, or start are the same, do it again
	if monster == door or monster == start:
		get_location(MAP)
	elif door == start:
		get_location(MAP)
	else:
		# return monster, door, start
		return(monster, door, start)

def move_player(player, move):
	# get the player's current location 
	# if move is LEFT, y - 1
	# if move is RIGHT, y + 1
	# if move is UP, x + 1
	# if move is DOWN, x - 1
	return(player)
	
def get_moves():
	MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	
	# if player's y is 0, remove LEFT 
	# if player's x is 0, remove UP
	# if player's y is 2, remove RIGHT
	# if player's x is 2, remove DOWN
	return(moves)
	
while True:
	monster, door, player = get_location(MAP)

	print("Welcome to the dungeon!")
	print("You are currently in {}")  # fill in with player posisition
	print("You can move {}") # fill in with available moves
	print("Enter QUIT to exit")
	
	move = raw_input(">")
	
	move = move.upper()
	
	if move == 'QUIT':
		break
	
	# if it's a good move change the player's position
	# if it's a bad move, don't change anythin
	# if the new player position is the door, they win 
	# if the new player position is the monster, they lose
	# otherwise continue
	
		