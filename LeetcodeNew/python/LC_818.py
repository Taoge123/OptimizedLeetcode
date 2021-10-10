"""
https://leetcode.com/problems/race-car/discuss/422810/Python-DP-explained
https://leetcode.com/problems/race-car/discuss/123834/JavaC%2B%2BPython-DP-solution
https://leetcode.com/problems/race-car/discuss/1270292/Python-DFS-beats-83-both-runtime-and-memory-with-comments
"""
"""
dp(target) means the minimum steps to reach target starting at 0, with speed 1 heading toward target.
If we can reach target without turn back, then this is the best way.
But if we can't, then we can:

either go forward until pass the target and then go back
Or go forward until one step before target, then go back to somewhere >=0, then go forward again to the target.
Either case, we can only turn back one time. If we allow turning back and force multiple times, there will be too many cases to consider and cause TLE.
"""

import collections
import functools


class SolutionTony:
    @functools.lru_cache(None)
    def racecar(self, target: int) -> int:

        memo = {}
        return self.dfs(target, memo)

    def dfs(self, target, memo):
        if target in memo:
            return memo[target]

        stepsOver = target.bit_length()
        pos1 = (1 << stepsOver) - 1
        if pos1 == target:
            return stepsOver
        res = self.dfs(pos1 - target, memo) + stepsOver + 1

        stepsBehind = stepsOver - 1
        pos2 = (1 << stepsBehind) - 1
        for backSteps in range(stepsBehind):
            backDist = (1 << backSteps) - 1
            res = min(res, self.dfs(target - pos2 + backDist, memo) + backSteps + stepsBehind + 2)

        memo[target] = res
        return res




class Solution:
    def racecar(self, target: int) -> int:
        queue = collections.deque()
        queue.append([0, 1])
        visited = set()
        visited.add((0, 1))
        res = 0
        while queue:
            size = len(queue)
            for i in range(size):
                pos, speed = queue.popleft()
                if pos == target:
                    return res

                nxt1 = [pos + speed, speed << 1]
                state1 = tuple(nxt1)
                if nxt1[0] >= 0 and state1 not in visited:
                    queue.append(nxt1)
                    visited.add(state1)

                if speed > 0:
                    nxt2 = [pos, -1]
                else:
                    nxt2 = [pos, 1]

                state2 = tuple(nxt2)
                if nxt2[0] >= 0 and state2 not in visited:
                    queue.append(nxt2)
                    visited.add(state2)
            res += 1
        return -1


