"""
K = 3
N = 1, 4

r = 1 % 3 = 1
r = 11 % 3 = 2
r = 21 % 3 = 0

"""


class Solution:
    def smallestRepunitDivByK(self, K):
        if K % 2 == 0 or K % 5 == 0:
            return -1
        r = 0
        for N in range(1, K + 1):
            r = (r * 10 + 1) % K
            if r == 0:
                return N


"""
x1 = k*q + r
x2 = 10*1+1 = k*10q + 10r = 10r1 + 1 (mod K)
x3 = 10*2+1 = 10r2 + 1 (mod K)


"""


class SolutionWisdom:
    def smallestRepunitDivByK(self, K: int) -> int:
        N = 1
        count = 1
        visited = set()
        while True:
            remain = N % K
            if remain == 0:
                return count
            if remain in visited:
                return -1
            visited.add(remain)
            N = N % K * 10 + 1
            count += 1
        return -1





