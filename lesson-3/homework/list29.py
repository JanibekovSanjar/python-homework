list1 = ['lemon','banana',"mountain",'eagle',"rock", 'stone']
index = int(input(f"Enter the index:(from 0 to {len(list1)-1})\n>>>"))
if index in range(0,len(list1)):
    list1.remove(list1[index])
    print(list1)
else:
    print(f"{index} is out of range")

