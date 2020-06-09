import collections

class Solution:
    def slidingPuzzle(self, board) -> int:
        queue = collections.deque()
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        s = []
        for i in range(2):
            for j in range(3):
                s.append(board[i][j])

        if s == [1, 2, 3, 4, 5, 0]:
            return 0

        #we need to use tuple becuz its immutable
        queue.append(tuple(s))
        visited = set()
        visited.add(tuple(s))
        step = -1

        while queue:
            # print(queue)
            size = len(queue)
            step += 1
            print(step)
            for _ in range(size):
                node = queue.popleft()
                for i in range(6):
                    if node[i] == 0:
                        pos1 = i
                        break

                i, j = pos1 // 3, pos1 % 3
                for dx, dy in self.directions:
                    x = i + dx
                    y = j + dy
                    if x < 0 or x >= 2 or y < 0 or y >= 3:
                        continue
                    pos2 = x * 3 + y
                    newS = list(node)
                    newS[pos1], newS[pos2] = newS[pos2], newS[pos1]
                    if newS == [1, 2, 3, 4, 5, 0]:
                        return step + 1

                    if tuple(newS) in visited:
                        continue
                    queue.append(tuple(newS))
                    visited.add(tuple(newS))
        return -1






board = [[1,2,3],
         [4,0,5]]
a = Solution()
print(a.slidingPuzzle(board))






