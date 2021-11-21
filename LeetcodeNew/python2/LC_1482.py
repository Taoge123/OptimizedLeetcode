"""
X, _, _, _, _
X, _, _, _, X
X, _, X, _, X
X, _, X, _, X
X, _, X, _, X
X, _, X, _, X
X, _, X, _, X
X, _, X, _, X
X, _, X, _, X
X, X, X, X, X

m = 3
k = 2

xx xx xx

n < m * k : return -1

day ->

left = 1
right = max()

if count(mid) > m:
    right = mid
else:
    left = mid + 1
return left

2. count()

3.

"""

class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:

        n = len(bloomDay)

        # total is less then m * k flowers
        if n < m * k:
            return -1

        left, right = 1, max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if self.count(bloomDay, mid, k) >= m:
                right = mid
            else:
                left = mid + 1
        return left

    def count(self, nums, day, k):
        count = 0
        summ = 0
        for num in nums:
            if num > day:
                summ = 0
            else:
                summ += 1
                if summ == k:
                    count += 1
                    summ = 0
        return count







