"""This is snake water gun game where snake drink water and have a fear of gun,
water: soaks the gun and it stops working and have fear of snake, and
gun: from last two statements you know what gun can do and whose gun has fear of """
import random
print("lets play snake water gun")
a = 0
while a < 10:
    a = a+1
    gam = ("snake", "water", "gun")
    cpu = random.choice(gam)
    human = int(input("press 1 for snake, 2 for water and 3 for gun\n"))
# its only for purpose to make program more readable
    if human == 1:
        print("Your choice is snake")
    elif human == 2:
        print("Your choice is water")
    elif human == 3:
        print("Your choice is gun")
    print("the computer choice is", cpu)
# To show the final result
    if cpu == "snake" and human == 1:
        result = "this game is tie and have no result"
        print(result)
    elif cpu == "water" and human == 2:
        result = "this game is tie and have no result"
    elif cpu == "gun" and human == 3:
        result = "this game is tie and have no result"
    elif cpu == "snake" and human == 2:
        result = "you lose"
    elif cpu == "water" and human == 3:
        result = "you lose"
        print(result)
    elif cpu == "gun" and human == 1:
        result = "you lose"
        print(result)
    elif cpu == "water" and human == 1:
        result = "you win"
        print(result)
    elif cpu == "gun" and human == 2:
        result = "you win"
        print(result)
    elif cpu == "snake" and human == 3:
        result = "you win"
        print(result)

    with open("game.txt", "a") as f:
        f = f.write(result + "\n")
# for evaluation who win in 10 rounds
file = open("game.txt", "rt")
game = file.read()
won = game.count("you win")
print('Number of win :', won)
loss = game.count("you lose")
print('Number of losses :', loss)
if won > loss:
    print("Congratulations..!!you won the finale")
elif won == loss:
    print("sorry..!! No Result: Tie")
elif won < loss:
    print("Loser..!! You lost the finale")
print("THANK YOU FOR PLAYING - GAME OVER")
file = open("game.txt", "r+")
file.truncate(0)
