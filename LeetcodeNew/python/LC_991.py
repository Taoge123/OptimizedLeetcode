
class SolutionLee:
    def brokenCalc(self, X: int, Y: int) -> int:

        res = 0
        while Y > X:
            if Y % 2 == 1:
                Y += 1
                res += 1
            else:
                Y //= 2
                res += 1

        return res + (X - Y)


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            # Base case, also known as stop condition
            return X - Y

        else:
            if Y % 2 == 1:
                # Y is odd
                return 1 + self.brokenCalc(X, Y + 1)
            else:
                # Y is even
                return 1 + self.brokenCalc(X, Y // 2)




