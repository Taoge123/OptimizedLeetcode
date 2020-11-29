"""
https://www.youtube.com/watch?v=SD99cAHkRow
"""


class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        odd, even = 0, 0
        # maxi = 0
        n = len(nums)
        if n < 3:
            return 0

        for i in range(1, n, 2):
            if i == n - 1:
                maxi = nums[i - 1]
            else:
                maxi = min(nums[i - 1], nums[i + 1])

            if nums[i] >= maxi:
                odd += 1 + nums[i] - maxi

        for i in range(0, n, 2):
            if i == 0:
                maxi = nums[i + 1]
            elif i == n - 1:
                maxi = nums[i - 1]
            else:
                maxi = min(nums[i - 1], nums[i + 1])

            if nums[i] >= maxi:
                even += 1 + nums[i] - maxi

        return min(odd, even)


class Solution2:
    def movesToMakeZigzag(self, nums) -> int:
        def isValid(i):
            return 0 <= i < len(nums)

        n = len(nums)
        odd, even = 0, 0
        for i in range(n):
            left = right = float('inf')
            if isValid(i - 1):
                left = nums[i - 1]
            if isValid(i + 1):
                right = nums[i + 1]
            move = nums[i] - min(left, right) + 1
            if 0 <= move != float('inf'):
                if i % 2 != 0:
                    odd += move
                else:
                    even += move

        return min(odd, even)

