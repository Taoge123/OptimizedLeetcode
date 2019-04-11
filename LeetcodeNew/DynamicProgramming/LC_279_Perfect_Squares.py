
"""

每一个你不满意的现在，都有一个你没有努力的曾经
https://leetcode.com/problems/perfect-squares/discuss/71475/Short-Python-solution-using-BFS

Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

"""
I just submitted a simple bottom-up DP solution in python and got a TLE. I searched through the discussions and saw many other people are struggling with TLE for their python code.

After struggling with my code a little bit, I finally figure out the issue.
Note that in my accepted code below, my dp array is declared as a class variable.
However, if you uncomment the init function to turn it to an instance variable, 
then you get the TLE error. Thus it is pretty obvious that the test script 
is written in a bad way where a different instance is created every time a new number is tested.

So try to get your TLE'ed version of Python code, 
turn your dp array into a class variable, and try it again. 
It should be accepted. 
Note that you do not need any of the simple optimizations I made below to get the code accepted.
"""
import math
import sys
import collections

class Solution0:
    numSquaresDP = [0]
    def numSquares(self, n):
        if len(self.numSquaresDP) <= n:
            perfectSqr = [v**2 for v in range(1, int(math.sqrt(n)) + 1)]
            for i in range(len(self.numSquaresDP), n + 1):
                self.numSquaresDP.append( min(1 + self.numSquaresDP[i - sqr] for sqr in perfectSqr if sqr <= i))
        return self.numSquaresDP[n]


class Solution1:
    """
    # making the dp array an instance variable would cause TLE
    def __init__(self):
        self.dp = [0]
    """

    dp = [0]  # so now dp is a class variable

    def numSquares(self, n):

        for i in range(len(self.dp), n + 1):
            result = sys.maxsize
            k = int(math.sqrt(i))
            if k * k == i:
                self.dp.append(1)
                continue
            for j in range(1, int(math.sqrt(i)) + 1):
                result = min(result, self.dp[i - j * j] + 1)
                if result is 2:
                    break
            self.dp.append(result)
        return self.dp[n]


class SolutionSlow:
    def numSquares(self, n):

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(0, n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1)
                j += 1

        return dp[n]


"""
解题思路：
解法I：数论（Number Theory）

时间复杂度：O(sqrt n)

四平方和定理(Lagrange's Four-Square Theorem)：所有自然数至多只要用四个数的平方和就可以表示。
"""

"""
int numSquares(int n) {
    while (n % 4 == 0)
        n /= 4;
    if (n % 8 == 7)
        return 4;
    for (int a=0; a*a<=n; ++a) {
        int b = sqrt(n - a*a);
        if (a*a + b*b == n)
            return !!a + !!b;
    }
    return 3;
}
"""

"""
解法II：动态规划（Dynamic Programming）

时间复杂度：O(n * sqrt n)

初始化将dp数组置为无穷大；令dp[y * y] = 1，其中：y * y <= n

状态转移方程：

dp[x + y * y] = min(dp[x + y * y], dp[x] + 1)
其中：dp [i] 表示凑成i所需的平方和数字的最小个数，并且 x + y * y <= n
"""


class SolutionTLE:
    def numSquares(self, n):

        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1



class Solution3:
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


"""
解题思路：

1、使用动态规划，维护一个长度为n+1的数组，第i位存储和为i的最少整数个数。则f(i)只与i之前的数组有关。

2、变态解法（四平方和定理），任何一个正整数都可以由4个整数的平方和组成。即对所有n, 都有n=a*a+b*b+c*c+d*d。
"""


class Solution4:
    def numSquares(self, n):

        if n == 0:
            return 0
        output = [0x7fffffff] * (n + 1)
        output[0] = 0
        output[1] = 1
        for i in range(2, n + 1):
            j = 1
            while (j * j <= i):
                output[i] = min(output[i], output[i - j * j] + 1)
                j = j + 1

        return output[n]


#The below are the BFS solutions
class SolutionBFS1:
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            toCheck = temp



class SolutionBFS2:
    def numSquares(self, n):

        s = [i * i for i in range(1, int(math.sqrt(n)) + 1)]  # Square numbers <= n
        l = 0  # BFS level
        currentLevel = [0]  # List of numbers in BFS level l

        while True:
            nextLevel = []
            for a in currentLevel:
                for b in s:
                    if a + b == n: return l + 1  # Found n
                    if a + b < n:  nextLevel.append(a + b)
            currentLevel = list(set(nextLevel))  # Remove duplicates
            l += 1


class SolutionBFS3:
    def numSquares(self, n):
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            i, step = queue.popleft()
            step += 1
            for j in range(1, n + 1):
                k = i + j * j
                if k > n:
                    break
                if k == n:
                    return step
                if k not in visited:
                    visited.add(k)
                    queue.append((k, step))


class Solution33:
    def numSquares(self, n):
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue:
            val, dis = queue.popleft()
            # if val == n:
            #     return dis
            for i in range(1, n + 1):
                j = val + i * i
                if j > n:
                    break
                if j == n:
                    return dis + 1
                if j not in visited:
                    visited.add(j)
                    queue.append((j, dis + 1))

                    