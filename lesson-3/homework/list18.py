list1 = ['banana', 'kite' , 'lemon' , 'quartz' ,'mountain','eagle', 'apple']
list2 = ['eagle', 'apple', 'lemon']
is_sublist = True
for element in list2:
    if element not in list1:
        is_sublist = False
        break
print("list2 is sublist of list1" if is_sublist else "list2 is not sublist of list1")