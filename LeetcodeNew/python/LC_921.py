"""
stack : (**)
greedy: count -> the number of unmatched left parenthesis

s = (()))((

((....    count = 2
(()...    count = 1
(())...   count = 0
*(()))... count = -1 => count = 0 + left
(()))(... count = 1
(()))((   count = 2 => count = 0 +2 right


"""


class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        count = 0
        res = 0
        for ch in S:
            if ch == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                res += 1
                count = 0
        return res + count



