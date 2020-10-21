"""
用'='将等式分为左右两半

分别求左右两侧x的系数和常数值，记为lx, lc, rx, rc

令x, c = lx - rx, rc - lc

若x != 0，则x = c / x

否则，若c != 0，说明方程无解

否则，说明有无数组解
"""


class Solution:
    def solveEquation(self, equation):
        left, right = equation.split('=')
        lx, lc = self.solve(left)
        rx, rc = self.solve(right)
        x, c = lx - rx, rc - lc
        if x:
            return 'x=%d' % (c / x)
        elif c:
            return 'No solution'
        return 'Infinite solutions'

    def solve(self, expr):
        x = c = 0
        num, sig = '', 1
        for ch in expr + '#':
            if '0' <= ch <= '9':
                num += ch
            elif ch == 'x':
                x += int(num or '1') * sig
                num, sig = '', 1
            else:
                c += int(num or '0') * sig
                num, sig = '', 1
                if ch == '-': sig = -1
        return x, c



class Solution2:
    def solveEquation(self, equation: str) -> str:
        equation += '+'
        num,flag,equation_flag = 0,1,1
        cur = 0
        n = m = 0
        for i, ch in enumerate(equation):
            if ch.isdigit():
                cur = cur * 10 + int(ch)
            elif ch == 'x':
                pre = flag * cur * equation_flag
                m += pre if (pre or equation[i-1]=='0') else equation_flag*flag
                cur  = 0
            elif ch == '+':
                n += flag * cur * equation_flag
                flag = 1
                cur = 0
            elif ch == '-':
                n += flag * cur * equation_flag
                flag = -1
                cur = 0
            elif ch == '=':
                n += flag * cur * equation_flag
                equation_flag = -1
                cur = 0
                flag = 1
        if not m and n:
            return 'No solution'
        elif not m:
            return 'Infinite solutions'
        else:
            return 'x='+str(-n//m)



