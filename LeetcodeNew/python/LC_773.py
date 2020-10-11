import collections

class Solution:
    def slidingPuzzle(self, board) -> int:
        m, n = len(board), len(board[0])
        queue = collections.deque()
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        start = []
        for i in range(2):
            for j in range(3):
                start.append(board[i][j])

        if start == [1, 2, 3, 4, 5, 0]:
            return 0

        #we need to use tuple becuz its immutable
        queue.append(tuple(start))
        visited = set()
        visited.add(tuple(start))
        step = -1

        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                node = queue.popleft()
                node = list(node)
                pos1 = node.index(0)
                i, j = pos1 // n, pos1 % n
                for dx, dy in self.directions:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    pos2 = x * n + y
                    newNode = list(node)
                    newNode[pos1], newNode[pos2] = newNode[pos2], newNode[pos1]
                    if newNode == [1, 2, 3, 4, 5, 0]:
                        return step + 1

                    if tuple(newNode) in visited:
                        continue
                    queue.append(tuple(newNode))
                    visited.add(tuple(newNode))
        return -1





board = [[1,2,3],
         [4,0,5]]
a = Solution()
print(a.slidingPuzzle(board))






