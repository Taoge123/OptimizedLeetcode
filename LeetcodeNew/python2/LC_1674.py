"""
1. what is the ultimate pair sum x?
2. how many moves required to make each pair sum equal to x?

    nums[i] + nums[n-1-i] => x
          a < b

0 move : a + b
1 move : [a+b+1, limit + b]
2 move : [limit+b+1, 2*limit]


1 move : [a+1, a+b-1]
2 move : [2, a]


y = 2
default diff = 0

diff[2] = 2
diff[a+1] = -1
diff[a+b] = -1
diff[a+b+1] = +1
diff[limit+b+1] = +1
"""


class Solution:
    def minMoves(self, nums, limit: int) -> int:
        diff = [0] * (200002)
        n = len(nums)

        for i in range(n // 2):
            a = min(nums[i], nums[n - 1 - i])
            b = max(nums[i], nums[n - 1 - i])

            diff[2] += 2
            diff[1 + a] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[limit + b + 1] += 1

        count = 0
        res = float('inf')
        for x in range(2, limit * 2 + 1):
            count += diff[x]
            res = min(res, count)

        return res

