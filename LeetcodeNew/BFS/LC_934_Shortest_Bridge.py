
"""
In a given 2D binary array A, there are two islands.
(An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""

"""
Idea is straightforward.
We get root of first island from "first" function
We dfs root and add indexes to bfs
We bfs and expand the first island in other words
Finally return step number when facing other island
Note: This can also be done with referenced array if you don't want to modify A.

"""

class Solution:
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
        while bfs:
            next = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            next.append((x, y))
            step += 1
            bfs = next


class Solution3:
    def shortestBridge(self, A):
        from collections import deque

        q = deque()

        m = len(A)
        n = len(A[0])
        step = 1
        neighbors = [(0, 1), (0, -1), (1, 0)]

        def dfs(A, x, y):
            if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                q.append((x, y))
                A[x][y] = 2
                dfs(A, x - 1, y)
                dfs(A, x + 1, y)
                dfs(A, x, y + 1)
                dfs(A, x, y - 1)

        # DFS to find first island and put it in queue, mark visited cell as 2
        found = False
        for i in range(m):
            if found:
                break
            for j in range(n):
                if A[i][j] == 1:
                    dfs(A, i, j)
                    found = True
                    break

        # BFS to move one step further if it didn't find the second island,
        # mark visited as 2 and also put it the queue
        while q:
            size = len(q)
            for i in range(size):
                cor = q.popleft()
                for neighbor in neighbors:
                    x = cor[0] + neighbor[0]
                    y = cor[1] + neighbor[1]
                    if x >= m or x < 0 or y < 0 or y >= n or A[x][y] == 2:
                        continue
                    if A[x][y] == 1:
                        return step - 1
                    A[x][y] = 2
                    q.append((x, y))
            step += 1





