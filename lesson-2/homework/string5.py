word = input("Enter a word:\n>>>").lower()
number_of_vowels = 0
number_of_consonants = 0
vowels = {"a", "e", "i", "o", "u"}
for letter in word:
    if letter.isalpha():
        if letter in vowels:
            number_of_vowels+=1
        else:
            number_of_consonants+=1    
print("Number of vowels:",number_of_vowels)
print("Number of consonants:",number_of_consonants)