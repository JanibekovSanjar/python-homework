num_list = [1,4,6,3,7,12,14,15]
print(num_list)
start = int(input(f"Enter the starting index(from 0 to {len(num_list)}):\n>>>"))
end = int(input(f"Enter the ending index(from {start+1} to {len(num_list+1)}):\n>>>"))
sublist = num_list[start:end+1]
sublist.sort()
print(f"Biggest element of the sublist: {sublist[-1]}") 