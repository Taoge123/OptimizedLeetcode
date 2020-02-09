

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = ''
        for i, char in enumerate(s):
            if char == '(':
                stack.append(res)
                res = ''
            elif char == ')':
                if stack:
                    res = stack.pop() + '(' + res + ')'
            else:
                res += char

        while stack:
            res = stack.pop() + res

        return res


class SolutionBetter:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = [''] * len(s)

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            #Only if we see ), pair it with left ( with index that stored in stack
            elif char == ')':
                if stack:
                    left = stack.pop()
                    res[left] = s[left]
                    res[i] = char

            else:
                res[i] = char

        return "".join(res)


s = "lee(t(c)o)de)"
a = SolutionBetter()
print(a.minRemoveToMakeValid(s))


