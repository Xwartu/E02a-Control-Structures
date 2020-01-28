#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!')             # A customary hello to the user, prints in terminal
colors = ['red','orange','yellow','green','blue','violet','purple']             # Listing all the possible colors in a list format that Python intrepreter can read. 
play_again = ''             # Sets up the varaible to be called later. 
best_count = sys.maxsize            # the biggest number, is set up to be called later. 

while (play_again != 'n' and play_again != 'no'):           # Creates a while loop that will not end until play_again == "no" or "n"
    match_color = random.choice(colors)             # Runs a function through the random module to select a color/string at random from the aforementioned list.
    count = 0           # Sets up the count varaible for the attempts to be counted. 
    color = ''          # Sets up the color variable to be called in the input. 
    while (color != match_color): #Creates another while loop within a while loop that won't end till the color inputed matches the rnadomly picked color from the list. 
        color = input("\nWhat is my favorite color? ")              #\n is a special code that adds a new line, input()will collect an input from the user through the terminal.
        color = color.lower().strip() #Takes the user's input and removes any extra characters that isn't text and makes it lowercase.  
        count += 1          # Another way to write count = count + 1, will count each time the loop runs through since the line will be called repeatedly. 
        if (color == match_color):          # An if statement being used to break the loop and reward the user
            print('Correct!')           # Prints the string in the terminal.
        else:           # A corresponding else statement to the previous statement to create a second set of code if the first condition is not met in the fi statement. 
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))              # Prints in terminal, uses the curly braces to input a string repeatedly after the fact, differentiated from count varaivle for human coder's sake. 
    
    print('\nYou guessed it in {} tries!'.format(count))            # Creates a new line, prints in the terminal and uses the same plug in string structure as in line 23

    if (count < best_count):            # A second if statment that keeps track of the highest count variable that comes through the loop. 
        print('This was your best guess so far!')           # Prints string in terminal
        best_count = count          # If the count was higher than best_count the if statement will run and then best_count will become the value stored in count. 

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()          # Asks the user to say yes or no to see if they would like to break the loop or continue through it, lower and .strip to standarnize the answers that could come in. 

print('Thanks for playing!')            # A customary end message for user, prints in terminal. 