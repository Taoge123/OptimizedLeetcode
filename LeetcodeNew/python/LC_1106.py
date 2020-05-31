
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        return self.parse(expression, 0)[0]

    def parse(self, exp, i):
        if exp[i] == 't':
            return True, i+ 1
        if exp[i] == 'f':
            return False, i + 1
        if exp[i] == '!':
            child, i = self.parse(exp, i + 2)
            return not child, i + 1
        if exp[i] == '&':
            i += 1  # "("
            true = True
            while exp[i] != ")":
                child, i = self.parse(exp, i + 1)
                true &= child
            return true, i + 1
        if exp[i] == '|':
            i += 1  # "("
            true = False
            while exp[i] != ")":
                child, i = self.parse(exp, i + 1)
                true |= child
            return true, i + 1


