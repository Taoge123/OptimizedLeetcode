
"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping
1 unit to the 2nd stone, then 2 units to the 3rd stone, then
2 units to the 4th stone, then 3 units to the 6th stone,
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as
the gap between the 5th and 6th stone is too large.
"""

import functools

class SolutionTD:
    def canCross(self, stones) -> bool:
        target = stones[-1]
        stones = set(stones)

        @functools.lru_cache(None)
        def dfs(i, speed):
            if i == target:
                return True
            for jump in [speed + 1, speed, speed - 1]:
                if jump != 0 and i + jump in stones:
                    if dfs(i + jump, jump):
                        return True
            return False

        return dfs(0, 0)




class Solution:
    def canCross(self, stones):

        table = {}
        for stone in stones:
            table[stone] = set()
        table.get(0).add(0)

        for i in range(len(stones)):
            for k in table.get(stones[i]):
                for step in range(k - 1, k + 2):
                    if step > 0 and step + stones[i] in table:
                        table[step + stones[i]].add(step)

        return len(table[stones[-1]]) > 0



class SolutionBFS:
    def canCross(self, stones) -> bool:
        if stones[1] != 1: return False
        if len(stones) < 3:
            return True
        target = stones[-1]
        mem = set(stones)
        q = [(1, 1)]
        visit = {(1, 1)}
        p = 0
        while p < len(q):
            i, j = q[p]
            for dis in (j - 1, j, j + 1):
                if dis > 0 and i + dis in mem and (i + dis, dis) not in visit:
                    if i + dis == target:
                        return True
                    visit.add((i + dis, dis))
                    q.append((i + dis, dis))
            p += 1
        return False


class Solution2:
    def canCross(self, stones) -> bool:
        self.stoneSet = set(stones)
        self.cantReach = set()
        return self.dfs(stones, 0, 0)

    def dfs(self, stones, pos, step):
        if pos == stones[-1]:
            return True
        if pos not in self.stoneSet:
            return False
        if (pos, step) in self.cantReach:
            return False

        if step > 1 and self.dfs(stones, pos + step - 1, step - 1):
            return True
        if step > 0 and self.dfs(stones, pos + step, step):
            return True
        if self.dfs(stones, pos + step + 1, step + 1):
            return True

        self.cantReach.add((pos, step))
        return False



stones = [0,1,3,5,6,8,12,17]
a = Solution2()
print(a.canCross(stones))








