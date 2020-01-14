
"""
Given a positive integer n, find the number of non-negative integers less than or equal to n,
whose binary representations do NOT contain consecutive ones.

Example 1:
Input: 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
Note: 1 <= n <= 109

"""


class SolutionTLE:
    def findIntegers(self, num: int) -> int:
        table = []
        res = 0
        for i in range(num + 1):
            temp = bin(i)[2:]
            if temp.count("11") < 1:
                res += 1
        return res




class Solution:
    def findIntegers(self, num: int) -> int:
        sb = bin(num)[2:][::-1]
        n = len(sb)
        a, b = [0] * n, [0] * n
        a[0] = b[0] = 1
        for i in range(1, n):
            a[i] = a[i -1] + b[i -1]
            b[i] = a[i -1]

        res = a[n -1] + b[n -1]

        for i in range(n -2, -1, -1):
            if sb[i] == '1' and sb[i +1] == '1':
                break
            if sb[i] == '0' and sb[i +1] == '0':
                res -= b[i]

        return res





class Solution2:
    def findIntegers(self, num: int) -> int:

        fn = [0] * 32
        fn[0], fn[1] = 1, 2

        for i in range(2, len(fn)):
            fn[i] = fn[i - 1] + fn[i - 2]

        binChr = list(bin(num)[2:])
        n = len(binChr) - 1
        res = 0
        preBit = False

        for i in range(len(binChr)):
            if binChr[i] == '1':
                res += fn[n - i]
                if preBit:
                    return res
                preBit = True
            else:
                preBit = False

        return res + 1












