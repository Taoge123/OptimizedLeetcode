"""

921: # of minimum remove
301: all valid strings by removing minimum # of parentheses
1249: any valid strings by removing minimum # of parenthese

stack : ( ( ) )
greedy:
    count : # of unmatched left parenthesis when count < 0


"""


class SolutionWisdom:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                # 前面没有匹配的(, 就直接改成空
                if not stack:
                    s[i] = ' '
                # 前面有匹配的(, 就直接改pop()
                else:
                    stack.pop()

        # 没有匹配的(也都改成' '
        while stack:
            s[stack.pop()] = ' '

        res = []
        for ch in s:
            if ch != ' ':
                res.append(ch)
        return "".join(res)



class Solution0:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                s[i] = ''
                stack.append(i)

            if char == ')':
                if stack:
                    s[stack.pop()] = '('
                else:
                    s[i] = ''

        return "".join(s)




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


