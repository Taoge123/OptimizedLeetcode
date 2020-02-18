"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
Note:

board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""

"""
# if the first player wins, the 'X' count number(c1) should be one more than 'O'(c2).
# if the second player wins, the 'X' count number should be equal to 'O'.
# they cannot both win, no need to check. bcoz otherwise c1==c2-1==c2, which is never true.
"""


class Solution:
    def isWin(self, board, char):
        for i in range(3):  # Row check
            if board[i] == char* 3:
                return True
        for i in range(3):  # Column check
            if board[0][i] == char and board[1][i] == char and board[2][i] == char:
                return True
        if board[0][0] == char and board[1][1] == char and board[2][2] == char or \
                board[0][2] == char and board[1][1] == char and board[2][0] == char:  # Diagonal check
            return True
        return False

    def validTicTacToe(self, board):
        countX = countO = 0
        for i in range(3):
            for j in range(3):
                countX += 1 if board[i][j] == 'X' else 0
                countO += 1 if board[i][j] == 'O' else 0
        if countO > countX or countX > countO + 1:
            return False
        if countO == countX and self.isWin(board, 'X') or countX == countO + 1 and self.isWin(board, 'O'):
            return False
        return True



