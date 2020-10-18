"""
The intuition is brute force, don't need any tricky.
One thing to pay attention: A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9.
I just find many sumbmission ignoring this condition.

Here I just want share two observatons with this 1-9 condition:

Assume a magic square:
a1,a2,a3
a4,a5,a6
a7,a8,a9

a2 + a5 + a8 = 15
a4 + a5 + a6 = 15
a1 + a5 + a9 = 15
a3 + a5 + a7 = 15

Accumulate all, then we have:
sum(ai) + 3 * a5 = 60
3 * a5 = 15
a5 = 5

The center of magic square must be 5.

Another observation for other 8 numbers:
The even must be in the corner, and the odd must be on the edge.
And it must be in a order like "43816729" （clockwise or anticlockwise)
"""


class Solution:
    def numMagicSquaresInside(self, grid):
        res = 0
        # Construct the 3x3 square
        for i in range(len(grid) - 2):
            for j in range(len(grid) - 2):
                temp = [grid[i + k][j:j + 3] for k in range(3)]
                if self.isMagicSquare(temp):
                    res += 1

        return res

    def isMagicSquare(self, grid):
        # Check the elements
        flat = [num for row in grid for num in row]
        if sorted(flat) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False

        # Check the row, column and diagnal sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum([row[i] for row in grid]) for i in range(3)]
        diag_sums = [sum([grid[i][i] for i in range(3)]), (grid[0][2] + grid[1][1] + grid[2][0])]
        row_sums.extend(col_sums)
        row_sums.extend(diag_sums)
        return len(set(row_sums)) == 1




