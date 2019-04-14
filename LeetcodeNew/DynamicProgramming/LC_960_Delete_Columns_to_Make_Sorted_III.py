
"""
https://www.youtube.com/channel/UCUBt1TDQTl1atYsscVoUzoQ
Leetcode 944. Delete Columns to Make Sorted

We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["babca","bbazb"] and deletion indices {0, 1, 4}, then the final array after deletions is ["bc","az"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row) in lexicographic order.

For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]),
A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.

Return the minimum possible value of D.length.

Example 1:

Input: ["babca","bbazb"]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is A = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
Note that A[0] > A[1] - the array A isn't necessarily in lexicographic order.
Example 2:

Input: ["edcba"]
Output: 4
Explanation: If we delete less than 4 columns, the only row won't be lexicographically sorted.
Example 3:

Input: ["ghi","def","abc"]
Output: 0
Explanation: All rows are already lexicographically sorted.

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100

"""
"""
Intuition

Take n cols as n elements, so we have an array of n elements.
=> The final array has every row in lexicographic order.
=> The elements in final state is in increasing order.
=> The final elements is a sub sequence of initial array.
=> Transform the problem to find the maximum increasing sub sequence.


Explanation
Now let's talking about how to find maximum increasing subsequence.
Here we apply a O(N^2) dp solution.

dp[i] means the longest subsequence ends with i-th element.
For all j < i, if A[][j] < A[][i], then dp[j] = max(dp[j], dp[i] + 1)


Time Complexity:
O(N^2) to find increasing subsequence
O(M) for comparing elements.
So Overall O(MN^2).
"""

class SolutionLee:
    def minDeletionSize(self, A):
        m, n = len(A), len(A[0])
        dp = [1] * n
        for j in range(1, n):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(m)):
                    dp[j] = max(dp[j], dp[i] + 1)
        return n - max(dp)


"""
for A = ["babca","bbazb"]
first we conver it to
b,b line 1
a,b line 2
b,a line 3
c,z line 4
a,b line 5

whether we should left line 1 or not is determined by which will get smaller D.length.
if we do not delete this line, then the next line's element should all be larger than this line, otherwise we must delete next line

we define function solve(A, index, start) means the D.length if we use start as the first element in A[index:].
index means the line which we are considering
start is a list, represent the last line we choose left.

so if any(A[index][i] < start[i]), we delete this line, and analyse solve(A, index+1, start)

otherwise, if all(A[index][i] >= start[i]), we choose the min D.length in case left A[index] and case delete A[index], e.g. min(solve(A,index+1,tuple(A[index])), 1+solve(A,index+1, start))

cause there are many double count, so I use tuple format to represent start
"""


class Solution2:
    def minDeletionSize(self, A):
        cache = {}

        def solve(A, index, start):
            if index >= len(A): return 0
            if (index, start) in cache: return cache[index, start]

            if any(A[index][j] < start[j] for j in range(len(A[index]))):
                cache[index, start] = 1 + solve(A, index + 1, start)
                return cache[index, start]

            cache[index, start] = min(solve(A, index + 1, tuple(A[index])), 1 + solve(A, index + 1, start))
            return cache[index, start]

        return solve(list(zip(*A)), 0, tuple(['a'] * len(A)))


# Python DP O(NM^2)
class Solution3:
    def minDeletionSize(self, A):

        width = len(A[0])
        common_non_decrease = [1] * width

        for c_i in range(width - 2, -1, -1):
            for c_j in range(c_i + 1, width):

                flag = True
                for row in A:
                    if row[c_i] > row[c_j]:
                        flag = False
                        break

                if flag:
                    common_non_decrease[c_i] = max(common_non_decrease[c_i], common_non_decrease[c_j] + 1)

        return width - max(common_non_decrease)


"""
dp[i] := max length of increasing sub-sequence (of all strings) ends with i-th letter.

dp[i] = max(dp[j] + 1) if all A[*][j] <= A[*][i], j < i

Time complexity: (n*L^2)
Space complexity: O(L)

"""
class SolutionHuahua:
    def minDeletionSize(self, A):
        n = len(A[0])
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                valid = True
                for a in A:
                    if a[j] > a[i]:
                        valid = False
                        break
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)

        return n - max(dp)

"""
Intuition and Algorithm

This is a tricky problem that is hard to build an intuition about.

First, lets try to find the number of columns to keep, 
instead of the number to delete. At the end, we can subtract to find the desired answer.

Now, let's say we must keep the first column C. The next column D we keep must have all rows lexicographically sorted 
(ie. C[i] <= D[i]), and we can say that we have deleted all columns between C and D.

Now, we can use dynamic programming to solve the problem in this manner. 
Let dp[k] be the number of columns that are kept in answering the question for input [row[k:] for row in A]. 
The above gives a simple recursion for dp[k].

Complexity Analysis

Time Complexity: O(N * W^2)O(N∗W 2), where NN is the length of A, and WW is the length of each word in A.

Space Complexity: O(W)O(W). 
"""
class Solution4:
    def minDeletionSize(self, A):
        W = len(A[0])
        dp = [1] * W
        for i in range(W-2, -1, -1):
            for j in range(i+1, W):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])

        return W - max(dp)


"""
有人说这道题很难（从提交情况来看，确实很难）。但我完全没有觉得它难，因为在做这个系列的第一题
（Leetcode 944. Delete Columns to Make Sorted）的时候，我就差点把题意当成了这一道，
所以我早就知道这道题怎么解了。

解法很简单。当成一个最长不降子序列问题就可以。两列满足不降的条件是，对应的每对字符都是不降的。所以复杂度是O(N*M^2)。

随便讲两句废话。按Leetcode的记录，我已经参加了21场比赛了，从8月14日到12月15日。
期间很多事情在逐渐发生变化。比如我的rating不再变了，对活跃在题解区的几个人有了更多了解，
lee215除了在题解区写题解之外还开始在简书上发中文题解和在youtube上发视频，
今天正好一共刷了233道题。我感觉，只要我在Leetcode上还有做起来费劲的题，刷Leetcode就不是没有价值的，
因为掌握不止要看“会”，还要看“熟练度”；但是刷Leetcode还是远远不够的。

据说Leetcode用户觉得最难的题目类型是动态规划。

今天去考了CSP，感觉自己还是菜。翻翻《算法竞赛入门经典训练指南》，感觉自己不会的topic比会的多多了。
等到寒假我打算尝试把USACO做完，并且开始打CF的div3之类的。
"""

"""
思路：DP，dp[i]表示以第i列结尾的情况下，前面那些字符需要删除的最小列数
（后面的一定会删掉，因为要以当前列结尾）
"""


class Solution5:
    def minDeletionSize(self, A):

        dp = [len(A) - 1] * len(A[0])
        dp[0] = 0
        for i in range(1, len(dp)):
            dp[i] = i
            for j in range(i):
                if all(A[k][i] >= A[k][j] for k in range(len(A))):
                    dp[i] = min(dp[i], dp[j] + i - j - 1)

        dp2 = [dp[i] + len(dp) - i - 1 for i in range(len(dp))]
        return min(dp2)



