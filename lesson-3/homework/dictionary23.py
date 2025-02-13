dictionary1 = {
    "name": "Cristiano",
    "surname": "Ronaldo",
    "age": "39",
    "occupation": "Footballer",
    "country": "Saudi Arabia",
    "city": "Riyadh",
    "goals": 920
}
dictionary2 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Developer",
    "country": "USA"
}
common = set(dictionary1.keys())&set(dictionary2.keys())
print("Dictionaries have common keys" if common else "Dictionaries doesn't have common keys")