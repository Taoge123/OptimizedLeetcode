"""
xxxxxx xxxxxxx xxxxxx
yyyyyy yyyyyyy yyyyyy


"""


class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.check(a, b) or self.check(b, a)

    def check(self, a: str, b: str) -> bool:
        i = 0
        j = len(b) - 1

        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        if i >= j:
            return True
        return self.isPal(a[i:j + 1]) or self.isPal(b[i:j + 1])

    def isPal(self, s):
        return s == s[::-1]



class SolutionTonyError:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        if len(a) == 1:
            return True
        return self.check(a, b, 0, len(b) - 1) or self.check(b, a, 0, len(a) - 1)

    def check(self, a, b, i, j):
        if i >= j:
            return True
        if a[i] != b[j] and a[i] != a[j] and b[i] != b[j]:
            return False
        else:
            return self.check(a, b, i + 1, j - 1)


