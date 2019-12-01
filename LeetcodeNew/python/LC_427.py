
"""
We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false.
The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node.
The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:



It can be divided according to the definition above:





The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.



Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
"""

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight



class Solution:
    def construct(self, grid) -> 'Node':
        if not grid:
            return None

        m, n = len(grid), len(grid[0])

        if self.isLeaf(grid, m, n):
            return Node(grid[0][0] == 1, True, None, None, None, None)

        n = len(grid)

        return Node('*', False,
                    self.construct([row[:n//2] for row in grid[:n//2]]),
                    self.construct([row[n//2:] for row in grid[:n//2]]),
                    self.construct([row[:n//2] for row in grid[n//2:]]),
                    self.construct([row[n//2:] for row in grid[n//2:]]))

    def isLeaf(self, grid, m, n):
        return all(grid[i][j] == grid[0][0] for i in range(m) for j in range(n))


class Solution2:
    def construct(self, grid):

        N = len(grid)
        if N == 1:
            return Node(grid[0][0] == 1, True, None, None, None, None)
        topLeftSum = sum([grid[i][j] for i in range(N // 2) for j in range(N // 2)])
        topRightSum = sum([grid[i][j] for i in range(N // 2) for j in range(N // 2, N)])
        bottomLeftSum = sum([grid[i][j] for i in range(N // 2, N) for j in range(N // 2)])
        bottomRightSum = sum(grid[i][j] for i in range(N // 2, N) for j in range(N // 2, N))
        node = Node(False, False, None, None, None, None)
        if topLeftSum == topRightSum == bottomLeftSum == bottomRightSum:
            if topLeftSum == 0:
                node.isLeaf = True
                node.val = False
            elif topLeftSum == (N // 2) ** 2:
                node.isLeaf = True
                node.val = True
        if node.isLeaf:
            return node
        node.val = True
        node.topLeft = self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2)])
        node.topRight = self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2)])
        node.bottomLeft = self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2, N)])
        node.bottomRight = self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2, N)])
        return node






