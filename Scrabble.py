# This is a scrabble cheater made in Python

scores = { "a" : 1, "b" : 3, "c" : 3, "d" : 2, "e" : 1, "f" : 4, "g" : 2, "h" : 4, "i" : 1, "j" : 8, 
"k" : 5, "l" : 1, "m" : 3, "n" : 1, "o" : 1, "p" : 3, "q" : 10, "r" : 1, "s" : 1, "t" : 1, "u" : 1, "v" : 4, "w" : 4, "x" : 8, "y" : 4, "z" : 10}





def scrabble_score(word):
    
    if len(str(word)) > 0 and word.isalpha():
    	word = word.lower()
    	result = 0
    	for letter in word:
    	    result += scores[letter]
    	return result

	elif len(word) <= 0:
		print "You have entered an incorrect response. Please try again."
		word.scrabble_score()

	elif word.isint() or word.isfloat():
		print "You have entered an incorrect response. Please try again."
		word.scrabble_score()


print "Your score is: " + str(scrabble_score(raw_input("What is the word you created in Scrabble? "))) + " points."


"""
def scrabble_score(word):
    word = word.lower()
    result = 0
    for letter in word:
        result += scores[letter]
    return result


So this function first makes the input "word" equal to itself, only all lower case, making it easier to go through.
Then, a new variable, "result" is created as a placeholder for the scores of the letters added together.
Now, a "for" loop is made for going through each "letter" in the input "word", and making the placeholder "result",
equal to itself plus the corresponding letter key in the dictionary "score", then it returns the final "result".






Had the following results what using the above code as it is now:



kemet@kemet-P15xEMx ~ $ python '/home/kemet/Programming Tutorials/Python Tutorials/Python Tutorials - Web Pages/Project Files/Scrabble.py'

What is the word you created in Scrabble? what

Your score is: 10 points.


kemet@kemet-P15xEMx ~ $ python '/home/kemet/Programming Tutorials/Python Tutorials/Python Tutorials - Web Pages/Project Files/Scrabble.py'

What is the word you created in Scrabble? 1

Your score is: None points.


Need to work on that.

"""




