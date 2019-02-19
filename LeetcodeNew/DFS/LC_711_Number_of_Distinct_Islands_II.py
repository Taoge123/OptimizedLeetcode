
"""
Algorithm

We feature two different implementations,
but the core idea is the same. We start with the code from the previous problem,
Number of Distinct Islands. For each of 8 possible rotations and reflections of the shape,
we will perform the transformation and then translate the shape
so that the bottom-left-most coordinate is (0, 0). Afterwards,
we will consider the canonical hash of the shape to be the maximum of these 8 intermediate hashes.

In Python, the motivation to use complex numbers is that rotation by 90 degrees
is the same as multiplying by the imaginary unit, 1j.
In Java, we manipulate the coordinates directly.
The 8 rotations and reflections of each point
are (x, y), (-x, y), (x, -y), (-x, -y), (y, x), (-y, x), (y, -x), (-y, -x).
"""

class Solution(object):
    def numDistinctIslands2(self, grid):
        seen = set()
        def explore(r, c):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add(complex(r, c))
                explore(r+1, c)
                explore(r-1, c)
                explore(r, c+1)
                explore(r, c-1)

        def canonical(shape):
            def translate(shape):
                w = complex(min(z.real for z in shape),
                            min(z.imag for z in shape))
                return sorted(str(z-w) for z in shape)

            ans = None
            for k in range(4):
                ans = max(ans, translate([z * (1j)**k for z in shape]))
                ans = max(ans,  translate([complex(z.imag, z.real) * (1j)**k
                                           for z in shape]))
            return tuple(ans)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c)
                if shape:
                    shapes.add(canonical(shape))

        return len(shapes)


class Solution2:
    def dfs(self, grid, r, c, shape):
        grid[r][c] = 0
        shape.append((r, c))

        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        for d in directions:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0:
                self.dfs(grid, nr, nc, shape)

    def normalize(self, shape):
        rotated_shapes = [[] for _ in xrange(8)]
        norm_res = []

        for p in shape:
            x, y = p
            rotated_shapes[0].append((x, y))
            rotated_shapes[1].append((-x, y))
            rotated_shapes[2].append((x, -y))
            rotated_shapes[3].append((-x, -y))
            rotated_shapes[4].append((y, x))
            rotated_shapes[5].append((-y, x))
            rotated_shapes[6].append((y, -x))
            rotated_shapes[7].append((-y, -x))

        for rs in rotated_shapes:
            rs.sort()

        for rs in rotated_shapes:
            tmp = [(0, 0)]
            for i in xrange(1, len(rs)):
                tmp.append((rs[i][0] - rs[0][0], rs[i][1] - rs[0][1]))
            norm_res.append(tmp[:])

        norm_res.sort()

        return tuple(norm_res[0])

    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = set()
        for r in range(0, m):
            for c in range(0, n):
                if grid[r][c] == 1:
                    shape = []
                    self.dfs(grid, r, c, shape)
                    norm = self.normalize(shape)
                    res.add(norm)

        return len(res)





