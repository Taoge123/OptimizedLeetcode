"""
Identical -> 1012. Numbers With Repeated Digits

"""


class Solution:
    def countSpecialNumbers(self, N: int) -> int:
        self.count = 0
        num = list(str(N))
        num = [int(i) for i in num]
        n = len(num)
        # 先算出所有n-1位的permutation
        for k in range(1, n):
            # print(k, n - (k + 1), self.perm(9, n - (k + 1)))
            #第一位数必须是9(1-9, 0不能选), 因为用了一位了， 后面就是9位选一位
            self.count += 9 * self.perm(9, n - (k + 1))

        digits = [False for i in range(10)]
        # 0代表最高位
        self.dfs(num, digits, 0)
        return self.count

    def dfs(self, num, digits, k):
        n = len(num)
        if k == n:
            self.count += 1
            return

        for i in range(10):
            # 最高位不能是0
            if k == 0 and i == 0:
                continue
            # 被占用了就不考虑了
            if digits[i] == True:
                continue

            #<num[i], 可以全排列
            if i < num[k]:
                # (k+1)代表已经用过多少数字了, 要减掉
                self.count += self.perm(10 - (k + 1), n - (k + 1))
            #==num[i], 继续往前走
            elif i == num[k]:
                digits[i] = True
                self.dfs(num, digits, k + 1)
                digits[i] = False

    def perm(self, m, n):
        res = 1
        for i in range(n):
            res *= (m - i)
        return res



