import collections


class Solution:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        visited = set()
        queue = collections.deque()
        queue.append((1, 0))
        while queue:
            node, step = queue.popleft()
            i, j = self.convert(node, n)
            if board[i][j] != -1:
                node = board[i][j]
            if node == n * n:
                return step
            for x in range(1, 7):
                newNode = node + x
                if newNode <= n * n and newNode not in visited:
                    visited.add(newNode)
                    queue.append((newNode, step + 1))
        return -1


    def convert(self, node, n):
        row, col = divmod(node - 1, n)
        if row % 2 == 0:
            return n - 1 - row, col
        else:
            return n - 1 - row, n - 1 - col