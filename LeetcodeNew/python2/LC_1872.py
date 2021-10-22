
"""
https://leetcode.com/problems/stone-game-viii/discuss/1224872/Top-Down-and-Bottom-Up
https://leetcode.com/problems/stone-game-viii/discuss/1228595/python-dp-O(n)
https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1872.Stone-Game-VIII
https://leetcode-cn.com/problems/stone-game-viii/solution/python-dong-tai-gui-hua-by-qubenhao-j287/

dp[i] : with i stones left, the maximum score difference for the starter

[x x x x x x o] -> dp[1] = 0
[x x x x x o] o -> dp[2] = presum[n] - dp[1]
[x x x x o] o o -> dp[3] = max(1, 2)
    1. pick 3 balls : presum[n] - dp[1]
    2. pick 2 balls : presum[n-1] - dp[2]
[x x x o] o o o -> dp[4] = max(1, 2, 3) = max(dp[3], presum[n-2] - dp[3])
    1. pick 4 balls : presum[n] - dp[1]
    2. pick 3 balls : presum[n-1] - dp[2]
    3. pick 2 balls : presum[n-2] - dp[3]


dp[i] = max(dp[i-1], presum[n-i+2] - dp[i-1])

"""

import functools


class Solution:
    def stoneGameVIII(self, stones) -> int:
        # 移除并放回，前缀和不变
        # 每次拿的石子必然包括前面的前缀和
        @functools.lru_cache(None)
        def dfs(i):
            if i >= n - 1:
                return presum[n]
            # 不选当前坐标，选后面的会是dfs(i+1),选当前坐标会得到presum[i+1] - dfs(i+1)。取两者最大值
            pick = presum[i + 1] - dfs(i + 1)
            no_pick = dfs(i + 1)

            return max(pick, no_pick)

        n = len(stones)
        presum = [0]
        for num in stones:
            presum.append(presum[-1] + num)
        dfs.cache_clear()
        return dfs(1)




