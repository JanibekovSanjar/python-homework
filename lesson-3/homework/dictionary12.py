dictionary1 = {
    "name": "John",
    "age": "30",
    "city": "New York",
    "occupation": "Developer",
    "country": "USA"
    }
v = input("Enter a value:\n>>>")
num_of_values = list(dictionary1.values()).count(v)
print(f"The value '{v}' is present {num_of_values} times in the dictionary.")