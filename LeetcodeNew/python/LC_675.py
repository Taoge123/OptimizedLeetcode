import collections
import heapq


class SolutionHeap:
    def cutOffTree(self, forest) -> int:

        m, n = len(forest), len(forest[0])
        heap = []

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 0:
                    heapq.heappush(heap, (forest[i][j], i, j))

        i, j = 0, 0
        res = 0
        while heap:
            num, destx, desty = heapq.heappop(heap)
            step = self.bfs(forest, i, j, destx, desty)
            # print(i, j, destx, desty)
            if step < 0:
                return -1

            res += step
            i, j = destx, desty

        return res

    def bfs(self, forest, i, j, destx, desty):
        m, n = len(forest), len(forest[0])
        queue = collections.deque()
        queue.append([i, j])
        visited = set()
        visited.add((i, j))
        step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                i, j = queue.popleft()
                if i == destx and j == desty:
                    return step
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x = i + dx
                    y = j + dy
                    if x < 0 or y < 0 or x >= m or y >= n or forest[x][y] == 0 or (x, y) in visited:
                        continue

                    queue.append([x, y])
                    visited.add((x, y))
            step += 1
        return -1




class Solution:
    def cutOffTree(self, forest) -> int:
        m, n = len(forest), len(forest[0])
        nums = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
        nums = sorted(nums)
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        i, j = 0, 0
        res = 0
        for num, x, y in nums:
            steps = self.bfs(forest, i, j, x, y)  # step 3
            if steps == -1:
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





forest = [[1,2,3],
          [0,0,4],
          [7,6,5]]

a = Solution2()
print(a.cutOffTree(forest))