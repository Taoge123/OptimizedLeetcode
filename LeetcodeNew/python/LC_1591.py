"""
1 2 1
2 1 3
2 4 4

(0, 0) : 1,2   -> 2 < 1
(2, 0) : 1, 2  -> 1 < 2
(2, 1) : 1,2,4 -> (1, 2) < 4
(1, 2) : 1,3   -> 1 < 3
(2, 2) : 1,4   -> 1 < 4
...

"""


class Solution:
    def isPrintable(self, targetGrid) -> bool:
        m = len(targetGrid)
        n = len(targetGrid[0])

        left, right = [n] * 61, [-1] * 61
        top, bottom = [m] * 61, [-1] * 61

        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                left[color] = min(left[color], j)
                right[color] = max(right[color], j)
                top[color] = min(top[color], i)
                bottom[color] = max(bottom[color], i)


        self.graph = [[] for i in range(61)]
        visited = [0] * 61

        for i in range(m):
            for j in range(n):
                for color in range(1, 61):
                    if i >= top[color] and i <= bottom[color] and j >= left[color] and j <= right[color]:
                        if color != targetGrid[i][j]:
                            self.graph[targetGrid[i][j]].append(color)

        for i in range(1, 61):
            if self.dfs(i, visited) == False:
                return False
        return True

    # 判断有环
    def dfs(self, node, visited):
        if visited[node] == 1:
            return True
        visited[node] = 2

        for nei in self.graph[node]:
            if visited[nei] == 1:
                continue
            if visited[nei] == 2:
                return False
            if self.dfs(nei, visited) == False:
                return False

        visited[node] = 1
        return True





