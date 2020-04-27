from fractions import Fraction


class Solution:
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

