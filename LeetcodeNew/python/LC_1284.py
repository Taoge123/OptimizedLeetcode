import collections
import copy


class Solution:
    def flip(self, mat, i, j):
        m, n = len(mat), len(mat[0])
        res = copy.deepcopy(mat)
        res[i][j] ^= 1
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            x = i + dx
            y = j + dy
            if 0 <= x < m and 0 <= y < n:
                res[x][y] ^= 1
        return res


    def minFlips(self, mat):
        m, n = len(mat), len(mat[0])

        visited = set()
        queue = collections.deque([[mat, 0]])
        while queue:
            for _ in range(len(queue)):
                node, step = queue.popleft()
                if sum(map(sum, node)) == 0:
                    return step
                for i in range(m):
                    for j in range(n):
                        newNode = self.flip(node, i, j)
                        cur = tuple(map(tuple, newNode))
                        if cur in visited:
                            continue
                        queue.append([newNode, step + 1])
                        visited.add(cur)
        return -1



