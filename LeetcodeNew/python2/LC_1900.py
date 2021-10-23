"""
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1900.The-Earliest-and-Latest-Rounds-Where-Players-Compete
https://leetcode-cn.com/problems/the-earliest-and-latest-rounds-where-players-compete/solution/greedy-ologn-solution-by-wisdompeak-r28c/


"""

import functools
import itertools



class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @functools.lru_cache(None)
        def dfs(left, right, m):
            if left > right:
                return dfs(right, left, m)
            # 两个人到达同一位置(即他俩发生了对抗)
            if left == right:
                return [1, 1]

            mini, maxi = float('inf'), 0
            # l的下一个可能性为1(l前面的全部为负)到l(l前面的全部为胜)
            for i in range(1, left + 1):
                # r的下一个可能性为l-i+1 (r到l之间的全部为负)到r-i (r到l之间的全部为胜)
                for j in range(left - i + 1, right - i + 1):
                    if not (m + 1) // 2 >= i + j >= left + right - m // 2:
                        continue
                    early, late = dfs(i, j, (m + 1) // 2)
                    mini = min(mini, early + 1)
                    maxi = max(maxi, late + 1)
            return mini, maxi

        return list(dfs(firstPlayer, n - secondPlayer + 1, n))


"""
https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/discuss/1268452/Python-2-Solution%3A-dfs-and-smart-dp-explained
https://www.youtube.com/watch?v=Fv42C4pMYQA
By add bitmask
https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/discuss/1270571/bit-mask-%2B-simulation-%2B-memorization
"""

class SolutionCheng:
    def earliestAndLatest(self, n: int, f: int, s: int) -> List[int]:
        @functools.lru_cache(None)
        def dfs(players):
            n = len(players)
            pairs = []

            for i in range(n // 2):
                p1 = players[i]
                p2 = players[-i - 1]

                if p1 == f and p2 == s:
                    return [1, 1]

                if p1 not in (f, s) and p2 not in (f, s):
                    pairs.append((p1, p2))

            remains = (f, s) if n % 2 == 0 else tuple(set([f, s, players[n // 2]]))

            mini = float('inf')
            maxi = float('-inf')

            for nxt in itertools.product(*pairs):
                nxt += remains
                res = dfs(tuple(sorted(nxt)))
                mini = min(mini, res[0] + 1)
                maxi = max(maxi, res[1] + 1)
            return mini, maxi

        return dfs(tuple(range(1, n + 1)))


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, prev):
            if i >= n:
                if prev == 2:
                    return 1
                else:
                    return 0

            res = 0
            if (nums[i] == prev + 1) or (nums[i] == prev):
                res += dfs(i + 1, nums[i])

            res += dfs(i + 1, prev)

        return dfs(0, -1)



