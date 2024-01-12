# task 73 - Create a tuple filled with 9 european countries in a random order. After that, display:
# - The first 5
# - The last 4
# - The alphabetical order
# - Portugal's position

countries = (
    "United Kingdom",
    "France",
    "Germany",
    "Italy",
    "Spain",
    "Poland",
    "Portugal",
    "Russia",
    "Sweden",
)

print("=" * 150)
print(f"List of 9 european countries: {countries}")
print("=" * 150)
print(f"The first 5 are: {countries[:5]}")
print("=" * 150)
print(f"The last 4 are: {countries[5:]}")
print("=" * 150)
print(f"In alphabetical order: {sorted(countries)}")
print("=" * 150)
print(f"Portugal is at the {countries.index('Portugal') + 1}º position")
print("=" * 150)
