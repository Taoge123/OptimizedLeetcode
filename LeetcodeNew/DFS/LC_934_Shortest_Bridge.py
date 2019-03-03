"""
https://buptwc.com/2018/11/05/leetcode-934-Shortest-Bridge/
https://blog.csdn.net/fuxuemingzhu/article/details/83716820
https://blog.csdn.net/qq_17550379/article/details/84283602
https://www.geeksforgeeks.org/bridge-in-a-graph/


Idea is straightforward.
We get root of first island from "first" function
We dfs root and add indexes to bfs
We bfs and expand the first island in other words
Finally return step number when facing other island
Note: This can also be done with referenced array if you don't want to modify A.

"""
import collections

class Solution:
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * N for _ in range(M)]
        hasfind = False
        que = collections.deque()
        for i in range(M):
            if hasfind: break
            for j in range(N):
                if A[i][j] == 1:
                    self.dfs(A, i, j, visited, que)
                    hasfind = True
                    break
        step = 0
        while que:
            size = len(que)
            for _ in range(size):
                i, j = que.popleft()
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < M and 0 <= y < N:
                        visited[x][y] = 1
                        if A[x][y] == 1:
                            return step
                        elif A[x][y] == 0:
                            A[x][y] = 2
                            que.append((x, y))
                        else:
                            continue
            step += 1
        return -1

    def dfs(self, A, i, j, visited, que):
        if visited[i][j]: return
        visited[i][j] = 1
        M, N = len(A), len(A[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if A[i][j] == 1:
            que.append((i, j))
            A[i][j] = 2
            for d in dirs:
                x, y = i + d[0], j + d[1]
                if 0 <= x < M and 0 <= y < N:
                    self.dfs(A, x, y, visited, que)
# ---------------------
# 作者：负雪明烛
# 来源：CSDN
# 原文：https://blog.csdn.net/fuxuemingzhu/article/details/83716820
# 版权声明：本文为博主原创文章，转载请附上博文链接！

class Solution2:
    def shortestBridge(self, A):
        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j


        n, step, bfs = len(A), 0, []
        dfs(*first())

        print(first())
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            bfs = new

A = [[0,1,0],[0,0,0],[0,0,1]]
a = Solution()
a.shortestBridge(A)


class Solution:
    def shortestBridge(self, A):

        row, col = len(A), len(A[0])
        visited = [[0] * col for _ in range(row)]  # 负责记录其中的一个岛
        q = []
        start = []  # 保存其中一个岛的所有位置
        found = False
        for i in range(row):  # 先找到一个岛中其中一个位置
            for j in range(col):
                if A[i][j] == 1:
                    found = True
                    q.append((i, j))
                    visited[i][j] = 1
                    break
            if found:
                break

        while q:  # 以其中一个岛的位置为基础，使用广度优先搜索方法，继续找到这个岛的其他位置
            tmp = []
            for a in q:
                x, y = a[0], a[1]
                start.append(a)  # 把岛的位置放到 start 队列里面
                if (x - 1 >= 0) and (visited[x - 1][y] == 0) and (A[x - 1][y] == 1):
                    tmp.append((x - 1, y))
                    visited[x - 1][y] = 1
                if (x + 1 < col) and (visited[x + 1][y] == 0) and (A[x + 1][y] == 1):
                    tmp.append((x + 1, y))
                    visited[x + 1][y] = 1
                if (y - 1 >= 0) and (visited[x][y - 1] == 0) and (A[x][y - 1] == 1):
                    tmp.append((x, y - 1))
                    visited[x][y - 1] = 1
                if (y + 1 < row) and (visited[x][y + 1] == 0) and (A[x][y + 1] == 1):
                    tmp.append((x, y + 1))
                    visited[x][y + 1] = 1
            q = tmp

        ans = 0
        while start:  # 从一个岛出发，去找探索另外一个岛
            tmp = []
            for a in start:  # 广度优先算法，一层一层的探查 是否 到达另外一个岛
                x, y = a[0], a[1]
                if (x - 1 >= 0) and (visited[x - 1][y] == 0):
                    if A[x - 1][y] == 1:
                        return ans
                    else:
                        tmp.append((x - 1, y))
                        visited[x - 1][y] = 1
                if (x + 1 < col) and (visited[x + 1][y] == 0):
                    if A[x + 1][y] == 1:
                        return ans
                    else:
                        tmp.append((x + 1, y))
                        visited[x + 1][y] = 1
                if (y - 1 >= 0) and (visited[x][y - 1] == 0):
                    if A[x][y - 1] == 1:
                        return ans
                    else:
                        tmp.append((x, y - 1))
                        visited[x][y - 1] = 1
                if (y + 1 < row) and (visited[x][y + 1] == 0):
                    if A[x][y + 1] == 1:
                        return ans
                    else:
                        tmp.append((x, y + 1))
                        visited[x][y + 1] = 1

            start = tmp  # 探索了一层之后，没有发现另外一个岛，则，更新 最外层边界 以及 路径长度
            ans += 1

        return ans


if __name__ == '__main__':
    A = [[1, 1, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 0, 0, 1],
         [1, 1, 1, 1, 1]]
    print(Solution().shortestBridge(A))
# ---------------------
# 作者：GorillaNotes
# 来源：CSDN
# 原文：https: // blog.csdn.net / XX_123_1_RJ / article / details / 84656064
# 版权声明：本文为博主原创文章，转载请附上博文链接！

