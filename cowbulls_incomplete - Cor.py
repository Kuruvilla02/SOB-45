import random
def compare_numbers(number, user_guess):
    if user_guess == number[cowbull[1]]:  #my code
        cowbull[1]+=1                 #cowbull1 is bull and cowbull0 is cow
    elif user_guess in number:
        cowbull[0]+=1
    return cowbull
playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
cowbull = [0,0]
guesses = 0
print(number)    #Iftp there was no ()
print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("We start with first digit")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")
while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1
    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break
    else:
        print("Your guess isn't quite right, try again.")