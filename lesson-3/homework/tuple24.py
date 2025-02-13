tuple1 = ('banana', 'eagle', 'lemon', 'mountain', 'rock', 'stone','rock')
reversed_tuple = tuple(reversed(list(tuple1)))
print("Tuple is palindrome" if reversed_tuple==tuple1 else "Tuple is not palindrome")