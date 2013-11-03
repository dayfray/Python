# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
count = 0
last_range = 0
num_range100 = 0
num_range1000 = 0

# helper function to start and restart the game
def new_game():
    # remove this when you add your code  
    global last_range 
    global count
    global num_range100
    global num_range1000

    if last_range == 101:
        range100()
        
    elif last_range == 1001:
        range1000()


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global last_range
    global count
    global num_range100

    count = 8
    last_range = 101
    num_range100 = random.randrange(0, last_range)
    
    # remove this when you add your code    
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global last_range
    global count
    global num_range1000

    count = 11
    last_range = 1001
    num_range1000 = random.randrange(0, last_range)
    
    # remove this when you add your code    
    
    
def input_guess(guess):
    # main game logic goes here	
    global count
    global last_range
    global num_range100
    global num_range1000

    input_guess = float(guess)

# check to see if the button for the 100 range was selected

    if last_range == 101:

# check to see if count is zero

        if count == 1:

            print "Your guess is " + str(guess)
            print "I'm sorry, but you have " + str(count) + " guesses remaining. You have lost."
            print ""
            new_game()

        elif input_guess < num_range100 and count > 1:

            print "Your guess is " + str(guess)
            count -= 1
            print "Higher!"
            print "You have " + str(count) + " turns remaining."
            print ""

        elif input_guess > num_range100 and count > 1:

            print "Your guess is " + str(guess)
            count -= 1
            print "Lower!"
            print "You have " + str(count) + " turns remaining."
            print ""

        elif input_guess == num_range100 and count > 1:

            print "Your guess is " + str(guess)
            print "Congratulations! Your guess of " + str(guess) + " was correct."
            print "The hidden number was " + str(num_range100)
            print ""
            new_game()

# check to see if the button for the 1000 range was selected

    elif last_range == 1001:

         if count == 1:
            print "Your guess is " + str(guess)
            print "I'm sorry, but you have " + str(count) + " guesses remaining. You have lost."
            print ""
            new_game()

         elif input_guess < num_range1000 and count > 1:

            print "Your guess is " + str(guess)
            count -= 1
            print "Higher!"
            print "You have " + str(count) + " turns remaining."
            print ""

         elif input_guess > num_range1000 and count > 1:

            count -= 1
            print "Your guess is " + str(guess)
            print "Lower!"
            print "You have " + str(count) + " turns remaining."
            print ""

         elif input_guess == num_range1000 and count > 1:

            print "Your guess is " + str(guess)
            print "Congratulations! Your guess of " + str(guess) + " was correct."
            print "The hidden number was " + str(num_range1000)
            print ""
            new_game()
    # remove this when you add your code
    

    
# create frame
f = simplegui.create_frame("Guess the Number Game!", 200, 200)


# register event handlers for control elements
f.add_button("Range: 0 to 100", range100, 100)
f.add_button("Range: 0 to 1000", range1000, 100)
f.add_input("Enter Guess Here", input_guess, 100)



# call new_game and start frame

new_game()


# always remember to check your completed program against the grading rubric

