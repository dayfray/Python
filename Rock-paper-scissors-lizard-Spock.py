# Rock-paper-scissors-lizard-Spock template

import math
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"

    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4

    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)

    # compute difference of player_number and comp_number modulo five
    resulting_number = player_number - comp_number

    comp_name = number_to_name(comp_number)

	# use if/elif/else to determine winner
    

   

    if resulting_number == 1 or resulting_number == 2 or resulting_number % 5 == 1 or resulting_number % 5 == 2:
        print "The player chooses: " + name
        print "The computer chooses: " + comp_name
        print ""
        print "The player is the winner."
        print ""
        

    elif resulting_number == 3 or resulting_number == 4 or resulting_number % 5 == 3 or resulting_number % 5 == 4:
        print "The player chooses: " + name
        print "The computer chooses: " + comp_name
        print ""
        print "The computer is the winner."
        print ""
        
    else:
        print "The player chooses: " + name
        print "The computer chooses: " + comp_name
        print ""
        print "There's a tie! Nobody wins."
        print ""


    # convert comp_number to name using number_to_name
    

    # print results
    
    
# test your code
rpsls("rock")
print "====="
print ""
rpsls("Spock")
print "====="
print ""
rpsls("paper")
print "====="
print ""
rpsls("lizard")
print "====="
print ""
rpsls("scissors")

# always remember to check your completed program against the grading rubric


