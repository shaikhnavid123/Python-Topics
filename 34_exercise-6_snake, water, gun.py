from random import choice

p = 0
Snake = 2
Water = 3
Gun = 4
You = 0
Com = 0
q = 0

print("Let's start the game!")
print("Type alphabet in capital letters :")
while p<10:
    i = str(input("S/W/G"))
    if i=='S' :
        j = choice([Water, Gun])
        if Snake*j == 6:
            print("You Won")
            You = You+1
        else:
            print("You Lose")
        Com = Com+1
    if i=='W' :
        j = choice([Snake, Gun])
        if Water*j == 6:
            print("You Lose")
            Com = Com+1
        else:
            print("You Won")
            You = You+1
    if i == 'G' :
        j = choice([Water, Snake])
        if Water*j == 12:
            print("You Lose")
            Com = Com+1
        else:
            print("You Won")
            You = You+1
    p=p+1
print("Game Over")
print("Your Score", You)
print("Opponent Score", Com)