


class SolutionBFS:
    def minFlips(self, mat) -> int:
        def filp(state, i, j):
            for dx, dy in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + dx
                y = j + dy
                print(i, j, x, y)
                if 0 <= x < m and 0 <= y < n:
                    state ^= (1 << (x * n + y))
            return state

        m, n = len(mat), len(mat[0])
        state = 0
        for i in range(m):
            for j in range(n):
                state |= (mat[i][j] << (i * n + j))

        queue = collections.deque([(state, 0)])
        visited = set([state])
        while queue:
            state, steps = queue.popleft()
            if state == 0:
                return steps
            for i in range(m):
                for j in range(n):
                    newState = filp(state, i, j)
                    if newState not in visited:
                        visited.add(newState)
                        queue.append((newState, steps + 1))
        return -1

