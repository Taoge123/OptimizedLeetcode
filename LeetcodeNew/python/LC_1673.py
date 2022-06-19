"""
402. Remove K Digits

1 3 5 7 9

1 3 5 7 9 6 -> then we will remove 7 and 9

1 3 5 6


"""


class SolutionTony:
    def mostCompetitive(self, nums, k: int):
        k = len(nums) - k
        # if k >= len(nums):
        #     return []
        stack = []
        for num in nums:
            while stack and k and stack[-1] > num:
                stack.pop()
                k -= 1
            stack.append(num)

        while k:
            stack.pop()
            k -= 1
        return stack


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


