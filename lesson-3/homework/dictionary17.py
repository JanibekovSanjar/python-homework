dictionary1 = {
    "name": "Cristiano",
    "surname": "Ronaldo",
    "age": "39",
    "occupation": "Footballer",
    "country": "Saudi Arabia",
    "city": "Riyadh",
    "goals": {"Juventus": 101, "Real Madrid": 450, "Sporting CP": 5, "Portugal": 109}
}
print(dictionary1.get("goals").get("Real Madrid")) # 450