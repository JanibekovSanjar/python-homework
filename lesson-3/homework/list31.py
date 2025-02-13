num_list = [1,6,3,4,7,3]
num_list = list(set(num_list))
num_list_copy = num_list.copy()
num_of_repeatence = int(input("Enter a number to repeat the elements:\n>>>"))
for num in range(num_of_repeatence-1):
    num_list.extend(num_list_copy)
print(num_list)