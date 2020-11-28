"""
https://www.youtube.com/watch?v=RwmNMRdnLl0&feature=youtu.be


1263.Minimum-Moves-to-Move-a-Box-to-Their-Target-Location
这道题可以用比较粗暴的BFS来实现。每个状态包括(bx,by,px,py)表示box和person的坐标，同时用一个四维数组flag[bx][by][px][py]来记录到达这个状态需要多少次移动（move）。

每次从队列中弹出一个状态，我们就遍历person朝四个方向可以变动的位置，再加入队列之中。
注意到这个新状态对应的最少移动次数flag[bx][by][px_new][py_new]=flag[bx][by][px][py]不会变化，
但如果我们仍然依照传统BFS的策略将这个新状态加入队列末尾，可能会导致队列中的状态所对应的move不是递增的，
最终无法搜索到正确的最少move次数。解决方法是：用deque而不是queue，将这个新状态加入到队列的首端而不是末端！完美！

对于每次从队列中弹出的一个状态，我们还需要查看person是否就在box的四周且可以推动它。如果是的话，我们就推动盒子，从而得到新的状态(bx_new,by_new,bx,by)。易知flag[bx_new][by_new][bx][by]=flag[bx][by][px][py]+1。所以我们应该将这个新状态应该加入双端队列的末尾！

这种用双端队列来实现BFS的技巧，值得好好体会！

"""



import collections

class Solution:
    def minPushBox(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        bx, by, px, py = 0, 0, 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    px, py = i, j
                    grid[i][j] = '.'
                elif grid[i][j] == 'B':
                    bx, by = i, j
                    grid[i][j] = '.'
                elif grid[i][j] == 'T':
                    tx, ty = i, j
                    grid[i][j] = '.'

        queue = collections.deque()
        queue.append([bx, by, px, py])
        memo = collections.defaultdict(lambda : -1)
        memo[(bx, by, px, py)] = 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            bx, by, px, py = queue.popleft()
            if bx == tx and by == ty:
                return memo[(bx, by, px, py)]

            for k in range(4):
                x = px + directions[k][0]
                y = py + directions[k][1]
                if x< 0 or x >= m or y < 0 or y >= n:
                    continue
                if grid[x][y] != '.':
                    continue
                #人和盒子
                if x == bx and y == by:
                    continue
                if memo[(bx, by, x, y)] >= 0:
                    continue
                memo[(bx, by, x, y)] = memo[(bx, by, px, py)]
                queue.appendleft([bx, by, x, y])

            # 相邻
            if abs(px - bx) + abs(py - by) == 1:
                for k in range(4):
                    # 找到方向 k 然后推着箱子走
                    if px + directions[k][0] == bx and py + directions[k][1] == by:
                        bx2 = bx + directions[k][0]
                        by2 = by + directions[k][1]
                        if bx2 < 0 or bx2 >= m or by2 < 0 or by2 >= n:
                            continue
                        if grid[bx2][by2] != '.':
                            continue
                        if memo[(bx2, by2, bx, by)] >= 0:
                            continue
                        memo[(bx2, by2, bx, by)] = memo[(bx, by, px, py)] + 1
                        queue.append([bx2, by2, bx, by])
        return -1



