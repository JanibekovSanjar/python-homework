dictionary1 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Developer",
    "country": "USA"
}

swapped_dictionary = {v: k for k, v in dictionary1.items()}
print(swapped_dictionary)