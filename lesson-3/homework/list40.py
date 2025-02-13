nums = [5,8,12,3,7,10,8,15,8,19,7,5,10]
unique_list = []
for num in nums:
    if num not in unique_list:
        unique_list.append(num)
print(unique_list)