"""

1541 Minimum Insertions to Balance a Parentheses String
1249 Minimum Remove to Make Valid Parentheses
1111 Maximum Nesting Depth of Two Valid Parentheses Strings
1190 Reverse Substrings Between Each Pair of Parentheses
1021 Remove Outermost Parentheses
921 Minimum Add to Make Parentheses Valid
856 Score of Parentheses

"""


class Solution:
    def maxDepth(self, s: str) -> int:
        cur = 0
        res = 0
        for ch in s:
            if ch == '(':
                cur += 1
                res = max(res, cur)
            if ch == ')':
                cur -= 1
        return res





