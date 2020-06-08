import collections


class Solution:
    def cutOffTree(self, forest) -> int:
        m, n = len(forest), len(forest[0])
        nums = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
        nums = sorted(nums)
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        print(nums)
        i, j = 0, 0
        res = 0
        for num, x, y in nums:
            steps = self.bfs(forest, i, j, x, y)  # step 3
            if steps == -1 :
                return -1
            res += steps
            i = x
            j = y

        return res


    def bfs(self, forest, i, j, x, y) :
        m, n = len(forest), len(forest[0])
        visited = [ [False for j in range(n)] for i in range(m)]
        queue = collections.deque()
        queue.append((i ,j ,0))
        while queue:
            i, j, step = queue.popleft()
            if [i, j] == [x, y] :
                return step
            for dx, dy in self.directions:
                r = i + dx
                c = j + dy
                if r >= 0 and r < m and c >= 0 and c < n and not visited[r][c] and forest[r][c] > 0:
                    visited[r][c] = True
                    queue.append((r, c, step + 1))
        return -1



