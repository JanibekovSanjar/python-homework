tuple1 = ('banana', 'eagle', 'lemon', 'mountain', 'rock', 'stone','rock')
unique_elements = []
for element in tuple1:
    if element not in unique_elements:
        unique_elements.append(element)
print(tuple(unique_elements))