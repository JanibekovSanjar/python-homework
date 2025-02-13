import random
start = int(input("Enter the starting number:\n>>>"))
end = int(input("Enter the ending number:\n>>>"))
num_of_elemends = int(input("How many random numbers do you want to generate?:\n>>>"))
random_set = {random.randint(start, end) for i in range(num_of_elemends)}
print(random_set)