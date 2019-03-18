
"""
https://leetcode.com/problems/shortest-distance-from-all-buildings/discuss/193324/Py3-Python-Optimisation-with-Standard-BFS-Comments-included-self-explained-CODE

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance.
You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building.
If it is not possible to build such house according to the above rules, return -1.


"""


"""
Use hit to record how many times a 0 grid has been reached 
and use distSum to record the sum of distance from all 1 grids to this 0 grid. 
A powerful pruning is that during the BFS we use count1 to count how many 1 grids we reached. 
If count1 < buildings then we know not all 1 grids are connected are we can return -1 immediately, 
which greatly improved speed (beat 100% submissions)
"""

"""
这道题目让我想起了 multi-end BFS
就是从多个building同时出发，一起遍历。
但是问题在于，如何标志，这个 empty area 被多个Building访问过后的状态？
我没仔细想，直接看了答案。
目前的这个解法，感觉并不是最优的，时间复杂度达到了
O(m * n * m * n)
他解决我说的问题的方法是，
对building 一个个进行BFS，同时维护两个数组，一个累加距离，一个累加到这个点的building 个数。
最后再遍历这个距离数组，如果到这个点的building 个数  =  总building个数，那么这个点可以作为一个最短点，然后我们判断下他的总距离是否最小，如果最小，就更新最小值。
同时，记住， BFS的时候，我们需要一个变量level，这是必须的，用来记录每次距离应该加多少。
时间不知不觉到了10月份了。。好久没刷题了。
加油。未来，就在这最后一个月！

作者：Richardo92
链接：https://www.jianshu.com/p/c38f93f6431f
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

我们可以从一个建筑物出发来计算每一个空地到这个建筑物的距离, 
然后设置一个数组sumDistance来累加统计从一个空地出发到其他所有建筑物的距离.
即sumDistance[i][j]代表从位置grid[i][j]出发到其他建筑物的距离之和.

其中在从一个建筑出发寻找所有空地到其距离的时候, 我们使用bfs来计算, 
并且可以每次访问地图的一个结点之后将其值-1, 用作标记已经访问过此结点, 
也用于标记下一次可访问这个结点.这样就避免了再开一个数组来标记是否访问过.
--------------------- 
作者：小榕流光 
来源：CSDN 
原文：https://blog.csdn.net/qq508618087/article/details/50987002 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

import collections



class Solution2:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])

        distance = [[0 for _ in range(w)] for _ in range(h)]
        reach = [[0 for _ in range(w)] for _ in range(h)]

        buildingNum = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    buildingNum += 1
                    q = [(i, j, 0)]

                    isVisited = [[False for _ in range(w)] for _ in range(h)]

                    for y, x, d in q:
                        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                            r = y + dy
                            c = x + dx

                            if 0 <= r < h and 0 <= c < w and grid[r][c] == 0 and not isVisited[r][c]:
                                distance[r][c] += d + 1
                                reach[r][c] += 1

                                isVisited[r][c] = True
                                q.append((r, c, d + 1))

        shortest = float("inf")
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    shortest = min(shortest, distance[i][j])

        if shortest < float("inf"):
            return shortest
        else:
            return -1



class Solution:
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1
        M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
        hit = [[0] * N for i in range(M)]
        distSum = [[0] * N for i in range(M)]

        def BFS(start_x, start_y):
            visited = [[False] * N for k in range(M)]
            visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings

        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x, y): return -1
        return min(
            [distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])





class Solution3:
    def shortestDistance(self, grid):
        if not grid or not grid[0]: return -1
        M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
        hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]

        def BFS(start_x, start_y):
            visited = [[False] * N for k in range(M)]
            visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
            while queue:
                x, y, dist = queue.popleft()
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < M and 0 <= j < N and not visited[i][j]:
                        visited[i][j] = True
                        if not grid[i][j]:
                            queue.append((i, j, dist + 1))
                            hit[i][j] += 1
                            distSum[i][j] += dist + 1
                        elif grid[i][j] == 1:
                            count1 += 1
            return count1 == buildings

        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    if not BFS(x, y): return -1
        return min(
            [distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])



