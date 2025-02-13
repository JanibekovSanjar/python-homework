dictionary1 = {
    "name": "Cristiano",
    "age": "39",
    "country": "Portugal",
    "occupation": "Footballer",
    "country": "Saudi Arabia",
    "city": "Riyadh",
    "team": "Al Nassr",
    "goals": "39"
}
values = input("Enter a value:\n>>>")
keys = [k for k, v in dictionary1.items() if v == values]
print(keys)
