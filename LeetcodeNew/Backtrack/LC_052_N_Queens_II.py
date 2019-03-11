

"""
https://leetcode.com/problems/n-queens-ii/solution/


"""


class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def is_not_under_attack(row, col):
            return not (rows[col] or hills[row - col] or dales[row + col])

        def place_queen(row, col):
            rows[col] = 1
            hills[row - col] = 1  # "hill" diagonals
            dales[row + col] = 1  # "dale" diagonals

        def remove_queen(row, col):
            rows[col] = 0
            hills[row - col] = 0  # "hill" diagonals
            dales[row + col] = 0  # "dale" diagonals

        def backtrack(row=0, count=0):
            for col in range(n):
                if is_not_under_attack(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        count += 1
                    else:
                        count = backtrack(row + 1, count)
                    remove_queen(row, col)
            return count

        rows = [0] * n
        hills = [0] * (2 * n - 1)  # "hill" diagonals
        dales = [0] * (2 * n - 1)  # "dale" diagonals
        return backtrack()


class Solution2:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        def backtrack(row=0, hills=0, next_row=0, dales=0, count=0):
            """
            :type row: current row to place the queen
            :type hills: "hill" diagonals occupation [1 = taken, 0 = free]
            :type next_row: free and taken slots for the next row [1 = taken, 0 = free]
            :type dales: "dale" diagonals occupation [1 = taken, 0 = free]
            :rtype: number of all possible solutions
            """
            if row == n:  # if all n queens are already placed
                count += 1  # we found one more solution
            else:
                # free columns in the current row
                # ! 0 and 1 are inversed with respect to hills, next_row and dales
                # [0 = taken, 1 = free]
                free_columns = columns & ~(hills | next_row | dales)

                # while there's still a column to place next queen
                while free_columns:
                    # the first bit '1' in a binary form of free_columns
                    # on this column we will place the current queen
                    curr_column = - free_columns & free_columns

                    # place the queen
                    # and exclude the column where the queen is placed
                    free_columns ^= curr_column

                    count = backtrack(row + 1,
                                      (hills | curr_column) << 1,
                                      next_row | curr_column,
                                      (dales | curr_column) >> 1,
                                      count)
            return count

        # all columns available for this board,
        # i.e. n times '1' in binary representation
        # bin(cols) = 0b1111 for n = 4, bin(cols) = 0b111 for n = 3
        # [1 = available]
        columns = (1 << n) - 1
        return backtrack()


"""
The idea here is quite similar to N-Queens while we don't need to record the path, 
and as the return value is a number not a list, it's better to use a global variable to record the result.
"""
class Solution3:
    def totalNQueens(self, n):
        self.res = 0
        self.dfs([-1] * n, 0)
        return self.res


    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index + 1)


    def valid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[n] - nums[i]) == n - i:
                return False
        return True


class Solution4:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        diag1 = set()
        diag2 = set()
        usedCols = set()

        return self.helper(n, diag1, diag2, usedCols, 0)

    def helper(self, n, diag1, diag2, usedCols, row):
        if row == n:
            return 1

        solutions = 0

        for col in range(n):
            if row + col in diag1 or row - col in diag2 or col in usedCols:
                continue

            diag1.add(row + col)
            diag2.add(row - col)
            usedCols.add(col)

            solutions += self.helper(n, diag1, diag2, usedCols, row + 1)

            diag1.remove(row + col)
            diag2.remove(row - col)
            usedCols.remove(col)

        return solutions


class Solution4:
    def totalNQueens(self, n):
        def dfs(board, row):
            if row == n: return 1
            count = 0
            for x in set_n - set(board):
                # check diagonal conflict
                if all(row - i != abs(x - y) for i, y in enumerate(board[:row])):
                    board[row] = x
                    count += dfs(board, row + 1)
                    board[row] = '.'
            return count

        set_n = {i for i in xrange(n)}
        return dfs(['.'] * n, 0)


class Solution5:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = [-1] * n  # -1: not set
        res = [0]
        self.backtrack(board, 0, res)

        return res[0]

    def backtrack(self, board, row, res):

        if row == len(board):
            res[0] += 1
            return

        for col in range(len(board)):
            board[row] = col

            if self.isValid(board, row, col):
                self.backtrack(board, row + 1, res)
            board[row] = -1

    def isValid(self, board, row, col):

        for prow in range(row):
            pcol = board[prow]
            if pcol == -1 or pcol == col or abs(pcol - col) == abs(prow - row):
                return False

        return True



