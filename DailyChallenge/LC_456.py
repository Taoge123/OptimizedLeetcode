

class Solution:
    def find132pattern(self, nums):

        mid = float('-inf')
        stack = []

        for item in nums[::-1]:
            if item < mid:
                return True

            while stack and stack[-1] < item:
                mid = stack.pop()

            stack.append(item)

        return False

