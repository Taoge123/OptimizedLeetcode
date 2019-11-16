"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

import collections

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        table = collections.defaultdict(list)
        for i, val in enumerate(ring):
            table[val].append(i)

        rsize = len(ring)
        init = {0 :0}

        for c in key:
            dp = {}
            for i in table[c]:
                dp[i] = float('inf')
                for j in init:
                    dp[i] = min(dp[i], init[j] + min(abs( i -j), rsize - abs( i -j)))
            init = dp

        return min(dp.values()) + len(key)



