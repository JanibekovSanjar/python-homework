tuple1 = ('banana', 'eagle', 'lemon', 'mountain', 'rock', 'stone','rock')
middle = len(tuple1)//2
new_tuple = []
new_tuple.append(tuple1[:middle])
new_tuple.append(tuple1[middle:])
print(tuple(new_tuple))