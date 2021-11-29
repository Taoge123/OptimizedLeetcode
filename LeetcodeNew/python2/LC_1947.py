
import functools

class Solution:
    def maxCompatibilitySum(self, students, mentors):
        def score(s, m):
            return sum(i == j for i, j in zip(s, m))

        n = len(students)
        @functools.lru_cache(None)
        def dfs(i, mask):
            if i >= n:
                return 0

            res = float('-inf')
            for j in range(n):
                if mask & ( 1< <j) == 0:
                    res = max(res, dfs(i+1, mask | (1<<j)) + score(students[i], mentors[j]))

            return res

        return dfs(0, 0)



