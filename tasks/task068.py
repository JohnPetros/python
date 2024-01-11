# task 68 - Write a script that plays odd or even with your computer. The game will only stop when the user loses, displaying the total of sequential victories they have achieved at the end of the game.

from random import randint

print("-=" * 20)
print("LET'S PLAY ODD OR EVEN")
print("-=" * 20)

victories = 0

while True:
    userNumber = int(input("Enter a number: "))

    while True:
        numberType = input("Odd or Even? [O/E] ").strip().upper()
        if numberType not in ["O", "E"]:
            print(
                "Invalid response! Choose between Odd (entering O) or Even (entering E)"
            )
        else:
            break

    botNumber = randint(1, 10)

    total = userNumber + botNumber

    result = "EVEN" if total % 2 == 0 else "ODD"

    hasUserWin = numberType == result[0]

    print(
        f"You play the number {userNumber} and the bot the number {botNumber}. The total of {total} is {result}."
    )

    if hasUserWin:
        print("YOUR WIN!")
        victories += 1
    else:
        print("YOUR LOSE!")
        break


print(f"GAME OVER! You won {victories} times.")
