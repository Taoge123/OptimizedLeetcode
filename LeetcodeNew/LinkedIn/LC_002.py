# dictionary
def twoSum1(self, nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if target - num in dic:
            return (dic[target - num] + 1, i + 1)
        dic[num] = i


# two-pointer
def twoSum(self, nums, target):
    nums = enumerate(nums)
    nums = sorted(nums, key=lambda x: x[1])
    l, r = 0, len(nums) - 1
    while l < r:
        if nums[l][1] + nums[r][1] == target:
            return sorted([nums[l][0] + 1, nums[r][0] + 1])
        elif nums[l][1] + nums[r][1] < target:
            l += 1
        else:
            r -= 1