# coding: utf-8
import random
mapSize = 4
x = list(range(mapSize))
y = list(range(mapSize))
map = []
player = []
monster = []
door = []
i = 0

def winorlose(player, monster):
	if player == door:
		print("You Win!")
		return(1)
	elif player == monster:
		print("You Lose!")
		return(0)
	else:
		return(2)
		
#initiate the map
while i < mapSize:
	for num in y:
		map.append((x[i], num))	
	i += 1

#initiate starting location of game pieces	
player = list(random.choice(map))
print(player)
#door = random.choice(map)
door = list(random.choice(map))
print(door)
monster = list(random.choice(map))

#move player and monster
while True:
	move = raw_input("> ")
	monster = list(random.choice(map))
	if move == "down".lower():
		player[1] = player[1] - 1
		win = winorlose(player, monster)
		if win == 1:
			break
		elif win == 0:
			break
		else:
			continue
		
	elif move == "left".lower():
		player[0] = player[0] - 1
		win = winorlose(player, monster)
		if win == 1:
			break
		elif win == 0:
			break
		else:
			continue
	
	elif move == "right".lower():
		player[0] = player[0] + 1
		win = winorlose(player, monster)
		if win == 1:
			break
		elif win == 0:
			break
		else:
			continue
	
	elif move == "right".lower():
		player[1] = player[1] + 1
		win = winorlose(player, monster)
		if win == 1:
			break
		elif win == 0:
			break
		else:
			continue


	