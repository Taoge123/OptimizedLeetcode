"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]

"""

import math

class Solution:
    def getFactors(self, n: int):
        if n == 1:
            return []
        res = []
        self.dfs(n, 2, [], res)
        return res

    def dfs(self, n, pos, path, res):
        if path:
            res.append(path + [n])

        for i in range(pos, int(math.sqrt(n)) + 1):
            if n % i == 0:
                self.dfs(n // i, i, path + [i], res)




