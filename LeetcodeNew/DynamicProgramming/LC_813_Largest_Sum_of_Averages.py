
"""
Similar to Word Break && Burst Bloon - All need to split the array


We partition a row of numbers A into at most K adjacent (non-empty) groups,
then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
"""
"""
Init:
dp[1][i] = avg(a[0] ~ a[i-1])

Transition:
dp[k][i] = max(dp[k-1][j] + avg(a[j+1], a[i]))

Answer:
dp[K][n]

"""
"""
解题方法
典型的dp求解的题目。不过dfs方式去做速度还挺快。看到A的大小是100，那么时间复杂度应该在O(n^3)。

我们定义一个函数LSA，这个函数的含义是，把A这个数组的前n个元素分成k个组得到的最大平均数和。
使用m_二维数组完成记忆化，使得搜索速度变快。用sum_保存前i项数组的和，使得可以快速求平均数。

所以递归的方式：

把A这个数组的前i个元素分成k个组得到的最大平均数和 = max(把A这个数组的前j个元素分成k-1个组得到的最大平均数和 + 数组A从j+1到i个元素的平均值）。

如果读不懂上面这句话，可以直观的理解成k个组的最大平均数和 是怎么组成的？
它是由前k-1个组与后面一个组放在一起组成，所以求怎么划分的情况下，前部分和后部分的求平均数的和最大。
"""
"""
Approach #1: Dynamic Programming [Accepted]
Intuition

The best score partitioning A[i:] into at most K parts depends on answers to paritioning A[j:] (j > i) into less parts. 
We can use dynamic programming as the states form a directed acyclic graph.

Algorithm

Let dp(i, k) be the best score partioning A[i:] into at most K parts.

If the first group we partition A[i:] into ends before j, then our candidate partition has score average(i, j) + dp(j, k-1)), where average(i, j) = (A[i] + A[i+1] + ... + A[j-1]) / (j - i) (floating point division). We take the highest score of these, keeping in mind we don't necessarily need to partition - dp(i, k) can also be just average(i, N).

In total, our recursion in the general case is dp(i, k) = max(average(i, N), max_{j > i}(average(i, j) + dp(j, k-1))).

We can calculate average a little bit faster by remembering prefix sums. If P[x+1] = A[0] + A[1] + ... + A[x], then average(i, j) = (P[j] - P[i]) / (j - i).

Our implementation showcases a "bottom-up" style of dp. Here at loop number k in our outer-most loop, dp[i] represents dp(i, k) from the discussion above, and we are calculating the next layer dp(i, k+1). The end of our second loop for i = 0..N-1 represents finishing the calculation of the correct value for dp(i, t), and the inner-most loop performs the calculation max_{j > i}(average(i, j) + dp(j, k)).

"""
import math

class Solution1:
    def largestSumOfAverages(self, A, K):
        P = [0]
        for x in A: P.append(P[-1] + x)
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        N = len(A)
        dp = [average(i, N) for i in range(N)]
        for k in range(K-1):
            for i in range(N):
                for j in range(i+1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]

"""
search return the result for n first numbers to k groups.
It's top-down solution and it keeps all process to memory.
So it's like a DP solution while DP is bottom-up.
I took suggestion from @MonnaGotIt and added a prunting: if (n < k) return 0;

Time complexity: O(KN^2)
"""
"""
It took me a while to understand the solution so hopefully this helps out.

General Idea is that:

You are building up a list of averages for each i,k index
Similar to the buying and selling of stock question, 
at each increment of k you are leverage off the previous k best average 
and trying to determine how the best average based on the addition of the new index. 
With the new index, there are different possibilities of how the average could be. 
You need to find the max of those and that will be equal to your solution for i,k
Here is an example:
i k
0 1 2 3
0 0 0 0 0
9 1 0 9
1 2 0 5
2 3 0 4

When k = 1, you know that it's just the total sum/number of integers. With the top-down approach, you will be calculating dp[3][2] first.

dp[3][2] = Max(dp[2][1] +2, dp[1,1] + (2+1)/2)

Notice how it's finding the max based on the previous calculation at k-1 = 1. For k = 2, the possible partition is

Best average sum for dp[2,1] + the rest of the number will belong to one partition so that is 2/1
Best average sum for dp[1,1] + the rest of the numbers will belong to one partition so that is (2+1)/2
So with that you know that the final answer is at dp[N][K].
"""

class SolutionLee:
    def largestSumOfAverages(self, A, K):
        memo = {}
        def search(n, k):
            if (n, k) in memo: return memo[n, k]
            if n < k: return 0
            if k == 1:
                memo[n, k] = sum(A[:n]) / float(n)
                return memo[n, k]
            cur, memo[n, k] = 0, 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                memo[n, k] = max(memo[n, k], search(i, k - 1) + cur / float(n - i))
            return memo[n, k]
        return search(len(A), K)



class SolutionFast:
    def largestSumOfAverages(self, a, k):
        def rec(st, k):
            if (st, k) in cache:
                return cache[(st, k)]
            if k == 1:
                cache[(st, k)] = sum(a[st:])/(len(a)-st)
                return cache[(st, k)]
            total = 0
            res = -math.inf
            for i in range(st, len(a)-k+1):
                total += a[i]
                res = max(res, (total/(i-st+1)) + rec(i+1, k-1))
            cache[(st, k)] = res
            return cache[(st, k)]
        cache = {}
        return rec(0, k)


"""
The idea is to work our way from left to the right, computing at every index i and every k <= K the max result 
if we want to split the subarray A[0 : i] into k segments. The solution can be easily sped up in multiple ways, 
including computing in advance sum(A[r:i]) efficiently, but this works well enough.
"""
"""
Sol1: straightforward recursive solution
if find the max avg of A[0:] = avg(A[0:i]) + rev(A[i:], K-1) loops from 1...len(A) - K + 1

Sol2: from the conception, we can get the idea of dp

dp[i, k] means the max avg of dividing the array A[i:] into at most k parts
return: dp(0, K)
init: dp(i:0...len(A) - 1, 1) = sum(A[i:])/len(A[i:])
equation: dp(i, k) = max(dp(j, k-1) + avg(A[i, j] loops j:i+1...N-k+2

"""
"""
动态规划（Dynamic Programming）

状态转移方程：

dp[x][y] = max(dp[x][y], dp[x - 1][z] + avg(z..y))    0 <= x < K,  x <= y < N, x <= z < y
上式中，dp[x][y]表示将数组的前y个元素至多分成x个子数组的最优解
"""
class Solution2:
    def largestSumOfAverages(self, A, K):

        N = len(A)
        S = [0] * (N + 1)
        for x, a in enumerate(A):
            S[x + 1] += S[x] + a

        dp = [1.0 * S[x] / x for x in range(1, N + 1)]
        for x in range(K - 1):
            dp0 = [0] * N
            for y in range(x, N):
                for z in range(x, y):
                    dp0[y] = max(dp0[y], dp[z] + 1.0 * (S[y + 1] - S[z + 1]) / (y - z))
            dp = dp0
        return dp[-1]


class Solution3:
    def largestSumOfAverages(self, A, K):

        n = len(A)
        m_ = [[0 for i in range(n + 1)] for j in range(K + 1)]
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + A[i - 1]
        return self.LSA(A, preSum, m_, n, K)

    # Largest sum of averages for first n elements in A partioned into K groups
    def LSA(self, A, preSum, matrix, n, k):
        if matrix[k][n] > 0:
            return matrix[k][n]
        if k == 1:
            return preSum[n] / n
        for i in range(k - 1, n):
            matrix[k][n] = max(matrix[k][n], self.LSA(A, preSum, matrix, i, k - 1) + (preSum[n] - preSum[i]) / (n - i))
        return matrix[k][n]





