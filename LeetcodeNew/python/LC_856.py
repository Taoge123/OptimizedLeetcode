
class Solution:
    def scoreOfParentheses(self, S: str) -> int:

        stack = []
        cur = 0
        for char in S:
            if char == ')':
                if cur != 0:
                    cur *= 2
                else:
                    cur = 1
                cur += stack.pop()
            else:
                stack.append(cur)
                cur = 0
        return cur




