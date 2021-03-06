
"""
nums ->

count[i] : how many objects for the i-th object
quantity[i] : how many same objects required by the i-th customer

bitmask: 2^m => all the states that presents who are satisfied

  50 * 1024
dp[i][state] : weather we can satisfy customers of state by using the first i objects

res = dp[n][11..11]
res = dp[n][(1<<m)-1]
dp[i][state] == True iff
-> if we can use count[i] to satisfy a subset of state
-> if we can use the first i-1 objects to satisfy state - subset
    -> dp[i-1][state - subset] == True

count[i] >= quantity[subset_1] + quantity[subset_2] + .....


"""

import collections
import functools


class Solution:
    def canDistribute(self, nums, quantity) -> bool:
        count = collections.Counter(nums)
        nums = sorted(count.values())
        n = len(nums)
        m = len(quantity)
        N = (1 << m) - 1
        table = collections.defaultdict(int)
        for state in range(1, 1 << m):
            for i in range(m):
                if (1 << i) & state:
                    table[state] += quantity[i]
            # print(state, table[state], bin(table[state])[2:])

        @functools.lru_cache(None)
        def dfs(pos, state):
            if state == 0:
                return True

            if pos == n:
                return False

            subset = state
            while subset:
                if table[subset] <= nums[pos] and dfs(pos + 1, state ^ subset):
                    return True
                subset = (subset - 1) & state

            return dfs(pos + 1, state)
        return dfs(0, N)



class SolutionDFS:
    def canDistribute(self, nums, quantity) -> bool:
        count = collections.Counter(nums)
        m = len(quantity)

        # we only need at most m diff numbers, so we choose the ones which are most abundant
        nums = sorted(count.values())[-m:]

        # If the customer with most quantity required cant be fulfilled, we dont need to go further and answer will be false
        quantity.sort(reverse=True)

        def dfs(nums, quantity, customer):
            if customer == len(quantity):
                return True

            for i in range(len(nums)):
                if nums[i] >= quantity[customer]:
                    nums[i] -= quantity[customer]
                    if dfs(nums, quantity, customer + 1):
                        return True
                    nums[i] += quantity[customer]
            return False

        return dfs(nums, quantity, 0)









