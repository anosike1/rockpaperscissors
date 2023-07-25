# import the random module
from random import *

# create a library of ROCK, PAPER and SCISSORS
options = ["rock","paper","scissors"]

# use the choice method to get a random element from the list
# this is used to denote the computer's choice
comp = choice (options)

# get the index of the computer's choice from the list
com_index = options.index(comp)

# set a True boolean and assign a variable, cont (this will serve as some sort of SWITCH)
cont = True

# as long as this boolean is True - or let's say this SWITCH is on
# the events which you create under it will keep running
while cont:

    # you will be asked to choose numbers to represent ROCK, PAPER, or SCISSORS
    selekt = int(input ("What do you choose? Type 0 for ROCK, 1 for PAPER, and 2 for SCISSORS: "))

    print (f"You chose {options[selekt]}. Computer chose {options[com_index]}")
    
    # create the win, lose, and tie conditions
    # ensure that the accepted options are below 3
    if selekt > com_index and selekt < 3:
        print ("You win!")

    elif selekt < com_index and selekt < 3:
        print ("You lose!")

    elif selekt == com_index and selekt < 3:
        print ("It's a tie.")

    # if the users enter 3 or above, display WRONG OPTION
    else:
        print ("wrong option")
    
    # give an option to retry
    retry=input ("Would you like to retry? Type 'Y' for YES and any other key for NO: ").lower()
    
    if retry =='y' or retry == 'yes':
        continue
    
    else:
        break
        print ("Goodbye!")