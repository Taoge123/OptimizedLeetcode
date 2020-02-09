
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a = self.process(S, [])
        b = self.process(T, [])
        return a == b

    def process(self, s, stack):
        for char in s:
            if char is not '#':
                stack.append(char)
            else:
                if not stack:
                    continue
                stack.pop()

        return stack


class SolutionLeeON:
    def backspaceCompare(self, S, T):
        i, j = len(S) - 1, len(T) - 1
        backS = backT = 0
        while True:
            while i >= 0 and (backS or S[i] == '#'):
                backS += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (backT or T[j] == '#'):
                backT += 1 if T[j] == '#' else -1
                j -= 1
            if not (i >= 0 and j >= 0 and S[i] == T[j]):
                return i == j == -1
            i, j = i - 1, j - 1






