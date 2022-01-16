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


class SolutionMemo2:
    def minDistance(self, houses, k: int) -> int:
        houses.sort()
        memo = {}
        return self.dfs(houses, 0, k, memo)

    def dfs(self, nums, i, k, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        n = len(nums)
        if i == n and k == 0:
            return 0
        if i == n or k == 0:
            return float('inf')

        res = float('inf')
        for j in range(i, n):
            res = min(res, self.dfs(nums, j + 1, k - 1, memo) + self.cost(nums, i, j))

        memo[(i, k)] = res
        return res

    def cost(self, nums, i, j):
        mid = (i + j) // 2
        res = 0
        for k in range(i, j + 1):
            res += abs(nums[k] - nums[mid])
        return res




class SolutionMemo:
    def minDistance(self, houses, k: int) -> int:

        memo = {}
        houses.sort()
        return self.dfs(houses, 0, k, memo)

    def dfs(self, nums, i, k, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        @cache
        def cost(i, j):
            mid = nums[(i + j) // 2]
            dist = 0
            for k in range(i, j + 1):
                dist += abs(nums[k] - mid)
            return dist

        n = len(nums)
        if i == n and k == 0:
            return 0
        if i == n or k == 0:
            return float('inf')

        res = float('inf')
        for j in range(i, n):
            res = min(res, self.dfs(nums, j + 1, k - 1, memo) + cost(i, j))
        memo[(i, k)] = res
        return res


#     def cost(self, nums, i, j):
#         mid = nums[(i+j)//2]
#         dist = 0
#         for k in range(i, j+1):
#             dist += abs(nums[k] - mid)
#         return dist


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







