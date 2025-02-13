tuple1 = ('lemon','banana',"mountain",'eagle',"rock",'stone')
element = input("Enter the element:\n>>>")
print(f"{element} is exist in the list" if element in tuple1 else f"{element} is not exist in the list")