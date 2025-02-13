tuple1 = ('lemon','banana',"mountain",'eagle',"rock",'stone','lemon','eagle')
element = input("Enter the element from the list:\n>>>")
indices = tuple(n for n in range(0,len(tuple1)) if tuple1[n] == element)
print(indices)