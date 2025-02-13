mylist = ["apple", 'banana', 'orange', 'grape', "dragon fruit"]
element = input("Enter an element to add to the list:\n>>>")
index = int(input("Enter index for element:\n>>>"))
mylist.insert(index,element)
print(mylist)