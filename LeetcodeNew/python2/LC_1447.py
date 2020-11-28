
class Solution:
    def simplifiedFractions(self, n: int):
        res = []
        for i in range(2, n+ 1):
            for j in range(1, i):
                if self.gcd(j, i) == 1:
                    res.append("%s/%s" % (j, i))
        return res

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)


