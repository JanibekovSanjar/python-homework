list1 = ['lemon','banana',"mountain",'eagle',"rock", 'stone']
lenth_of_list = len(list1)
print(f"{list1[lenth_of_list//2]}" if lenth_of_list%2 else f"{list1[lenth_of_list//2-1]} and {list1[lenth_of_list//2]}")