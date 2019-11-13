class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        table = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in table:
                stack.append(char)
            elif char in table.values():
                if not stack or table[stack.pop()] != char:
                    return False
        return not stack




