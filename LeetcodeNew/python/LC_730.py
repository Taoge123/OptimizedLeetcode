"""
https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109510/Python-DP%2BDFS-O(n2)-with-Explanations
https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/272297/DP-C%2B%2B-Clear-solution-explained

https://www.youtube.com/watch?v=UjiFFYU3EKM
really hard

First of all, I compute when 'a' appears first (index i) and last (index j) in the segment I am considering. Then it breaks down into two cases:

If i == j. There is only one 'a' in the segment. So the answer is 1.
If i != j. The possible palindromes are 'a', 'aa', and 'a*a' where '*' stands for any palindromes contained in S[i+1:j]. The answer would be DFS(i+1,j) + 2. Since I want to avoid repetitive computation, I write cache(i+1,j) + 2 instead.
The worst case time complexity is O(n^2). The best case time complexity is O(n).
"""

import functools

"""

c - 1
cc - 2

c ********* c

********* - n 
c cc - 2
c ********* c - n
2 * n + 2


b cc b -> 6
cc - 2
bb - 2
b cc b - 2

bccb - 6
a bccb a
aa - 2
a bccb a - 6

"""


class Solution00:
    def countPalindromicSubsequences(self, s: str) -> int:

        mod = 10 ** 9 + 7
        memo = {}
        return self.dfs(s, 0, len(s) - 1, memo) % mod

    def dfs(self, s, i, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > j:
            return 0
        if i == j:
            return 1

        res = 0
        for ch in set(s[i:j + 1]):
            left = s.find(ch, i, j + 1)
            right = s.rfind(ch, i, j + 1)
            if left == right:
                res += 1
            else:
                res += self.dfs(s, left + 1, right - 1, memo) + 2
        memo[(i, j)] = res
        return res


class Solution0:
    def countPalindromicSubsequences(self, S: str) -> int:
        mod = 1000000007

        @functools.lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            # if i == j:
            #     return 1
            res = 0
            for ch in set(S[i:j + 1]):
                left = S.find(ch, i, j + 1)
                right = S.rfind(ch, i, j + 1)
                if left == right:
                    res += 1
                else:
                    res += dfs(left + 1, right - 1) + 2

            return res % mod

        return dfs(0, len(S) - 1)



class SolutionTD1:
    def countPalindromicSubsequences(self, S: str) -> int:
        mod = 1000000007

        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            res = 0
            for ch in set(S[i:j]):
                left = S.find(ch, i, j)
                right = S.rfind(ch, i, j)
                if left == right:
                    res += 1
                else:
                    res += dfs(left + 1, right) + 2

            return res % mod

        return dfs(0, len(S))



class SolutionTony:
    def countPalindromicSubsequences(self, S):
        memo = {}
        return self.dfs(S, memo) % 1000000007

    def dfs(self, s, memo):
        if s in memo:
            return memo[s]
        res = 0
        for ch in set(s):
            i = s.find(ch)
            j = s.rfind(ch)
            if i == j:
                res += 1
            else:
                res += self.dfs(s[i + 1:j], memo) + 2
        memo[s] = res
        return res


class SolutionTD:
    def countPalindromicSubsequences(self, S):
        @functools.lru_cache(None)
        def dfs(s):
            res = 0
            for ch in set(s):
                left = s.find(ch)
                right = s.rfind(ch)
                if left == right:
                    res += 1
                else:
                    res += dfs(s[left + 1:right]) + 2
            return res

        return dfs(S) % 1000000007



class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        mod = 10 ** 9 + 7

        def count(S, i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if self.table[i][j]:
                return self.table[i][j]

            if S[i] == S[j]:
                res = count(S, i + 1, j - 1) * 2
                left = i + 1
                right = j - 1
                while left <= right and S[left] != S[i]:
                    left += 1
                while left <= right and S[right] != S[i]:
                    right -= 1
                if left > right:
                    res += 2
                elif left == right:
                    res += 1
                else:
                    res -= count(S, left + 1, right - 1)
            else:
                res = count(S, i + 1, j) + count(S, i, j - 1) - + count(S, i + 1, j - 1)

            self.table[i][j] = res % mod
            return self.table[i][j]

        n = len(S)
        self.table = [[None for i in range(n)] for j in range(n)]
        return count(S, 0, n - 1)


s = "abccba"
a = Solution00()
print(a.countPalindromicSubsequences(s))


