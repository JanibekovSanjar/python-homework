from collections import defaultdict
default_dictionary = defaultdict(lambda: "Key not found", {
    "name": "Cristiano",
    "surname": "Ronaldo",
    "age": "39",
    "occupation": "Footballer",
    "country": "Saudi Arabia",
    "city": "Riyadh",
    "goals": 920
})

k = "team"
print(default_dictionary[k])