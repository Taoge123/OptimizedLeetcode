class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)

        res = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[l] + nums[i] + nums[r]
                if abs(s - target) < abs(res - target):
                    res = s
                elif s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res

