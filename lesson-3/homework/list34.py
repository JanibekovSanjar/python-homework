nums = [5,8,12,3,7,10,15]
k = 4
rotated_list = nums[-k:]+nums[:-k]
print(rotated_list)