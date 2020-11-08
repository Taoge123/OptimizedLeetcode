import functools

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @functools.lru_cache(None)
        def power(x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + power(x // 2)
            return 1 + power(3 * x + 1)

        return sorted(range(lo, hi + 1), key=power)[k - 1]




class SolutionTony:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @functools.lru_cache(None)
        def power(x):
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + power(x // 2)
            return 1 + power(3 * x + 1)

        # nums = sorted(range(lo, hi+1))[k-1]
        nums = [[power(num), num] for num in range(lo, hi + 1)]
        nums.sort()
        return nums[k - 1][1]

