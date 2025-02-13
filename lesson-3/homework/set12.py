set1 = {'a', 'b', 'c','f'}
element = input("Enter the element to append to set1:\n>>>")
if element in set1:
    print("Element already exists in the set")
else:
    set1.add(element)
    print(set1)