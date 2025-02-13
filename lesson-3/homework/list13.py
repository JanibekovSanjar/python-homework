mylist = ["apple", 'banana', 'orange', 'grape', "dragon fruit"]
print(mylist)
element = input("Enter an element from the list:\n>>>")
print(mylist.index(element.lower()) if element in mylist else f"{element} is not in the list")
