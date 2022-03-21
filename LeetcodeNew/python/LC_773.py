import collections

"""
graph[(0, 0)] = [(0, 1), (1, 0)]
graph[(0, 1)] = [(0, 0), (0, 2), (1, 1)]
graph[(0, 2)] = [(0, 1), (1, 2)]
graph[(1, 0)] = [(0, 0), (1, 1)]
graph[(1, 1)] = [(1, 0), (0, 1), (1, 2)]
graph[(1, 2)] = [(0, 2), (1, 1)]

00 -> 01 10
01 -> 00 02 11
02 -> 01 12
10 -> 00 11
11 -> 10 01 12
12 -> 02 11

0 : 1 3
1 : 0 2 4
2 : 1 5
3 : 0 4
4 : 3 1 5
5 : 2 4

00 = 0
01 = 1
02 = 2
10 = 3
11 = 4
12 = 5

"""

import collections

class SolutionTonyBFS:
    def slidingPuzzle(self, board) -> int:

        graph = collections.defaultdict(list)
        graph[0] = [1, 3]
        graph[1] = [0, 2, 4]
        graph[2] = [1, 5]
        graph[3] = [0, 4]
        graph[4] = [1, 3, 5]
        graph[5] = [2, 4]

        target = '123450'

        queue = collections.deque()
        node = ""
        for row in board:
            for col in row:
                node += str(col)

        queue.append(node)
        visited = set()
        step = 0

        def swap(node, i, j):
            node = list(node)
            node_i = node[i]
            node_j = node[j]
            for k in range(len(node)):
                if k == i:
                    node[i] = node_j
                if k == j:
                    node[j] = node_i
            return "".join(node)

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node == target:
                    return step
                i = node.index('0')
                for j in graph[i]:
                    new_node = swap(node, i, j)
                    if new_node in visited:
                        continue
                    visited.add(new_node)
                    queue.append(new_node)

            step += 1
        return -1




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
        step = 0

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
                        return step

                    if tuple(newNode) in visited:
                        continue
                    queue.append(tuple(newNode))
                    visited.add(tuple(newNode))
            step += 1
        return -1





board = [[1,2,3],
         [4,0,5]]
a = Solution()
print(a.slidingPuzzle(board))






