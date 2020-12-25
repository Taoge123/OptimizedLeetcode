"""
https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/discuss/974594/Python-Accepted-Clean-Greedy-Backtracking-with-Memoriztion
https://leetcode-cn.com/problems/delivering-boxes-from-storage-to-ports/solution/zai-liang-chong-tan-xin-ce-lue-zhong-zuo-qepx/
idx:  1 2 3 4 5
port: 1 2 3 4 5
6 trips

idx:  1 2 3 4 5 6
port: 1 2 3 4 5 5

plan 1:
idx:   1 2 3 4 5  6
port: [1 2 3 4 5] [5]
         6 + 2 = 8

plan 2:
idx:  1 2 3 4  5 6
port: [1 2 3 4] [5 6]
         5 + 2 = 7

dp[i] : the minimum trips to deliver the first i boxes

idx :  i ..... j  j+1
port:  X X X X X   X

# 1 is come back to port
plan1: dp[j] <= dp[i-1] + tripNum[i:j] + 1
plan2: dp[j-2] <= dp[i-1] + tripNum[i:j-2] + 1


"""

import functools

class Solution:
    def boxDelivering(self, boxes, portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)

        @functools.lru_cache(None)
        def dfs(i):
            if i > n - 1:
                return 0

            j = k = i
            b = w = extra = 0

            while j < n and b < maxBoxes and w + boxes[j][1] <= maxWeight:
                b += 1
                w += boxes[j][1]

                if j != i and boxes[j][0] != boxes[j - 1][0]:
                    extra += 1
                    k = j

                j += 1

            # every time going back to home -> add 2
            trip = dfs(j) + extra + 2
            if k != i:
                trip = min(trip, dfs(k) + extra + 1)

            return trip

        return dfs(0)


