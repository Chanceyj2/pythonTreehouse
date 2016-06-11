# coding: utf-8

toDoList = []

def toDoHelp():
	print("Enter items to the toDo list")
	print("""DONE: Will end the program 
SHOW: Will display your toDo list""")

def showList():		
	i = 1
	for x in toDoList:
		print("{}: {}".format(i, x))
		i += 1

def addItem():
	
	while True:
		item = raw_input("> ")
	
		if item == "DONE":
			showList()
			break
		elif item == "SHOW":
			showList()
			continue
		elif item == "HELP":
			toDoHelp()
			continue
		elif item == "MOVE":
			moveItem()
			continue	
		else:
			toDoList.append(item)
			
def moveItem():
	itemToMove = int(raw_input("> "))
	locToMove = int(raw_input(">> "))
	
	tempItem = toDoList.pop(itemToMove - 1)
	print(tempItem)
	toDoList.insert((locToMove - 1), tempItem)
	
toDoHelp()
addItem()