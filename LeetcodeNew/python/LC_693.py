
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = n ^ ( n> >1)
        return (n & n+ 1) == 0


class SolutionTony:
    def hasAlternatingBits(self, n: int) -> bool:
        num = bin(n)[2:]
        for i in range(1, len(num)):
            if num[i] == num[ i -1]:
                return False
        return True



