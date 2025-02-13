fruits = ["apple", 'banana', 'orange', 'grape']
fruit = input("Enter a fruit:\n>>>")
print(f"We have {fruit}" if fruits.count(fruit) else f"We don't have {fruit}")