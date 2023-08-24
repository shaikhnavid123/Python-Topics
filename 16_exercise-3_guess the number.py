n = 35

# no. of guesses 9  a
# print no. of guesses left
# No. of guesses he took to finish
#game over

"""
while(True):
    inp = int(input("Guess a number :"))
    if inp==35:
        print("Congrats! You've guess the correct Number")
        break
    if inp>35:
        print("You've entered greater number")
        print("Try again!")
        continue
    if inp<35:
        print("You've entered smaller number")
        print("Try again!")
    else:
        print("Try again!")
        continue
"""

n = 18

number_of_guesses=1
print("Number of guesses is limited to only 9 times :")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number :"))
    if guess_number<18:
        print("You've entered lesser number")
    elif guess_number>18:
        print("You've entered greater number")
    else:
        print("You won!\n")
        print(9-number_of_guesses, "no. of guesses you required to finish")
        break
    print(9-number_of_guesses, "no. of guesses left")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("Game Over!")