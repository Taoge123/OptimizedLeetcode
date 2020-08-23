"""
(ed(et(oc))el)
(ed(etoc)el)
(ed cote el)
leetcode


"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        cur = []

        for char in s:
            if char == "(":
                stack.append(cur)
                cur = []
            elif char == ")":
                cur = cur[::-1]
                cur = stack.pop() + cur
            else:
                cur.append(char)

        return "".join(cur)



