
"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Accepted
112,287
Submissions
399,926
"""

class SolutionCaikehe:
    # O(m*n) space
    def isInterleave1(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        dp = [[True for _ in range(c + 1)] for _ in range(r + 1)]
        for i in range(1, r + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, c + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j]) or (dp[i][j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1][-1]

    # O(2*n) space
    def isInterleave2(self, s1, s2, s3):
        l1, l2, l3 = len(s1) + 1, len(s2) + 1, len(s3) + 1
        if l1 + l2 != l3 + 1:
            return False
        pre = [True for _ in range(l2)]
        for j in range(1, l2):
            pre[j] = pre[j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, l1):
            cur = [pre[0] and s1[i - 1] == s3[i - 1]] * l2
            for j in range(1, l2):
                cur[j] = (cur[j - 1] and s2[j - 1] == s3[i + j - 1]) or \
                         (pre[j] and s1[i - 1] == s3[i + j - 1])
            pre = cur[:]
        return pre[-1]

    # O(n) space
    def isInterleave3(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        dp = [True for _ in range(c + 1)]
        for j in range(1, c + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, r + 1):
            dp[0] = (dp[0] and s1[i - 1] == s3[i - 1])
            for j in range(1, c + 1):
                dp[j] = (dp[j] and s1[i - 1] == s3[i - 1 + j]) or (dp[j - 1] and s2[j - 1] == s3[i - 1 + j])
        return dp[-1]

    # DFS
    def isInterleave4(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            x, y = stack.pop()
            if x + y == l:
                return True
            if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                stack.append((x + 1, y));
                visited.add((x + 1, y))
            if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                stack.append((x, y + 1));
                visited.add((x, y + 1))
        return False

    # BFS
    def isInterleave(self, s1, s2, s3):
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False
        queue, visited = [(0, 0)], set((0, 0))
        while queue:
            x, y = queue.pop(0)
            if x + y == l:
                return True
            if x + 1 <= r and s1[x] == s3[x + y] and (x + 1, y) not in visited:
                queue.append((x + 1, y));
                visited.add((x + 1, y))
            if y + 1 <= c and s2[y] == s3[x + y] and (x, y + 1) not in visited:
                queue.append((x, y + 1));
                visited.add((x, y + 1))
        return False

"""
Pure recursion without loops. Useful for interviews when we need to code things fast without much bullcrap. 
Shortest in Python I've seen so far for this problem, but may be wrong.
"""


class Solution1:
    def isInterleave(self, s1, s2, s3, memo={}):
        if len(s1) + len(s2) != len(s3): return False
        if not s1 and not s2 and not s3: return True
        if (s1, s2, s3) in memo:         return memo[s1, s2, s3]
        memo[s1, s2, s3] = \
            (len(s1) > 0 and len(s3) > 0 and s1[0] == s3[0] and self.isInterleave(s1[1:], s2, s3[1:], memo)) or \
            (len(s2) > 0 and len(s3) > 0 and s2[0] == s3[0] and self.isInterleave(s1, s2[1:], s3[1:], memo))
        return memo[s1, s2, s3]


class Solution2:
    # def isInterleave(self, s1, s2, s3):
    def bottom_up(self, s1, s2, s3):
        # dp solution
        # dp[i][j] means using first i chars from s1 and first j chars from s2, can we interleave to something that is s3[:i+j]
        # two cases, the new char from s1 or s2:
        # dp[i][j] = (dp[i-1][j] && s1[i] == s3[i+j]) || (dp[i][j-1] && s2[j] == s3[i+j])
        m, n = len(s1), len(s2)
        if m + n != len(s3): return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # initialize, if both s1 and s2 are empty strings, their interleave is also an empty string which is part of s3
        dp[0][0] = True
        for i in range(1, m + 1):
            if dp[i - 1][0] and s1[i - 1] == s3[i - 1]: dp[i][0] = True
        for i in range(1, n + 1):
            if dp[0][i - 1] and s2[i - 1] == s3[i - 1]: dp[0][i] = True

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]):
                    dp[i][j] = True
        return dp[m][n]

    def top_down(self, s1, s2, s3):
        # recursive
        m, n, y = len(s1), len(s2), len(s3)
        cache = {}

        def helper(i, j):
            k = i + j
            key = (i, j)
            if key in cache: return cache[key]
            if i == m: return s2[j:] == s3[k:]
            if j == n: return s1[i:] == s3[k:]
            if k >= y: return False
            # next char either comes from s1 or s2
            ans = False
            if s3[k] == s1[i] and helper(i + 1, j):
                ans = True
            elif s3[k] == s2[j] and helper(i, j + 1):
                ans = True
            cache[key] = ans
            return ans

        return helper(0, 0)

    isInterleave = top_down





