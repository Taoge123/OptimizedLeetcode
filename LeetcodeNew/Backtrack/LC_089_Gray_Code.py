
"""dp is a good way to solve this problem.
Every time when you increase the n by 1, you add 1 more digit in the front,
which means you add 2**(n-1) to dp[n-1][-1] for you second half number list
n = 1: [0,1]
n = 2: [0,1]+ [2+0, 2+1][::-1] = [0,1,3,2]
n = 3: [0,1,3,2] + [4 + 0, 4 +1, 4 +3, 4 + 2][::-1] = [0,1,3,2,6,7,5,4]

"""

class Solution:
    def grayCode(self, n):
        dp = [[0]]
        for i in range(1,n+1):
            dp.append(dp[i-1] + [2**(i-1) + j for j in dp[i-1]][::-1])
        return dp[n]


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        def helper(n):
            if n == 1:
                return ['0', '1']
            temp = helper(n - 1)
            return ['0' + x for x in temp] + ['1' + y for y in temp[::-1]]

        if n == 0:
            return [0]
        return [int(x, 2) for x in helper(n)]


class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        re=[0]
        for i in range(n):
            re=re+[2**i+x for x in re[::-1]]
        return re


