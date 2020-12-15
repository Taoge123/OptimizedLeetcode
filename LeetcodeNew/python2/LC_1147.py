"""
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/discuss/351387/Java-Simple-Memo-Top-Down-DP
https://leetcode.com/problems/longest-chunked-palindrome-decomposition/discuss/350560/JavaC%2B%2BPython-Easy-Greedy-with-Prove
"""

class Solution:
    def longestDecomposition(self, text: str) -> int:

        res = 0
        left, right = "", ""
        for i, j in zip(text, text[::-1]):
            left = left + i
            right = j + right
            if left == right:
                res += 1
                left, right = "", ""
        return res



class Solution2:
    def longestDecomposition(self, text: str) -> int:
        if not text:
            return 0

        res = 1
        for i in range(1, len(text) // 2 + 1):
            if text[:i] == text[-i:]:
                res = 2 + self.longestDecomposition(text[i: -i])
                break
        return res


