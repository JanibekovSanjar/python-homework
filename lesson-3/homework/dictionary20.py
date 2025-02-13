dictionary = {
    "name": "Cristiano",
    "surname": "Ronaldo",
    "age": "39",
    "occupation": "Footballer",
    "country": "Saudi Arabia",
    "city": "Riyadh",
    "goals": 920
}
sorted_dict = {k: dictionary[k] for k in sorted(dictionary)}
print(sorted_dict)