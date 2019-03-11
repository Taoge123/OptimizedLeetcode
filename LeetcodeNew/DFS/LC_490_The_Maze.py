"""

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.




这里对于stop的判定条件是：球从一个方向朝着end卷过来，能否在end点的下一个位置碰到墙。举个不成立的例子

比如你从左边冲过来，到达了end，虽然end点的上下两头都有墙，但右边没有墙，这种就不符合定义。

思路
有了定义的条件，不难想象这是一道图的遍历。DFS和BFS都行。这里说一下BFS的思路。

BFS前的基础设施
放入Queue的条件：当满足没有被访问过，且是一个新的起始点，我们放入Queue。新的起始点的定义是：从任意方向撞过来，并且触碰到墙后，触碰墙之前的最后一个节点。
Visited数组设立一个和input matrix等长宽的二维boolean数组 (论坛大牛这一步有优化，我就写一个最原始的方法吧)
根据题目尿性的额外设施
方向数组，这个如果不写也行，只是要多写几个方向的判断。写的话，写成上下左右四个方向比较顺溜。
BFS主代码
和一般的BFS没什么区别，先把最开始的起始点从Queue中pop出来，比对Termination Condition(是否和终结点坐标一致)。

不一致的话，就开始上下左右四个方向的滚动，每次滚动都滚到底，之后记住要回撤一部，因为while的终止条件使得最后球的坐标会在一面墙上。
然后对回撤完了的这个节点进行去重比较，没Visited过就放入queue中，成为之后上下左右滚动的起始点
"""

class Solution:
    def hasPath(self, maze, start, destination):

        Q = [start]
        n = len(maze)
        m = len(maze[0])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while Q:
            # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance. Kudos to @whglamrock
            i, j = Q.pop(0)
            maze[i][j] = 2

            if i == destination[0] and j == destination[1]:
                return True

            for x, y in dirs:
                row = i + x
                col = j + y
                while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                    row += x
                    col += y
                row -= x
                col -= y
                if maze[row][col] == 0:
                    Q.append([row, col])

        return False


class Solution(object):
    def hasPath(self, maze, start, destination):
        return self.helper(maze, destination, start[0], start[1])

    def helper(self, maze, dest, i, j):
        if [i, j] == dest:
            return True
        if maze[i][j] == 2:
            return False
        up, down, left, right = i, i, j, j
        while up > 0 and maze[up - 1][j] != 1:
            up -= 1
        while down < len(maze) - 1 and maze[down + 1][j] != 1:
            down += 1
        while left > 0 and maze[i][left - 1] != 1:
            left -= 1
        while right < len(maze[0]) - 1 and maze[i][right + 1] != 1:
            right += 1
        maze[i][j] = 2
        return self.helper(maze, dest, up, j) \
               or self.helper(maze, dest, down, j) \
               or self.helper(maze, dest, i,left) \
               or self.helper(maze, dest, i, right)



class Solution2:
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        def dfs(x, y, stopped):
            if (x, y) in stopped: return False
            stopped.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in ((-1, 0) , (1, 0), (0, -1), (0, 1)):
                newX, newY = x, y
                while 0 <= newX + i < m and 0 <= newY + j < n and maze[newX + i][newY + j] != 1:
                    newX += i
                    newY += j
                if dfs(newX, newY, stopped):
                    return True
            return False
        return dfs(start[0], start[1], set())
