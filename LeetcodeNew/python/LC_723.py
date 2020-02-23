
class Solution:
    def candyCrush(self, board):
        m, n = len(board), len(board[0])
        while True:
            crush = set()
            #marker all candies needed to crush
            for i in range(m):
                for j in range(n):
                    if j >= 2 and board[i][j] and board[i][j] == board[i][ j -1] == board[i][ j -2]:
                        crush |= {(i, j), (i, j- 1), (i, j - 2)}
                    if i >= 2 and board[i][j] and board[i][j] == board[i - 1][j] == board[i - 2][j]:
                        crush |= {(i, j), (i - 1, j), (i - 2, j)}

            if not crush:
                break

            #set all crushed value to 0
            for i, j in crush:
                board[i][j] = 0

            #drop all the values
            for j in range(n):
                index = m - 1
                #whenever we have values from bottom to up, drop all the way down
                for i in reversed(range(m)):
                    if board[i][j]:
                        board[index][j] = board[i][j]
                        index -= 1
                #set the rest of the values above as 0, then we are done
                for i in range(index + 1):
                    board[i][j] = 0
        return board


"""
1 2 3
1 3 2
0 0 1
0 0 0
will become 

0 0 0
0 0 3
1 2 2
1 3 1

"""



