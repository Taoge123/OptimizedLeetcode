
class SolutionDFS:
    def maxStudents(self, seats) -> int:
        m, n = len(seats), len(seats[0])
        table = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '.':
                    table[i] |= (1 << j)
                else:
                    table[i] |= 0
        memo = {}
        return self.dfs(seats, 0, 0, table, memo)

    def dfs(self, seats, state, pos, table, memo):
        m, n = len(seats), len(seats[0])
        if (state, pos) in memo:
            return memo[(state, pos)]

        if pos == m:
            return 0

        res = 0
        for newState in range(1 << n):
            # check if there is no adjancent students in the row
            if (newState & table[pos]) == newState and newState & (newState << 1) == 0:
                # no students in the upper left positions and upper right positions
                if (state << 1) & newState == 0 and (newState << 1) & state == 0:
                    res = max(res, self.count(newState) + self.dfs(seats, newState, pos + 1, table, memo))
        memo[(state, pos)] = res
        return memo[(state, pos)]

    def count(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count