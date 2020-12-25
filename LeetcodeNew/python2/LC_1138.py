import collections


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def bfs(i, j, ch):
            visited = set()
            queue = collections.deque([(i, j, '')])
            while queue:
                size = len(queue)
                for _ in range(size):
                    i, j, moves = queue.popleft()
                    if ch == board[i][j]:
                        return i, j, moves + '!'
                    for _, (dx, dy, step) in enumerate([(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]):
                        x = i + dx
                        y = j + dy

                        if (x, y) in visited:
                            continue

                        if 0 <= x < m and 0 <= y < n and board[x][y] != '0':
                            queue.append((x, y, moves + step))
                            visited.add((x, y))

        x, y, res = 0, 0, ''
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z0000"]
        m, n = len(board), len(board[0])
        for i in range(len(target)):
            x, y, moves = bfs(x, y, target[i])
            res = res + moves
        return res

