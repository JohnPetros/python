# Task 26 - Write a script that reads a phrase and displays
# - How many times does the letter "A" appear in the phrase
# - At what position does the letter "A" first appear in the phrase
# - At what position does the letter "A" last appear in the phrase

name = input('Type a phrase: ').strip().upper()

print(f'The letter A appears {name.count("A")} times in the name')
print(f'The first letter A appears at {name.find("A") + 1} position')
print(f'The last letter A appears at {name.rfind("A") + 1} position')
