import random

while True:
    number=random.randint(1,100)
    attempts =7
    print("NUMBER GUESSING GAME")
    print("guess the number between 1 and 100")
    print("You have 7 attempts")
    for i in range(1,attempts+1):
        guess =int(input("Enter your guess:"))
        if guess>number:
            print("Too high!")
        elif guess<number:
            print("too low!")
        else:
            print("Congo You guessed the number in",i,"attempts")
            break
        print("Attempts remaining:",attempts-i)
    else:
        print("Sry You failed.")
        print("The number was:",number)
    choice = input("Do you want to play again? (yes/no):")
    if choice !="yes":
        print("tq for playing")
        break