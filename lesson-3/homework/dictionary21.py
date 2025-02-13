dictionary = {"name": "Cristiano",
    "surname": "Ronaldo",
    "age": "39",
    "occupation": "Footballer",
    "country": "Saudi Arabia",
    "city": "Riyadh",
    "goals": 920}
sorted_dict_by_values = {k: dictionary[k] for k in sorted(dictionary, key=dictionary.get)} 
print(sorted_dict_by_values)