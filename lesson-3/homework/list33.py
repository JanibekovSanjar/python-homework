list1 = ['lemon','banana',"mountain", 'lemon','mountain','eagle', 'apple', "banana",'mountain', 'lemon']
print(list1)
element = input("Enter the element from the list:\n>>>")
indices = [n for n in range(0,len(list1)) if list1[n] == element]
print(indices)