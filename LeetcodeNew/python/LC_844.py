class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s = self.convert(S)
        t = self.convert(T)
        return s == t

    def convert(self, s):
        stack = []
        for char in s:
            if char != '#':
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        return stack


class SolutionBetter:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, i = self.convert(list(S))
        t, j = self.convert(list(T))
        return s[:i] == t[:j]

    def convert(self, s):
        i = 0
        for j in range(len(s)):
            if s[j] != '#':
                s[i] = s[j]
                i += 1
            else:
                i = max(0, i - 1)
        return s, i



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






