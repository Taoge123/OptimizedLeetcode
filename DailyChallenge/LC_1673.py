


class Solution:
    def mostCompetitive(self, nums, k: int):
        stack = []
        count = len(nums) - k
        # if count >= len(nums):
        #     return []
        for num in nums:
            while stack and stack[-1] > num and count:
                stack.pop()
                count -= 1
            stack.append(num)
        while count:
            stack.pop()
            count -= 1

        return stack

