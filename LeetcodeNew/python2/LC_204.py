
class Solution:
    def countPrimes(self, n):

        if n<= 2:
            return 0

        ans = [True] * n
        ans[0] = ans[1] = False

        for i in range(2, n):
            if ans[i] == True:
                for j in range(2, (n - 1) // i + 1):
                    ans[i * j] = False

        return sum(ans)


