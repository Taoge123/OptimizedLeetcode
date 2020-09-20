import collections
import heapq


class Solution2:
    def cutOffTree(self, forest) -> int:
        if not forest or len(forest) == 0:
            return 0
        m, n = len(forest), len(forest[0])

        heap = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    heapq.heappush(heap, (forest[i][j], i, j))

        start = [0, 0]
        res = 0
        while heap:
            dest = heapq.heappop(heap)
            step = self.minStep(forest, start, dest, m, n)
            if step < 0:
                return -1
            res += step
            start[0] = dest[1]
            start[1] = dest[2]
        return res

    def minStep(self, forest, start, dest, m, n):
        step = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = collections.deque()
        queue.append(start)
        visited = [[False for i in range(n)] for j in range(m)]
        visited[start[0]][start[1]] = True

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node[0] == dest[1] and node[1] == dest[2]:
                    return step
                for dx, dy in directions:
                    newX = node[0] + dx
                    newY = node[1] + dy
                    if newX < 0 or newX >= m or newY < 0 or newY >= n or forest[newX][newY] == 0 or visited[newX][newY]:
                        continue
                    queue.append([newX, newY])
                    visited[newX][newY] = True
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