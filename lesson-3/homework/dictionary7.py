dictionary1 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Developer",
    "country": "USA"
    }
key = input("Enter key to be removed from dictionary:\n>>>")
dictionary1.pop(key, "Key not found")
print(dictionary1)