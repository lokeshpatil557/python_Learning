print("Welcome to Guess game. You have  5 tries . Show us what you have")
n = 18
Chances = 0
while Chances < 5:

    num = int(input("Enter the number \n"))
    if num < n:
        print("your number is smaller")
        Chances = Chances + 1
        Chancesleft = 5 - Chances
        print("the chances you have left are", Chancesleft)
    elif num > n:
        print("your number is greater")
        Chances = Chances + 1
        Chancesleft = 5 - Chances
        print("the chances you have left are", Chancesleft)
    elif num == n:
        print("Congratulation!your guess is right")
        Chances = Chances + 1
        Chancesleft = 5-Chances
        print("the chances you have left are", Chancesleft)
        break
