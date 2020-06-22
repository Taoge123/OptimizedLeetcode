
"""
      j
 0 0 0
 1 1 1
 0 f f

 board[i][j]
 row[i] += player
 row[i] == 0
 row[1] = 3
 if i == j:
     diagonal += 1
 if self.size - 1 - j = i:
     antiDiagonal += 1

"""


class TicTacToe:
    def __init__(self, n):
        self.board = [['X' for i in range(n)] for j in range(n)]
        self.size = n

    def move(self, player, i, j):
        if self.checkFullBoard():
            print('is tie')
            return True
        if self.board[i][j] != 'X':
            return False
        self.board[i][j] = player
        if self.isWinning(player):
            print('player ' + player + 'is winning')
            return True
        print('game continue')


    def isWinning(self, player):
        if [player] * self.size in self.board:
            return True

        count = 1
        for j in range(self.size):
            for i in range(self.size - 1):
                if self.board[i][j] == self.board[i+1][j] == player:
                    count += 1
            if count == self.size:
                return True

        count = 1
        countDiago = 1
        for i in range(self.size - 1):
            if self.board[i][i] == self.board[i+1][i+1]:
                count += 1
            if self.board[i][self.size-1-i] == self.board[i+1][self.size-2-i]:
                countDiago += 1
        if count == self.size or countDiago == self.size:
            return True
        return False

    def checkFullBoard(self):
        return any(col != 'X' for row in self.board for col in row)


