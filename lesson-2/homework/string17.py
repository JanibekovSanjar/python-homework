string = input("Enter a string:\n>>>")
vowels = ["a", "e", "i", "o", "u"]
for letter in string:
    if letter.lower() in vowels:
        string = string.replace(letter,"*")
print(string)      