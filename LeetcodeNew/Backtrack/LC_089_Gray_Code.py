
"""

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code.
A gray code sequence must begin with 0.

Example 1:

Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.

00 - 0
10 - 2
11 - 3
01 - 1
Example 2:

Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].



dp is a good way to solve this problem.
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


