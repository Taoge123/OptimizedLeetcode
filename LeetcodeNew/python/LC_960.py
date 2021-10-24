

"""
dp[i] := max length of increasing sub-sequence (of all strings) ends with i-th letter.
dp[i] = max(dp[j] + 1) if all A[*][j] <= A[*][i], j < i

解题思路：本题可以采用动态规划的方法。记dp[i][0] = v表示不删除第i个元素时，
使得0~i子区间有序需要删除掉v个字符，dp[i][1] = v表示删除第i个元素时，使得0~i子区间有序需要删除掉v个字符。
先看第二种情况，因为对第i个元素删除操作，所以其值完全和dp[i-1]有关，
有dp[i][1] = min(dp[i-1][0],dp[i-1][1]) + 1，取第i个元素删除或者不删除时候的较小值；
而如果第i个元素保留，那么我们只需要找出离i最近的保留的元素j，
使得Input 中每一个元素 item 都需要满足 item[i] > item[j]，这样的j可能不存在或者有多个，
找出满足 dp[i][0] = min(dp[i][0],dp[j][0] + (i-j-1)) 最小的即可，如果没有这样的j存在，
令dp[i][0] = i。最后的结果为 dp[-1][0]和dp[-1][1]中的较小值。

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

"""

import functools



class SolutionTony1:
    def minDeletionSize(self, A):
        m, n = len(A), len(A[0])

        @functools.lru_cache(None)
        def dfs(i):
            if i >= n:
                return 1

            res = 0
            for j in range(i+1, n):
                check = True
                for k in range(m):
                    if A[k][j] < A[k][i]:
                        check = False
                if check:
                    res = max(res, dfs(j))
            return res + 1

        return n - max(dfs(i) for i in range(n))






class SolutionTony2:
    def minDeletionSize(self, A):
        m, n = len(A), len(A[0])

        @functools.lru_cache(None)
        def dfs(i):
            if i >= n:
                return 1

            res = 0
            for j in range(i+1, n):
                if all(A[k][j] >= A[k][i] for k in range(m)):
                    res = max(res, dfs(j))
            return res + 1

        return n - max(dfs(i) for i in range(n))






class SolutionLee:
    def minDeletionSize(self, A):
        n = len(A[0])
        dp = [1] * n
        for j in range(1, n):
            for i in range(j):
                if all(a[i] <= a[j] for a in A):
                    dp[j] = max(dp[j], dp[i] + 1)
        return n - max(dp)


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

  class Solution1:
      def minDeletionSize(self, A) -> int:
          m, n = len(A), len(A[0])
          dp = [1] * n
          for i in range(1, n):
              for j in range(i):
                  for k in range(m + 1):
                      if k == m:
                          dp[i] = max(dp[i], dp[j] + 1)
                      elif A[k][j] > A[k][i]:
                          break

          return n - max(dp)





