

"""

Example 1:

Input: "T?2:3"

Output: "2"

Explanation: If true, then result is 2; otherwise result is 3.
Example 2:

Input: "F?1:T?4:5"

Output: "4"

Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
          -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
          -> "4"                                    -> "4"
Example 3:

Input: "T?T?F:5:3"

Output: "F"

Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:

             "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
          -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
          -> "F"                                    -> "F"



Iterate the expression from tail,
whenever encounter a character before '?',
calculate the right value and push back to stack.

P.S. this code is guaranteed only if "the given expression is valid"
base on the requirement.
"""


class Solution:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = list()

        for c in reversed(expression):
            if stack and stack[-1] == "?":
                stack.pop()
                first = stack.pop()
                stack.pop()
                second = stack.pop()
                if c == "T":
                    stack.append(first)
                else:
                    stack.append(second)

            else:
                stack.append(c)
        return stack[0]



class Solution2:
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        stack = []
        d = {}
        for i in range(0, len(expression)):
            if expression[i] == "?":
                stack.append(("?", i))
            elif expression[i] == ":":
                _, pos = stack.pop()
                d[pos] = i

        def dfs(expr, start, end, d):
            if end - start + 1 < 5:
                return expr[start:end+1]
            iSep = d[start + 1]
            stmt = expr[start]
            return dfs(expr, start + 2, iSep - 1, d) if stmt == "T" else dfs(expr, iSep + 1, end, d)
        return dfs(expression, 0, len(expression), d)


class Solution3:
    def parseTernary(self, s):
        stack = list(s)[::-1]

        def helper():
            if len(stack) == 1: return stack[0]
            n = stack.pop()
            op = stack.pop()
            if op == ':': return n
            a = helper()
            b = helper()
            return a if n == 'T' else b

        return helper()

# The expression can be expressed as a binary tree, with condition as the parent, value1 and value2 as the two leaves, going deep.
# The tree is special-- parent either have two full children or none. The correct way to evaluate the expression is bottom-up, which corresponding to scanning from right to left.
# We should scan from right to left to look for the first '?', that indicates the lowest parent and do the calculation if possible.
class Solution3:
    def parseTernary(self, expression):
        # T?2:3
        for i in range(len(expression) - 1, 0, -1):  # Let i starts with the last char and ends at the 2nd char
            if expression[i] == '?':
                v1 = expression[i + 1]
                v2 = expression[i + 3]
                cond = expression[i - 1]
                res = v1 if cond == 'T' else v2  # Python's Ternary Operator
                expression = expression[0:i - 1] + res + expression[i + 4:]

        return expression


