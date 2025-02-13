list1 = ['lemon','banana',"mountain", 'lemon','mountain','eagle', 'apple', "banana",'mountain', 'lemon']
print(list1)
element = input("Enter the element to be replaced:\n>>>")
replacement = input("Enter a word word to replace:\n>>>")
if element in list1:
    index_of_element= list1.index(element)
    list1[index_of_element] = replacement
print(list1)
