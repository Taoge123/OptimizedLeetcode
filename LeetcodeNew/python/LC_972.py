"""
提示：

每个部分仅由数字组成。
整数部分 <IntegerPart> 不会以 2 个或更多的零开头。（对每个部分的数字没有其他限制）。
1 <= <IntegerPart>.length <= 4
0 <= <NonRepeatingPart>.length <= 4
1 <= <RepeatingPart>.length <= 4
思路分析：
其他语言我不太清楚，但是在python中，浮点数的比较是不准确的。这是因为浮点数在计算机中保存的精度问题导致的。
下面是我在cmd里敲的几个例子，可以看到在浮点数除法(1/6)中显示出来的结果保存 小数点后17位

>>> 1 / 6
0.16666666666666666(17位)
>>> 0.16666666666666666 == 1 / 6 (手动判断17位是否相等)
True
>>> 0.166666666666666666 == 1 / 6(手动判断18位是否相等)
True
>>> 0.166666666666666669 == 1 / 6(手动判断18位是否相等，后面补个9)
True
>>> 0.1666666666666666666 == 1 / 6(手动判断19位是否相等)
True
>>> 0.1666666666666666 == 1 / 6 (手动判断16位是否相等)
False
严格来说，这里面的任何一个case都应该是false，因为 1/6 是无限循环小数，要大于上面输入的任何一个数(除去case3)，但由于浮点数自身的特点，当小数位大于17位的时候，他会自动判定为相等

那么这道题就很简单了，对于循环小数，我们只要将小数点位数循环到17位以上，就相当于获得了这个数的"真值"

"""

class Solution:
    def isRationalEqual(self, S, T):
        def traverse(s):
            if '(' not in s:
                return float(s)
            index = s.index('(')
            s = s[:index] + s[index+1:-1] * 17
            return float(s)
        return traverse(S) == traverse(T)



from fractions import Fraction


class Solution2:
    def isRationalEqual(self, S, T):
        return self.convert(S) == self.convert(T)

    def convert(self, S):
        if '.' not in S:
            return Fraction(int(S), 1)
        i = S.index('.')
        res = Fraction(int(S[:i]), 1)
        S = S[i + 1:]
        if '(' not in S:
            if S:
                res += Fraction(int(S), 10 ** len(S))
            return res

        i = S.index('(')
        if i:
            res += Fraction(int(S[:i]), 10 ** i)
        S = S[i + 1:-1]
        j = len(S)
        res += Fraction(int(S), 10 ** i * (10 ** j - 1))
        return res


class SolutionLee:
    def isRationalEqual(self, S, T):
        def f(s):
            i = s.find('(')
            if i >= 0:
                s = s[:i] + s[i + 1:-1] * 20
            return float(s[:20])
        return f(S) == f(T)

