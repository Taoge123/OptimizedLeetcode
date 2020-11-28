

class Solution:
    def queensAttacktheKing(self, queens, king):
        res = []
        queens = {(i, j) for i, j in queens}
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in range(8):
                    x = king[0] + i * k
                    y = king[1] + j * k
                    if (x, y) in queens:
                        res.append([x, y])
                        break

        return res



