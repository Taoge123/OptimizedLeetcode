
class Solution:
    def minimumMoves(self, grid) -> int:
        # 判断蛇的状态
        def snake_state(r1, c1, r2, c2):
            if r1 == r2 and c1 + 1 == c2:
                return 1
            else:
                return 2

        n = len(grid)
        step = 0
        queue = collections.deque()
        queue.append([0, 0, 0, 1])
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                r1, c1, r2, c2 = queue.popleft()
                if r1 == n - 1 and c1 == n - 2 and r2 == n - 1 and c2 == n - 1:
                    return step
                # 判断状态
                if snake_state(r1 ,c1 ,r2 ,c2) == 1:
                    # 水平状态
                    # 下方没有障碍物
                    if r1 + 1 < n and grid[r1 + 1][c1] == 0 and grid[r2 + 1][c2] == 0:
                        if (r1 + 1, c1, r2 + 1, c2) not in visited:
                            queue.append((r1 + 1, c1, r2 + 1, c2))
                            visited.add((r1 + 1, c1, r2 + 1, c2))
                        # 判断能否顺时针旋转
                        if (r1 ,c1 ,r1 + 1 ,c1) not in visited:
                            queue.append((r1 ,c1 ,r1 + 1 ,c1))
                            visited.add((r1 ,c1 ,r1 + 1 ,c1))
                    # 向右侧移动
                    if c2 + 1 < n and grid[r2][c2 + 1] == 0:
                        if (r2 ,c2 ,r2 ,c2 + 1) not in visited:
                            queue.append((r2 ,c2 ,r2 ,c2 + 1))
                            visited.add((r2 ,c2 ,r2 ,c2 + 1))
                else:
                    # 竖直状态
                    # 右侧没有障碍物
                    if c2 + 1 < n and grid[r1][c1 + 1] == 0 and grid[r2][c2 + 1] == 0:
                        if (r1, c1 + 1, r2, c2 + 1) not in visited:
                            queue.append((r1, c1 + 1, r2, c2 + 1))
                            visited.add((r1, c1 + 1, r2, c2 + 1))
                        # 判断能否逆时针旋转
                        if (r1 ,c1 ,r1 ,c1 + 1) not in visited:
                            queue.append((r1 ,c1 ,r1 ,c1 + 1))
                            visited.add((r1 ,c1 ,r1 ,c1 + 1))
                    # 向下侧移动
                    if r2 + 1 < n and grid[r2 + 1][c2] == 0:
                        if (r2, c2, r2 + 1, c2) not in visited:
                            queue.append((r2 ,c2 ,r2 + 1 ,c2))
                            visited.add((r2 ,c2 ,r2 + 1 ,c2))
            step += 1
        return -1



