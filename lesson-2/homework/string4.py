a = input("Enter a word:\n>>>")
b = a[-1::-1]
print(f"{a} is palindrome" if a==b else f"{a} is not palindrome")   