# Task 53 - Write a script that reads any number and informs whether is a palindrome, disregarding blank spaces

phrase = input("Enter a phrase: ").strip()

reversePhrase = ""

for letter in range(-1, -1 - len(phrase), -1):
    reversePhrase += phrase[letter]

if reversePhrase.upper().replace(" ", "") == phrase.upper().replace(" ", ""):
    print("IT IS a palindrome")
else:
    print("IT NOT IS a palindrome")

# other solution

joinedWords = "".join(phrase.split())

reversedJoinedWords = joinedWords[::-1]

if joinedWords == reversedJoinedWords:
    print("IT IS a palindrome")
else:
    print("IT NOT IS a palindrome")
