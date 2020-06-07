"""
Split a cell in to 4 parts like this.
We give it a number top is 1, right is 2, bottom is 3 left is 4.



Two adjacent parts in different cells are contiguous regions.
In case '/', top and left are contiguous, botton and right are contiguous.
In case '\\', top and right are contiguous, bottom and left are contiguous.
In case ' ', all 4 parts are contiguous.

Congratulation.
Now you have another problem of counting the number of islands.

DFS will be good enough to solve it.
As I did in 947.Most Stones Removed with Same Row or Column
I solve it with union find.

Good luck and have fun.


"""


class SolutionUF:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        if a != b:
            self.parent[a] = b
            self.count -= 1

    def regionsBySlashes(self, grid):
        n = len(grid)
        self.count = n * n * 4
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    self.union((i - 1, j, 2), (i, j, 0))
                if j:
                    self.union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    self.union((i, j, 0), (i, j, 1))
                    self.union((i, j, 2), (i, j, 3))
                if grid[i][j] != "\\":
                    self.union((i, j, 3), (i, j, 0))
                    self.union((i, j, 1), (i, j, 2))

        return self.count





class SolutionDFS:
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)
        matrix = [[0 for i in range(n * 3)] for j in range(n * 3)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    print(i*3, j*3)
                    matrix[i * 3 + 0][j * 3 + 2] = 1
                    matrix[i * 3 + 1][j * 3 + 1] = 1
                    matrix[i * 3 + 2][j * 3 + 0] = 1
                elif grid[i][j] == '\\':
                    matrix[i * 3 + 0][j * 3 + 0] = 1
                    matrix[i * 3 + 1][j * 3 + 1] = 1
                    matrix[i * 3 + 2][j * 3 + 2] = 1
        print(matrix)
        self.count = 0
        for i in range(n * 3):
            for j in range(n * 3):
                if matrix[i][j] == 0:
                    self.dfs(matrix, i, j)
                    self.count += 1

        return self.count

    def dfs(self, matrix, i, j):
        n = len(matrix)
        if i < 0 or i >= n or j < 0 or j >= n:
            return
        if matrix[i][j] != 0:
            return
        matrix[i][j] = 2
        for dx, dy in self.directions:
            x = i + dx
            y = j + dy
            self.dfs(matrix, x, y)



grid = [" /","/ "]
a = SolutionUF()
print(a.regionsBySlashes(grid))





