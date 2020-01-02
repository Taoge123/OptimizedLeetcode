"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""
"""
这个题的思路我是参考的Lexicographical Numbers 字典顺序的数字，不太好想。

如果curr乘以10小于等于n，那么下个数字应该是curr末尾补0；
如果curr已经到达了n，那么说明各位数字已经到头了，应该变化十位数字了，所以除以10，再加一。
这时可能会出现恰好进位的情况，而字典序可能是从末尾没有0的数字开始的，所以要把末尾的0去掉。

"""


class Solution:
    def lexicalOrder(self, n: int):

        res = [1]
        while len(res) < n:
            newNum = res[-1] * 10
            while newNum > n:
                newNum //= 10
                newNum += 1
                while newNum % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    newNum //= 10
            res.append(newNum)
        return res

class Solution2:
    def lexicalOrder(self, n: int):

        res = [1]
        for i in range(n-1):
            last = res[-1]
            if last * 10 <= n:
                res.append(last * 10)
            else:
                #Deal with cases like 199 + 1 = 200
                while last + 1 > n or (last + 1) % 10 == 0:
                    last //= 10
                res.append(last + 1)
        return res


class Solution3:
    def lexicalOrder(self, n: int):
        res = []
        for i in range(1, 10):
            self.dfs(i, res, n)
        return res

    def dfs(self, num, res, n):
        if num <= n:
            res.append(num)
            new = num * 10
            if new <= n:
                for i in range(10):
                    self.dfs(new + i, res, n)



n = 200
a = Solution2()
print(a.lexicalOrder(n))



