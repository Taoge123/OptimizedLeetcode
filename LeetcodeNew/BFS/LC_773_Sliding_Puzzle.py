
"""
http://www.cnblogs.com/grandyang/p/8955735.html

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board,
return the least number of moves required so that the state of the board is solved.
If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14

"""

class Solution:
    def slidingPuzzle(self, board):
        moves, used, cnt = {0: {1, 3}, 1:{0, 2, 4}, 2:{1, 5}, 3:{0, 4}, 4:{1, 3, 5}, 5:{2, 4}}, set(), 0
        s = "".join(str(c) for row in board for c in row)
        q = [(s, s.index("0"))]
        while q:
            new = []
            for s, i in q:
                used.add(s)
                if s == "123450":
                    return cnt
                arr = [c for c in s]
                for move in moves[i]:
                    new_arr = arr[:]
                    new_arr[i], new_arr[move] = new_arr[move], new_arr[i]
                    new_s = "".join(new_arr)
                    if new_s not in used:
                        new.append((new_s, move))
            cnt += 1
            q = new
        return -1


"""
We can think of this problem as a shortest path problem on a graph. 
Each node is a different board state, 
and we connect two boards by an edge if they can be transformed into one another in one move. 
We can solve shortest path problems with breadth first search.
For our breadth first search, we will need to be able to represent the nodes as something hashable, 
and we'll need to enumerate the neighbors of a board. Afterwards, 
we can use a typical template for breadth-first search:
"""

"""
queue = collections.deque([(start, 0)])
seen = {start}
while queue:
    node, depth = queue.popleft()
    if node == target: return depth
    for nei in neighbors(node):
        if nei not in seen:
            seen.add(nei)
            queue.append((nei, depth+1))
"""


"""
To represent the nodes as something hashable, in Python, 
we convert the board to 1 dimension and use a tuple; 
in Java we can either encode the board as an integer, or more generally use Arrays.deepToString.

To enumerate the neighbors of a board, we'll remember where the zero is. 
Then, there are only 4 possible neighbors. If the board is flattened to 1 dimension, 
these neighbors occur at distances (1, -1, C, -C) from the zero, where C is the number of columns in the board.
"""
import collections
import itertools

class Solution2:
    def slidingPuzzle(self, board):
        R, C = len(board), len(board[0])
        #[[1, 2, 3], [4, 0, 5]] - >(1, 2, 3, 4, 0, 5)
        start = tuple(itertools.chain(*board))
        queue = collections.deque([(start, start.index(0), 0)])
        seen = {start}

        target = tuple(range(1, R*C) + [0])

        while queue:
            board, posn, depth = queue.popleft()
            if board == target: return depth
            for d in (-1, 1, -C, C):
                nei = posn + d
                if abs(nei/C - posn/C) + abs(nei%C - posn%C) != 1:
                    continue
                if 0 <= nei < R*C:
                    newboard = list(board)
                    newboard[posn], newboard[nei] = newboard[nei], newboard[posn]
                    newt = tuple(newboard)
                    if newt not in seen:
                        seen.add(newt)
                        queue.append((newt, nei, depth+1))

        return -1

"""
Complexity Analysis

Time Complexity: O(R * C * (R * C)!)O(R∗C∗(R∗C)!), where R, CR,C are the number of rows and columns in board. There are O((R * C)!)O((R∗C)!) possible board states.

Space Complexity: O(R * C * (R * C)!)O(R∗C∗(R∗C)!).
"""


class Solution3:
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        goal = "123450"
        boardStr = self.boardtoStr(board)
        q = collections.deque()
        q.append((boardStr, 0))
        dxs = [-1, 0, 1, 0]
        dys = [0, 1, 0, -1]
        m = len(board)
        n = len(board[0])
        visited = set()
        visited.add(boardStr)

        while q:
            path, step = q.popleft()
            if path == goal:
                return step

            zeroIndex = path.index("0")
            x, y = zeroIndex / n, zeroIndex % n
            path = list(path)

            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                path[nx * n + ny], path[x * n + y] = path[x * n + y], path[nx * n + ny]
                pathStr = "".join(path)

                if pathStr not in visited:
                    q.append((pathStr, step + 1))
                    visited.add(pathStr)
                path[nx * n + ny], path[x * n + y] = path[x * n + y], path[nx * n + ny]

        return -1

    def boardtoStr(self, board):

        ss = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                ss += str(board[i][j])

        return ss



    





