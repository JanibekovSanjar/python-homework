dictionary1 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Developer",
    "country": "USA"
}
k = list(dictionary1.keys())

key1 = k[0]
print(f"{key1} : {dictionary1.get(key1)}" if dictionary1 else "Dictionary is empty")