
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        self.mod = 10 ** 9 + 7
        count = 0
        for i in range(2, n+ 1):
            flag = 1
            j = 2
            while j * j <= i:
                if i % j == 0:
                    flag = 0
                    break
                j += 1
            if flag:
                count += 1

        return self.perm(count) * self.perm(n - count) % self.mod

    def perm(self, num):
        res = 1
        for i in range(1, num + 1):
            res = res * i % self.mod
        return res





