"""
https://leetcode.com/problems/redundant-connection/solution/
The trick is to fill in the space between the lines, but since a 2x2 matrix has no spaces in between to work with. The space can be introduce without changing the original problem statement by replacing each character with a 4x4 squares, thereby you need an int array of 4x the dimension to translate the original array. Then iterate through the array and fill in an area in using DFS and return whenever the function hit the border or a divider line (which can be represent by -1, 0 represent the square need to be fill)

[if you try using a 2x2 array for each character, it will break at example 5]

"/"

[ 0, 0, 0,-1]
[ 0, 0,-1, 0]
[ 0,-1, 0, 0]
[-1, 0, 0, 0]

"\"

[-1, 0, 0, 0]
[ 0,-1, 0, 0]
[ 0, 0,-1, 0]
[ 0, 0, 0,-1]

" "
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]

The first example translate to:
[ 0, 0, 0, 0, 0, 0, 0,-1]
[ 0, 0, 0, 0, 0, 0,-1, 0]
[ 0, 0, 0, 0, 0,-1, 0, 0]
[ 0, 0, 0, 0,-1, 0, 0, 0]
[ 0, 0, 0,-1, 0, 0, 0, 0]
[ 0, 0,-1, 0, 0, 0, 0, 0]
[ 0,-1, 0, 0, 0, 0, 0, 0]
[-1, 0, 0, 0, 0, 0, 0, 0]

after the algorithm run:
[ 1, 1, 1, 1, 1, 1, 1,-1]
[ 1, 1, 1, 1, 1, 1,-1, 2]
[ 1, 1, 1, 1, 1,-1, 2, 2]
[ 1, 1, 1, 1,-1, 2, 2, 2]
[ 1, 1, 1,-1, 2, 2, 2, 2]
[ 1, 1,-1, 2, 2, 2, 2, 2]
[ 1,-1, 2, 2, 2, 2, 2, 2]
[-1, 2, 2, 2, 2, 2, 2, 2]

"""

class DSU:
    def __init__(self, N):
        self.parent = range(N)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.parent[xr] = yr

class Solution(object):
    def regionsBySlashes(self, grid):
        N = len(grid)
        dsu = DSU(4 * N * N)
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                root = 4 * (r*N + c)
                if val in '/ ':
                    dsu.union(root + 0, root + 1)
                    dsu.union(root + 2, root + 3)
                if val in '\ ':
                    dsu.union(root + 0, root + 2)
                    dsu.union(root + 1, root + 3)

                # north/south
                if r+1 < N: dsu.union(root + 3, (root+4*N) + 0)
                if r-1 >= 0: dsu.union(root + 0, (root-4*N) + 3)
                # east/west
                if c+1 < N: dsu.union(root + 2, (root+4) + 1)
                if c-1 >= 0: dsu.union(root + 1, (root-4) + 2)

        return sum(dsu.find(x) == x for x in range(4*N*N))







