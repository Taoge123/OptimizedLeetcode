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


class SolutionDFS:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)

        def dfs(i, j):
            if i > j:
                return 0

            if i == j:
                return 1

            res = 1
            for k in range(1, (j - i + 1) // 2 + 1):
                if text[i:i + k] == text[j - k + 1:j + 1]:
                    res = max(res, dfs(i + k, j - k) + 2)
                    break
            return res

        return dfs(0, n - 1)




class SolutionDFSRollingHash:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        base = 26
        nums = [ord(text[i]) - ord('a') for i in range(n)]
        mod = 10 ** 9 + 7

        def dfs(i, j):
            if i >= j:
                return 0

            prefix, suffix = 0, 0
            aL = 1
            for k in range((j - i) // 2):
                prefix = (prefix + nums[i + k] * aL) % mod
                suffix = (suffix * base + nums[j - k - 1]) % mod
                aL = (aL * base) % mod
                if prefix == suffix:
                    if text[i:i + k + 1] == text[j - k - 1:j]:
                        return dfs(i + k + 1, j - k - 1) + 2
            return 1

        return dfs(0, n)



class SolutionSlicing:
    def longestDecomposition(self, text: str) -> int:
        if not text:
            return 0

        res = 1
        for i in range(1, len(text) // 2 + 1):
            if text[:i] == text[-i:]:
                res = 2 + self.longestDecomposition(text[i: -i])
                break
        return res


