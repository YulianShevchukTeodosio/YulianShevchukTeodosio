import random

n = random.randint(0, 1)

guess = int(input("Guess The Number:" ))


if guess == n:
    print("You Won")

if guess < n:
    print("Your Guess Is LOWER")
    while True:
        guess_sec = int(input("Guess Again:" ))
        if guess_sec == n:
            print("You Won")
            break
        elif guess_sec < n:
            print("Your Guess Is LOWER")
        elif guess_sec > n:
             print("Your Guess Is BIGGER")

if guess > n:
    print("Your Guess Is BIGGER")
    while True:
        guess_sec = int(input("Guess Again:" ))
        if guess_sec == n:
            print("You Won")
            break
        elif guess_sec < n:
            print("Your Guess Is LOWER")
        elif guess_sec > n:
             print("Your Guess Is BIGGER")