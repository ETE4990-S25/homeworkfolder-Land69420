# %% [markdown]
# # Lists - Maggie Tapia and Alexander Land
# 
# ## Background
# Lists are one of the most commonly used data structures in Python and are very similar to arrays from other programming languages. A list can store many items or values inside of one overall object or structure, unlike a variable which can only store one item or value inside one object. 
# 
# The items in a list can be accessed by using what is called an “index” value, which simply refers to the position of a certain item inside of a list, as lists are ordered from item 0 to the number of elements - 1. Therefore a list with 5 elements will have index positions 0 through 4. 
# 
# Any data can be stored inside a list, numbers, strings, or objects, but it is common practice to only have one data type per list. Therefore if my list has integers, it would ONLY have integers, not strings, doubles, objects, etc.

# %% [markdown]
# ## Mini-project - Guessing game
# Create a number guessing game and set a secret number at the beginning of the program. 
# The program will ask the player to enter a number to guess what the number is, then it’ll inform the player if they got it right or wrong.

# %%
# put your code here

secretNumber = 1
guess = int(input("make a guess"))
if guess == secretNumber:
    print("correct")
else:
    print("incorrect")


# %% [markdown]
# ## Mini-Project - Dice Roll
# 
# Part 1:
# Create a random number generator using dice. 
# You must create at least 5 dice
# The game must use conditionals (If, Else, Elif)
# The game must use nested conditionals (if 0=0:if 1=1: do something)
# 
# What lists should we create for the project?
# How many loops do we need?
# 
# Part 2:
# Create a list to store your gameplay. 
# Create at least 2 lists to store your game statistics.
# 
# Part 3:
# At the end of the output your gameplay statistics
# 
# Part 4:
# Exchange code with your partner and begin adding comments on improvements (save your original version)
# 
# Part 5:
# Return the code and create a comparison 
# 
# Part 6:
# Upload the code and comparison it to Canvas. 
# 
# 
# ## Part 3 was done with two different methods: first method saving wins and losses, second is saving the rolls then comparing after 
# 

# %%
# Alexander Land & Maggie Tapia 
import random
import os

os.system('cls')
#clears screen


def rollDice():
    return random.randint(1,6)
    #idk any other way to write this



def printStats(playerWinLoss):
    wins = 0
    ties = 0
    for round in playerWinLoss: #increments for wins and ties 
        if round == 1:
            wins += 1

        if round == 2: 
            ties += 1
    winrate = wins/len(playerWinLoss)

    print("YOUR STATS\n----------")
    print("you won", wins, "games")
    print("you tied", ties,"games")
    print("your winrate is ", winrate)
    return 0

def printStatsMethod2(ListofmyRolls,ListofPuterRolls):
    wins = 0
    losses = 0
    ties = 0

    for i in range(0,len(ListofmyRolls)): #i iterates from 0 to the number of games played
        if ListofmyRolls[i] > ListofPuterRolls[i]: #compares each game to check for win or loss
            wins += 1
        elif ListofmyRolls[i] < ListofPuterRolls[i]:
            losses += 1
        else ListofmyRolls[i] == ListofPuterRolls[i]:#else
            ties += 1
    
    winrate = wins/(wins + losses + ties) 

    print("YOUR STATS Method 2\n----------")
    print("you won", wins, "games")
    print("you tied", ties,"games")
    print("your winrate is ", winrate)






def main():
    print("Welcome to the Dice Rolling Game!")
    print("You and Puter will each roll a dice, and the one with the higher number wins.\n")
    #we stole the intro text 

    playerWinLoss = []
        #declared win loss array

    ListofPuterRolls = []
    ListofmyRolls = []
        #lists for method two stats


    while True:
        input("Press Enter to roll")

        myRoll = rollDice()
        ListofmyRolls.append(myRoll) #stores each roll for stats later

        PuterRoll = rollDice()
        ListofPuterRolls.append(PuterRoll)

        print("you rolled:", myRoll)
        print("Puter rolled:", PuterRoll)

        if myRoll > PuterRoll:
            print("win")
            playerWinLoss.append(1)

        elif PuterRoll > myRoll:
            print("lose")
            playerWinLoss.append(0)

        else:
            print("tie")
            playerWinLoss.append(2)

        print("")

        

        playAgain = input("would u like to play again (y/n):").lower()

        if playAgain !="y": # if y isn't pressed, while loop gets broken and stats are shown
            break

        

    printStats(playerWinLoss)
    print("")
    printStatsMethod2(ListofmyRolls, ListofPuterRolls)



if __name__ == "__main__":
    main()



# %%
## Sample code
Below you will find a Chat GPT generated Dice game.

Lets talk about it. 

# %%
import random


def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Game!")
    print("You and the computer will each roll a dice, and the one with the higher number wins.")

    while True:
        input("Press Enter to roll the dice...")
        
        user_roll = roll_dice()
        computer_roll = roll_dice()

        print("You rolled:", user_roll)
        print("Computer rolled:", computer_roll)

        if user_roll > computer_roll:
            print("Congratulations! You win!")
        elif user_roll < computer_roll:
            print("Sorry, you lost. Better luck next time!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

# %%



