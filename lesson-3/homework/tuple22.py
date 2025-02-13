start = int(input("Enter the starting point:\n>>>"))
end = int(input("Enter the ending point:\n>>>"))
range_tuple = tuple(range(start,end+1))
print(*(n for n in range_tuple))