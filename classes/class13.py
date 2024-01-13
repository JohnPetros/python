# Class 13 - Dictionaries

people = {
    "name": "Gustav",
    "gender": "male",
    "age": 22,
}

print(f'{people["name"]} is {people["age"]} years old and of {people["gender"]} gender')

for key, value in people.items():
    print(f"{key} = {value}")

del people["gender"]

# print(people["gender"]) 🚫

Brasil = []

state1 = {"uf": "RJ", "name": "Rio de Janeiro"}
state2 = {"uf": "SP", "name": "São Paulo"}

Brasil.append(state1)
Brasil.append(state2)

print(Brasil[0]["name"])
print(Brasil[1]["name"])
