
"""
动态规划（Dynamic Programming）

首先把连续相同颜色的盒子进行合并，得到数组color以及数组length，分别表示合并后盒子的颜色和长度

dp[l][r][k]表示第l到第r个合并后的盒子，连同其后颜色为color[r]的长度k一并消去所能得到的最大得分

https://translate.google.com/translate?hl=en&sl=zh-CN&u=http://www.cnblogs.com/grandyang/p/6850657.html&prev=search


Note: The number of boxes n would not exceed 100.

When I first started reading this question, I felt like the Zuma Game before,
so I wrote a brute force method, and the result was TLE.
In desperation, I had to search the Internet for the solution of the gods,
and I read the post written by fun4LeetCode.
The previous Reverse Pairs was the reference to the fun4LeetCode Great God's post.
It was so amazing that this time it was so wonderful, please accept it. My knees.
Then the following solution is mostly explained with reference to the post of
fun4LeetCode .
In the previous post, Reverse Pairs , the Great God summarized two modes of reproduction.
We also tried to see if it could be applied. The ability to abstract modeling
is very important for such a problem that seems to have no idea.
For the specific scenes in the topic,
we can ignore the specific representation of things,
which can help us to approach the essence of the problem.
The essence of this problem is an array.
We eliminate one or more numbers each time and get corresponding The score,
let us ask for the highest score. The previous Zuma Game also gave an array,
et us add a number to a certain position, so that at least 3 of the same number
can be eliminated. The two are not very similar,
but the solution is quite different.
The reason why the brute force crack is no problem
is because the length of the array and the number of given numbers are limited,
and they are relatively small numbers, so even if you traverse all the cases,
there will not be much calculation. And this question is not the same,
since it can not be brute force, then for the problem of playing arrays
and sub-arrays, the old drivers who brush the questions will give priority to using DP
to do it. Since you want to play a subarray,
you must limit the range of the subarray,
then at least it should be a two-dimensional dp array,
where dp[i][j] represents the highest score that can be obtained in the subarray [i, j] range.
Then, finally we return dp[0][n-1] is the result of the request.

So for dp[i][j] we think that if we remove the number boxes[i],
then the total score should be 1 + dp[i+1][j],
but by analyzing the examples in the title,
we can get The trick of high integration is that after removing one or a few numbers,
if the same number that is not continuous is changed, the continuous number is dropped,
because the more numbers are removed at the same time, the higher the score is. .
So if there is a position m in the middle of [i, j],
making boxes[i] and boxes[m] equal, then we should not just remove the number of boxes[i],
but should also consider removing them directly [ The number on the interval i+1, m-1]
makes boxes[i] and boxes[m] directly adjacent,
then the score we get is dp[i+1][m-1], then what are we left? ,
boxes[i] and boxes[m, j] interval numbers,
at this point we can't process sub-arrays [m, j],
because some of our information is not included in our dp array,
such topics are summarized as not themselves The sub-problems included,
the solution depends on information other than sub-problems .
Such problems usually do not have a well-defined recurring relationship,
so it is not easy to recursively solve.
In order to solve such problems, we need to modify the definition of the problem
so that it contains some external information,
which becomes a self-contained sub-problem .

So for this question, the boxes[m, j]
interval cannot be processed because it lacks key information.
We don't know the number k of the same number on the left side of boxes[m].
Only know this information, then the position of m It makes sense,
so our dp array should be a three-dimensional array dp[i][j][k],
which represents the maximum integral that can be obtained in the interval [i, j].
When there are k numbers on the left of boxes[i] They are equal,
then our goal is to ask dp[0][n-1][0],
and we can also introduce dp[i][i][k] = (1+k) * (1+k) This equation.
Then we will derive the recurrence relationship. For dp[i][j][k],
if we remove boxes[i], then we get (1+k)*(1+k) + dp[i+1] [j][0].
For the case mentioned above, when a position m, with boxes[i] == boxes[m],
we should also consider removing [i+1,m-1] first, we get the points Dp[i+1][m-1][0],
and then process the remaining part to get the integral dp[m][j][k+1],
where k is added 1 point because the middle is removed After the part,
the boxes[i] that are not adjacent to boxes[m] are now adjacent,
and because the two values ​​are the same, k should be incremented by 1,
because the definition of k is the number of numbers on the left.
Speaking of this, then the most difficult recursive formula of the DP method is also obtained,
then the code is not difficult to write.

"""

class Solution:
    def removeBoxes(self, A):
        N = len(A)
        memo = [[[0] * N for _ in range(N)] for _ in range(N)]

        def dp(i, j, k):
            if i > j: return 0
            if not memo[i][j][k]:
                m = i
                while m + 1 <= j and A[m + 1] == A[i]:
                    m += 1
                i, k = m, k + m - i
                ans = dp(i + 1, j, 0) + (k + 1) ** 2
                for m in range(i + 1, j + 1):
                    if A[i] == A[m]:
                        ans = max(ans, dp(i + 1, m - 1, 0) + dp(m, j, k + 1))
                memo[i][j][k] = ans
            return memo[i][j][k]

        return dp(0, N - 1, 0)








