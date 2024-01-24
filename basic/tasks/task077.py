# task 77 -

words = (
    "software",
    "hardware",
    "network",
    "database",
    "algorithm",
    "programming",
    "cybersecurity",
    "computer",
)

for word in words:
    print(f"In the word {word.upper()} we have ", end="")

    for letter in word:
        if letter.lower() in ["a", "e", "i", "o", "u"]:
            print(letter, end=" ")

    print(end="\n")
