import functools


class Solution:
    def validPalindrome(self, s):

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left += 1
            right -= 1
        return True


class SolutionMemo:
    def validPalindrome(self, s: str) -> bool:

        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0

            if s[i] == s[j]:
                return dfs(i + 1, j - 1)
            else:
                return min(dfs(i + 1, j), dfs(i, j - 1)) + 1

        return dfs(0, len(s) - 1) <= 1


