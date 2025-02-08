string = input()
digit_exist = 0
for letter in string:
    if letter.isdigit():
        digit_exist = 1
        break
print("There is a digit in this string" if digit_exist == 1 else "There is not a digit in this string")