
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        i, j = r0, c0
        res = [[r0, c0]]
        size = 1
        sign = 1

        while len(res) < R * C:
            for _ in range(size):
                j += sign
                if i < R and j < C and i>= 0 and j >= 0:
                    res.append([i, j])

            for _ in range(size):
                i += sign
                if i < R and j < C and i >= 0 and j >= 0:
                    res.append([i, j])

            size += 1
            sign *= -1

        return res


class Solution2:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):

        res = [[r0, c0]]
        count = 0
        index = 0
        i, j = r0, c0

        dire = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while len(res) < R * C:
            steps = count // 2 + 1
            for step in range(steps):
                i += dire[index][0]
                j += dire[index][1]
                if 0 <= i <= R - 1 and 0 <= j <= C - 1:
                    res.append([i, j])
            count += 1
            index = (index + 1) % 4

        return res



