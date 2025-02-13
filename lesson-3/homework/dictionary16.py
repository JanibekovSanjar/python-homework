dictionary1 = {
    "name": "Cristiano",
    "surname": "Ronaldo",
    "age": "39",
    "occupation": "Footballer",
    "country": "Saudi Arabia",
    "city": "Riyadh",
    "goals": {"Juventus": 101, "Real Madrid": 450, "Sporting CP": 5, "Portugal": 109}
}
include = False
for k, v in dictionary1.items():
    if type(v) == dict:
        include = True
        break
print("Dictionary includes a dictionary" if include else "Dictionary does not include a dictionary")