# Task 45 - Write a script that makes the computer play Jokenpo with you

from time import sleep

from random import randint

print(
    """Your options:
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS"""
)

userOption = int(input("What is your play? "))

if userOption > 2 or userOption < 0:
    print("Invalid play")
else:
    items = ("ROCK", "PAPER", "SCISSORS")

    botOption = randint(0, 2)

    user = items[userOption]
    bot = items[botOption]

    print("JO")
    sleep(0.4)
    print("KEN")
    sleep(0.4)
    print("PO!!!")

    print("=" * 20)
    print(f"USER played {user}")
    print(f"BOT played {bot}")
    print("=" * 20)

    if (
        (user == "ROCK" and bot == "SCISSORS")
        or (user == "PAPER" and bot == "ROCK")
        or (user == "SCISSORS" and bot == "PAPER")
    ):
        print("USER WINS!")
    elif (
        (bot == "ROCK" and user == "SCISSORS")
        or (bot == "PAPER" and user == "ROCK")
        or (bot == "SCISSORS" and user == "PAPER")
    ):
        print("BOT WINS!")
    else:
        print("DRAW!")
