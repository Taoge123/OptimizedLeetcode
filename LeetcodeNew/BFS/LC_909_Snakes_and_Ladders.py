
"""
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board,
 and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:


You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move:
if the destination to a snake or ladder is the start of another snake or ladder,
you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`,
and on the first move your destination square is `2`, then you finish your first move at `3`,
because you do not continue moving to `4`.)
"""

"""
Intuition

As we are looking for a shortest path, a breadth-first search is ideal. 
The main difficulty is to handle enumerating all possible moves from each square.

Algorithm

Suppose we are on a square with number s. 
We would like to know all final destinations with number s2 after making one move.

This requires knowing the coordinates get(s2) of square s2. This is a small puzzle in itself: 
we know that the row changes every N squares, and so is only based on quot = (s2-1) / N; 
also the column is only based on rem = (s2-1) % N and what row we are on (forwards or backwards.)

From there, we perform a breadth first search, where the nodes are the square numbers s.
"""
import collections

class SolutionLee:
    def snakesAndLadders(self, board):
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x + 1, x + 7):
                a, b = (i - 1) / n, (i - 1) % n
                #means index from right
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0: i = nxt
                if i == n * n: return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1


class Solution:
    def snakesAndLadders(self, board):
        arr, nn, q, seen, moves = [0], len(board) ** 2, [1], set(), 0
        for i, row in enumerate(board[::-1]): arr += row[::-1] if i % 2 else row
        while q:
            new = []
            for sq in q:
                if sq == nn: return moves
                for i in range(1, 7):
                    if sq + i <= nn and sq + i not in seen:
                        seen.add(sq + i)
                        new.append(sq + i if arr[sq + i] == -1 else arr[sq + i])
            q, moves = new, moves + 1
        return -1


class Solution2:
    def snakesAndLadders(self, board):
        N = len(board)

        def get(s):
            # Given a square num s, return board coordinates (r, c)
            quot, rem = divmod(s-1, N)
            row = N - 1 - quot
            col = rem if row%2 != N%2 else N - 1 - rem
            return row, col

        dist = {1: 0}
        queue = collections.deque([1])
        while queue:
            s = queue.popleft()
            if s == N*N: return dist[s]
            for s2 in range(s+1, min(s+6, N*N) + 1):
                r, c = get(s2)
                if board[r][c] != -1:
                    s2 = board[r][c]
                if s2 not in dist:
                    dist[s2] = dist[s] + 1
                    queue.append(s2)
        return -1










