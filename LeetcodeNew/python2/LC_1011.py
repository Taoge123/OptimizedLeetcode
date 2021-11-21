"""

1.

left = max(nums)
right = sum(nums)

if count(mid) > days:
    left = mid + 1
else:
    right = mid
return left


2. count(nums, target):

3. equal

"""

class SolutionTony:
    def shipWithinDays(self, weights, days: int) -> int:

        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (left+right)//2
            if self.count(weights, mid) > days:
                left = mid+1
            else:
                right = mid-1
        return left

    def count(self, nums, target):
        count = 0
        summ = 0
        for w in nums:
            if summ+w > target:
                count += 1
                summ = 0
            summ += w
        return count + 1



class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        left = max(weights)
        right = left * len(weights) // D
        while left < right:
            mid = (left + right) // 2
            count = 1
            summ = 0
            for w in weights:
                if summ + w > mid:
                    count += 1
                    summ = 0
                summ += w

            if count > D:
                left = mid + 1
            else:
                right = mid

        return left

