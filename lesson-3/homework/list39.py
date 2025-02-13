list1 = ['lemon','banana',"mountain",'eagle',"rock",'stone']
middle = len(list1)//2
new_list = []
new_list.append(list1[:middle])
new_list.append((list1[middle:]))
print(new_list)