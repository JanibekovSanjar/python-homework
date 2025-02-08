from datetime import date
name = input("Enter your name: ")
year = int(input("Enter your year of birth: "))
current_year = date.today().year
age = current_year - year
print(f"Hi {name}, you are {age} years old")