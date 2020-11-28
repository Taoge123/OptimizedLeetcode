

class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:

        if M == 2:
            if Y % 4:
                return 28
            if Y % 4 == 0 and Y % 100:
                return 29
            if Y % 100 == 0 and Y % 400:
                return 28
            if Y % 400 == 0:
                return 29

        if M in [4, 6, 9, 11]:
            return 30

        return 31



