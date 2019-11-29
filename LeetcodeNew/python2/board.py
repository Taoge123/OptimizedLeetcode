
class Game:
    def __init__(self):
        self.board = [['-'] * 3 for i in range(3)]

    def add(self, i, j, player):
        #need to come back
        if player == 'A':
            self.board[i][j] = 'X'
        elif player == 'B':
            self.board[i][j] = 'O'

    def findEmpty(self):
        try:
            for i, row in enumerate(self.board):
                for j, col in enumerate(row):
                    if self.board[i][j] == '-':
                        return [i, j]
        except:
            print('not more empty spot exist')

    def checkFull(self):
        for row in self.board:
            for col in row:
                if col == '-':
                    return False
        return True

    def aiMove(self):
        try:
            spot = self.findEmpty()
            self.board[spot[0]][spot[1]] = 'O'
        except:
            print("ai can not move due to nomore spot")

    def printBoard(self):
        for row in self.board:
            temp = ""
            for i, col in enumerate(row):
                if i == 0:
                    temp += col
                else:
                    temp += "|%s"%col
            print(temp)


a = Game()
# a.add(0,0,'A')
# a.add(0,1,'B')
# a.add(0,2,'A')
# a.add(1,0,'A')
# a.add(1,1,'B')
# a.add(1,2,'A')
# a.add(2,0,'A')
# a.add(2,1,'B')
# a.add(2,2,'A')
# a.aiMove()
# a.aiMove()
# a.printBoard()
while True:
    a.aiMove()
    a.printBoard()
    print(a.checkFull())







