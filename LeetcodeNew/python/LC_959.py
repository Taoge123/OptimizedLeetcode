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


class Solution:
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
        self.parent[a] = b

    def regionsBySlashes(self, grid):
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
        print(list(map(self.find, self.parent)))
        return len(set(map(self.find, self.parent)))


grid = [" /","/ "]
a = Solution()
print(a.regionsBySlashes(grid))





