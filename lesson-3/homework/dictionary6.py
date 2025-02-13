dictionary1 = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Developer",
    "country": "USA"
    }
dictionary2 = {
    "company": "Google",
    "position": "Software Engineer",
    "location": "Mountain View",
    "salary": 100000,
    "currency": "USD"
}
combined_dictionary = {**dictionary1, **dictionary2}
print(combined_dictionary)