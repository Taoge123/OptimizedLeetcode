"""
there are two cases that source node cannot reach target node
case 1 is the blocked points and boundary points form a closed interval and one node(source or target) in,another out.
case 2 is only the blocked points form a closed interval and one node(source or target) in,another out.

the key point is the length of blocked is smaller than 200, so the closed area will not too large
we can just use bfs to search from the source, and set a maximum step.
after moving maximum step, if we can still move, then it must can reach the target point

here the maximum step should be the length of blocked, seen in case 3
of course, we should handled the different situation with the starting node
"""


import collections

"""
oxo
xoo


oooxooooo
ooxoooooo
oxooooooo
xoooooooo
ooooooooo

200 -> 2500

19900

1. expand by layer
2. 19900

"""


class SolutionRika:
    def isEscapePossible(self, blocked, source, target):

        # 两种cases
        # 1）其中一个点被blocked住，那么被包围的最大面积为 （两条边的三角形） size*size/2
        # 2) 如果其中一个点没被包围住，则检查另一个点有没被包围住
        # 如果都没被包围 --> 肯定能找到 两个个点

        if not blocked:
            return True

        # maximum area that can be surrounded by 200 blockers (when they form a triangle with grid's corner)
        n = len(blocked) * len(blocked) // 2

        # build a hashset to store all blocks
        blocks = set()
        for (x, y) in blocked:
            blocks.add((x, y))

        return self.dfs(source[0], source[1], blocks, target, set(), n) & self.dfs(target[0], target[1], blocks, source,
                                                                                   set(), n)

    def dfs(self, i, j, blocks, target, visited, n):
        if (i == target[0] and j == target[1]) or len(visited) >= n:  # 有可能跑到一半就返回 True （没跑到终点）
            return True

        visited.add((i, j))

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            x = i + dx
            y = j + dy
            if 0 <= x < 10 ** 6 and 0 <= y < 10 ** 6 and (x, y) not in blocks and (x, y) not in visited:
                if self.dfs(x, y, blocks, target, visited, n):
                    return True

        return False



class Solution:
    def isEscapePossible(self, blocked, source, target):

        if not blocked:
            return True

        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        blocked = set(map(tuple, blocked))
        return self.bfs(blocked, source, target) and self.bfs(blocked, target, source)

    def bfs(self, blocked, source, target):
        m = n = 10 ** 6
        queue = collections.deque()
        queue.append(source)
        visited = set()
        visited.add(tuple(source))
        step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if [i, j] == target:
                    return True

                for dx, dy in self.directions:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited or (x, y) in blocked:
                        continue
                    queue.append((x, y))
                    visited.add((x, y))

            step += 1
            if step == len(blocked):
                return True
            if len(visited) >= 20000:
                return True

            if len(queue) == 0:
                break

        return False






class SolutionLee:
    def isEscapePossible(self, blocked, source, target) -> bool:
        self.directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        blocked = [tuple(item) for item in blocked]
        return self.bfs(blocked, source, target) and self.bfs(blocked, target, source)

    def bfs(self, blocked, source, target):
        queue = [source]
        visited = {tuple(source)}
        for i, j in queue:
            for node in self.directions:
                print(i, j)
                x = i + node[0]
                y = j + node[1]
                if x >= 0 and y >= 0 and x < 10 ** 6 and y < 10 ** 6 and (x, y) not in visited and (x, y) not in blocked:
                    if [x, y] == target:
                        return True
                    queue.append([x, y])
                    visited.add((x, y))

            if len(queue) >= 20000:
                return True
        return False



blocked = []
source = [0,0]
target = [999999,999999]

a = SolutionLee()
print(a.isEscapePossible(blocked, source, target))



