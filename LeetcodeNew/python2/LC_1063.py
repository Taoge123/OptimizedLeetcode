"""
固定每个num当做leftmost, 找出所有符合规定的subarry

1 2 3 4 5 是个 special case
1 2 3 4 5 -inf
"""


class Solution:
    def validSubarrays(self, nums) -> int:
        nums.append(float('-inf'))
        stack = []
        count = 0
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                count += i - stack.pop()
            stack.append(i)
        return count



