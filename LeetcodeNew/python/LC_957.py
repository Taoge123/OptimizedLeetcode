


class Solution:
    def prisonAfterNDays(self, cells, N):
        visited = {}
        while N > 0:
            nums = tuple(cells)
            if nums in visited: 
                N %= visited[nums] - N
            visited[nums] = N

            if N >= 1:
                N -= 1
                cells = self.nextday(cells)

        return cells

    def nextday(self, cells):
        return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1]) for i in range(8)]



cells = [1,0,0,1,0,0,1,0]
N = 1000000000


a = Solution()
print(a.prisonAfterNDays(cells, N))
