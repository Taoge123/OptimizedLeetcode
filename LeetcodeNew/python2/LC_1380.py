
class Solution:
    def luckyNumbers (self, matrix):
        mi = [min(row) for row in matrix]
        mx = [max(col) for col in zip(*matrix)]
        return [cell for i, row in enumerate(matrix) for j, cell in enumerate(row) if mi[i] == mx[j]]


class SolutionTony:
    def luckyNumbers(self, matrix):
        table = []
        for i, row in enumerate(matrix):
            val = min(row)
            index = row.index(val)
            table.append([val, index])

        res = []
        for val, index in table:
            if val == max([row[index] for row in matrix]):
                res.append(val)

        return res




