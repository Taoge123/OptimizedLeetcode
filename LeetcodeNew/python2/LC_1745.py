
import functools


class Solution:
    def checkPartitioning(self, s: str) -> bool:

        memo = {}
        return self.dfs(s, 0, 3, memo)

    def dfs(self, s, i, k, memo):
        if (i, k) in memo:
            return memo[(i, k)]

        n = len(s)
        if i >= n and k == 0:
            return True

        if i >= n or k == 0:
            return False

        for j in range(i + 1, n + 1):
            if s[i:j] == s[i:j][::-1]:
                if self.dfs(s, j, k - 1, memo):
                    memo[(i, k)] = True
                    return True

        memo[(i, k)] = False
        return False


class SolutionTony2:
    def checkPartitioning(self, s: str) -> bool:
        memo = {}
        return self.dfs(s, 0, 3, memo)

    def dfs(self, s, i, k, memo):

        @functools.lru_cache(None)
        def isPal(l, r):  # l, r inclusive
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return isPal(l + 1, r - 1)

        if (i, k) in memo:
            return memo[(i, k)]

        n = len(s)
        if i >= n and k == 0:
            return True
        if i >= n or k == 0:
            return False

        for j in range(i, n):
            # if s[i:j] == s[i:j][::-1]:
            if isPal(i, j):
                if self.dfs(s, j + 1, k - 1, memo):
                    memo[(i, k)] = True
                    return True
        memo[(i, k)] = False
        return False



class SolutionTonyMLE:
    def checkPartitioning(self, s: str) -> bool:
        memo = {}
        return self.dfs(s, 0, 3, memo)

    def dfs(self, s, i, k, memo):

        @functools.lru_cache(None)
        def isPal(l, r):  # l, r inclusive
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return isPal(l + 1, r - 1)

        if (i, k) in memo:
            return memo[(i, k)]

        n = len(s)
        if i >= n and k == 0:
            return True
        if i >= n or k == 0:
            return False

        for j in range(i + 1, n + 1):
            # if s[i:j] == s[i:j][::-1]:
            if isPal(i, j - 1):
                if self.dfs(s, j, k - 1, memo):
                    memo[(i, k)] = True
                    return True
        memo[(i, k)] = False
        return False


class SolutionAC:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        @functools.lru_cache(None)
        def isPal(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return pal(i + 1, j - 1)

        for i in range(n - 2):
            if isPal(0, i):
                for j in range(i + 1, n - 1):
                    if isPal(i + 1, j) and isPal(j + 1, n - 1):
                        return True
        return False
