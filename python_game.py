# monster chase game

class Main(object):

	max_width = 5
	max_height = 5
	character_alive = True
	character_won = False
	monster_awake = False
	monster_awakened = False
	monster_move_per_turn = 2

	def __init__(self):

		self.displayMenu()
		

	def displayMenu(self):

		menu_list = ['Start New Game', 'Save Game', 'Load Game', 'Customize Setup', 'Exit']
		print "Type the number of your choice:"
		print " "
		for i in range(1, len(menu_list) + 1):
			print str(i) + ' ' + menu_list[i-1]
		choice = raw_input("Your Choice:")
		self.menuChoice(choice)

	def menuChoice(self, choice):
		try:
			choice = int(choice)
		except ValueError:
			choice = 0

		if choice == 1:
			pass
		elif choice == 2:
			pass
		elif choice == 3:
			pass
		elif choice == 4:
			pass
		elif choice == 5:
			sys.exit(0)
		else:
			print "That was not a valid option. Try again."
			self.displayMenu()


