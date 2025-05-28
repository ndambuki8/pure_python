# creating a dictionary
country_capitals = {
    "Germany": "Berlin",
    "Canada" : "Ottawa",
    "England" : "London",
    254: "Kenya"
}

country_capitals[255] = "Uganda"

# del country_capitals[254]
country_capitals.pop(254)
country_capitals[254] = "Tz"
# print(country_capitals)
# print(country_capitals["Canada"])
# print(country_capitals["England"])
# print(country_capitals.get(254))

# print(len(country_capitals))

# print a dictionary keys one by one
# print("Keys:")
# for country in country_capitals:
#     print(country)

# print("\nValues:")

# for country in country_capitals:
#     print(country_capitals.get(country))

for values in country_capitals.values():
    print(values)