class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        # no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False

    def isSafe(self, row, col, ch):
        boxrow = row - row % 3
        boxcol = col - col % 3
        if self.checkrow(row, ch) and self.checkcol(col, ch) and self.checksquare(boxrow, boxcol, ch):
            return True
        return False

    def checkrow(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checkcol(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def checksquare(self, row, col, ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True


#Solution 2

"""
Keep track of possible numbers in each column, each row and each 3*3 square in sets.
Always DFS the empty block with minimum number of possible numbers.
"""


class Solution(object):

    def DFS(self, empty, colnum, rownum, sqnum, board):
        if len(empty) == 0:
            return True

        maxpossiblelen = 9
        for (r, c) in empty:
            possible = rownum[r] & colnum[c] & sqnum[r / 3][c / 3]
            if len(possible) <= maxpossiblelen:
                maxpossiblelen = len(possible)
                i, j = r, c

        if maxpossiblelen == 0:
            return False

        empty.remove((i, j))
        possible = rownum[i] & colnum[j] & sqnum[i / 3][j / 3]

        for num in possible:
            rownum[i].remove(num)
            colnum[j].remove(num)
            sqnum[i / 3][j / 3].remove(num)
            board[i][j] = str(num)
            if self.DFS(empty, colnum, rownum, sqnum, board):
                return True
            board[i][j] = '.'
            rownum[i].add(num)
            colnum[j].add(num)
            sqnum[i / 3][j / 3].add(num)

        empty.add((i, j))
        return False

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        colnum = []
        rownum = []
        sqnum = [[0] * 3 for _ in range(3)]
        for i in range(9):
            colnum.append(set(tuple(range(1, 10))))
            rownum.append(set(tuple(range(1, 10))))

        for i in range(3):
            for j in range(3):
                sqnum[i][j] = set(tuple(range(1, 10)))

        empty = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if int(board[i][j]) in rownum[i]:
                        rownum[i].remove(int(board[i][j]))
                    if int(board[i][j]) in colnum[j]:
                        colnum[j].remove(int(board[i][j]))
                    if int(board[i][j]) in sqnum[i / 3][j / 3]:
                        sqnum[i / 3][j / 3].remove(int(board[i][j]))
                else:
                    empty.add((i, j))

        self.DFS(empty, colnum, rownum, sqnum, board)


        


