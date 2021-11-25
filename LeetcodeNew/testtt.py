
nums = [1,2,3,4,5,6,7,8,9]

for i in range(len(nums)):
    for j in range(i, len(nums)):
        nums[j] = i
    else:
        nums[j] = 9

print(nums)


