
"""
https://leetcode-cn.com/problems/bulb-switcher-ii/solution/672-dfs-wei-yun-suan-gui-lu-by-desti-2rdp/
https://leetcode-cn.com/problems/bulb-switcher-ii/solution/bao-li-mo-ni-by-lizhenbang56/

"""

import functools

class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        res = set()
        state = int('1' * n)
        mask = {
            1: int(''.join(['1' for i in range(n)])),
            2: int(''.join(['1' if (i + 1) % 2 == 0 else '0' for i in range(n)])),
            3: int(''.join(['1' if (i + 1) % 2 == 1 else '0' for i in range(n)])),
            4: int(''.join(['1' if (i + 1) % 3 == 1 else '0' for i in range(n)])),
        }
        print(mask)

        @functools.lru_cache(None)
        def dfs(state, k):
            if len(res) >= 8:
                return

            if k == 0:
                res.add(state)
                return

            for i in range(1, 5):
                dfs(state ^ mask[i], k - 1)

        dfs(state, presses)
        return len(res)



class SolutionDFS:
    def flipLights(self, n: int, presses: int) -> int:
        res = set()
        state = int('1' * n)
        self.mask = {
            1: int(''.join(['1' for i in range(n)])),
            2: int(''.join(['1' if (i + 1) % 2 == 0 else '0' for i in range(n)])),
            3: int(''.join(['1' if (i + 1) % 2 == 1 else '0' for i in range(n)])),
            4: int(''.join(['1' if (i + 1) % 3 == 1 else '0' for i in range(n)])),
        }
        print(self.mask)

        memo = {}
        self.dfs(state, presses, res, memo)
        return len(res)

    def dfs(self, state, k, res, memo):
        if (state, k) in memo:
            return memo[(state, k)]

        if len(res) >= 8:
            return

        if k == 0:
            res.add(state)
            return

        for i in range(1, 5):
            self.dfs(state ^ self.mask[i], k - 1, res, memo)

        memo[(state, k)] = res