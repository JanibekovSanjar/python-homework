tuple1 = ('banana', 'eagle', 'lemon', 'mountain', 'rock', 'stone','rock')
a = list(tuple1).copy()
element = input("Enter an element to remove:\n>>>")
if element in tuple1:
    a.remove(element)
print(tuple(a))