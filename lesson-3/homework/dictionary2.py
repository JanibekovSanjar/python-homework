dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer",
    "country": "USA"
    }
k = input("Enter key: ")
print("Key doesn't found" if k not in dictionary else dictionary.get(k))