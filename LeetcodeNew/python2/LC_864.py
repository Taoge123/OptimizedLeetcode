import collections

class Solution:
    def shortestPathAllKeys(self, grid):
        m, n = len(grid), len(grid[0])
        self.directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    s1, s2 = (i, j)
                elif grid[i][j] in "abcdef":
                    count += 1

        finalState = 0
        for i in range(count):
            finalState |= (1 << i)
        queue = collections.deque([(s1, s2, 0)])  # [(i, j, state, moves)]
        visited = set([(s1, s2, 0)])
        step = -1
        """
        deque([(0, 0, 0)])
        {(0, 0, 0)}
"""
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                i, j, state = queue.popleft()
                if state == finalState:
                    return step
                for dx, dy in self.directions:
                    x = i + dx
                    y = j + dy
                    newState = state
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    if grid[x][y] == "#":
                        continue
                    elif grid[x][y] in "ABCDEF":
                        # 遇到锁, 看看有没有钥匙
                        k = ord(grid[x][y]) - ord('A')
                        if state & (1 << k) == 0:
                            continue
                    elif grid[x][y] in "abcdef":
                        k = ord(grid[x][y]) - ord('a')
                        newState = state | (1 << k)
                    if (x, y, newState) in visited:
                        continue
                    queue.append((x, y, newState))
                    visited.add((x, y, newState))
        return -1








