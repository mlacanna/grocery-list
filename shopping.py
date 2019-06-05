import os,sys,time

gList = []

try:
	f = open("shopping.txt", "r")
	for line in f:
		gList.append(line.strip())
	f.close()
except:
	pass

def mainScreen():
	os.system('cls') # for linux 'clear'
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("       Shopping List       ")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n\nYour list contains", len(gList), "items.\n")
	print("Please choose from the following options: \n")
	print("(1) add to the list")
	print("(2) delete from the list")
	print("(3) view the list")
	print("(4) quit the program")
	choice = input("\nchoice: ")
	
	if choice == "1":
		addScreen()
	elif choice == "2":
		deleteScreen()
	elif choice == "3":
		viewScreen()
	elif choice == "4":
		sys.exit()
	else:
		mainScreen()

def addScreen ():
	global gList
	os.system('cls') # for linux 'clear'
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("       ADD SCREEN          ")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n\n")
	print("Please enter the name of the item that you want to add.")
	print("Press ENTER to return to the main menu.\n")
	item = input("\nItem: ")
	if len(item) > 0:
		gList.append(item)
		print("Item added!")
		saveList()
		time.sleep(1)
		addScreen()
	else:
		mainScreen()

def viewScreen() :
	os.system('cls') # for linux 'clear'
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("       View Screen         ")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("\n\n")
	for item in gList:
		print(item)
		
	print("\n\n")
	print("Press enter to return to the main menu")
	input()
	mainScreen()
	
	

def deleteScreen():
	global gList
	os.system('cls') # for linux 'clear'
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	print("       Delete Screen       ")
	print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
	count = 0
	for item in gList:
		print(count, " ", item)
		count = count + 1
	print("What number to delete?")
	choice = input("number: ")
	if len(choice) > 0:
		try: 
			del gList[int(choice)]
			print("Item deleted...")
			saveList()
			time.sleep(1)
		except:
			print("invalid number")
			time.sleep(1)
		deleteScreen()
		
	else:
		mainScreen()
		
def saveList():
	f = open("shopping.txt", "w")
	for item in gList:
		f.write(item+"\n")
	f.close()
	
	
	
mainScreen()
