
class Solution:
    def isArmstrong(self, N: int) -> bool:
        num = str(N)
        n = len(num)
        i = 0
        summ = 0
        while i < n:
            summ += int(num[i]) ** n
            i += 1
        return summ == N





