import functools

class Solution:
    def maxSatisfaction(self, satisfaction) -> int:
        @functools.lru_cache(None)
        def dfs(i, n):
            if i >= len(satisfaction):
                return 0

            # with or without
            w = dfs(i + 1, n + 1) + n * satisfaction[i]
            wo = dfs(i + 1, n)

            return max(w, wo)

        satisfaction = sorted(satisfaction)
        return dfs(0, 1)


"""
If we cook some dishes,
they must be the most satisfied among all choices.

Another important observation is that,
we will cook the dish with small satisfication,
and leave the most satisfied dish in the end.

Explanation
We choose dishes from most satisfied.
Everytime we add a new dish to the menu list,
all dishes on the menu list will be cooked one time unit later,
so the result += total satisfaction on the list.
We'll keep doing this as long as A[i] + total > 0.


Complexity
Time O(NlogN)
Space O(1)
"""


class SolutionLee:
    def maxSatisfaction(self, satisfaction):
        res = total = 0
        satisfaction.sort()
        while satisfaction and satisfaction[-1] + total > 0:
            total += satisfaction.pop()
            res += total
        return res