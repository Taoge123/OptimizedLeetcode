"""
(ed(et(oc))el)
(ed(etoc)el)
(ed cote el)
leetcode


"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = []

        for char in s:
            if char == "(":
                stack.append(res)
                res = []
            elif char == ")":
                res = res[::-1]
                res = stack.pop() + res
            else:
                res.append(char)

        return "".join(res)


class SolutionWisdom:
    def reverseParentheses(self, s: str) -> str:
        res = []
        stack = []

        for char in s:
            if char.isalpha():
                res.append(char)
            elif char == "(":
                stack.append(len(res))
            else:
                i = stack.pop()
                res[i:] = res[i:][::-1]

        return "".join(res)


"""
abc(def(ghi)k)

abc k ghi fed
1. enter a parenthesis pair: -> (   ,   ) <- 
   goto the opposite one, flip the direction

2. exit a parenthesis pair: -> )
   goto the opposite one, flip the direction


"""


class SolutionON:
    def reverseParentheses(self, s: str) -> str:
        res = []
        stack = []
        n = len(s)
        pairs = [-1] * n

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pairs[i] = j
                pairs[j] = i

        i = 0
        direction = 1
        while i < n:
            if s[i].isalpha():
                res.append(s[i])
            else:
                i = pairs[i]
                direction = -direction
            i += direction
        return "".join(res)

