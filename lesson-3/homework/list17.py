import itertools
list1 = ['banana ', 'kite' , 'lemon ' , 'quartz' ,'mountain']
list2 = ['eagle', 'apple', 'tiger', 'Nissan']
combined_list = list(itertools.chain(list1, list2))
print(combined_list)