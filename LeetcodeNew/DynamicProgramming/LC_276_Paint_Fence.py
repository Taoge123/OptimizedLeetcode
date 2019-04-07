
"""
https://leetcode.com/problems/paint-fence/discuss/71183/An-easy-to-understand-explanation-of-Paint-Fence

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3
 -----      -----  -----  -----
   1         c1     c1     c2
   2         c1     c2     c1
   3         c1     c2     c2
   4         c2     c1     c1
   5         c2     c1     c2
   6         c2     c2     c1
"""
"""
If n == 1, there would be k-ways to paint.

if n == 2, there would be two situations:

   2.1 You paint same color with the previous post: k*1 ways to paint, named it as same
   2.2 You paint differently with the previous post: k*(k-1) ways to paint this way, named it as dif

So, you can think, if n >= 3, you can always maintain these two situations,
You either paint the same color with the previous one, or differently.

Since there is a rule: "no more than two adjacent fence posts have the same color."

We can further analyze:

   - from 2.1, since previous two are in the same color, next one you could only paint differently, 
     and it would form one part of "paint differently" case in the n == 3 level, 
     and the number of ways to paint this way would equal to same*(k-1).
   - from 2.2, since previous two are not the same, you can either paint the same color this time (dif*1) ways to do so, 
     or stick to paint differently (dif*(k-1)) times.

Here you can conclude, when seeing back from the next level, ways to paint the same, 
or variable same would equal to dif*1 = dif, and ways to paint differently, variable dif,
would equal to same*(k-1)+dif*(k-1) = (same + dif)*(k-1)

"""
class Solution1:
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        same, dif = k, k * (k - 1)
        for i in range(3, n + 1):
            same, dif = dif, (same + dif) * (k - 1)
        return same + dif


class Solution2:
    def numWays(self, n, k):
        if n == 0 or k == 0:
            return 0

        num_same = 0  # the number of ways that the last element has the same color as the second last one
        num_diff = k  # the number of ways that the last element has differnt color from the second last one

        for i in range(1, n):
            total = num_diff + num_same
            num_same = num_diff
            num_diff = total * (k - 1)

        return num_same + num_diff

"""
Following this logic we would also have:

dp[i][1] = dp[i-1][1]*(k-1) + dp[i-1][0]*(k-1)
"""


class Solution3:
    def numWays(self, n, k):

        if n <= 0: return 0
        if n == 1: return k
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [0, k]  # tricky part. Imagine that there is a virtual extra fence on the left.

        # dp[i][0] means at i fence, it's same color with the i-1 fence. At this case how many possibilities.
        for i in range(1, n):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = dp[i - 1][1] * (k - 1) + dp[i - 1][0] * (k - 1)
        return sum(dp[-1])


