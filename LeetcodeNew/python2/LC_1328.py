class Solution:
    def breakPalindrome(self, s: str) -> str:

        for i in range(len(s) // 2):
            if s[i] != 'a':
                return s[:i] + 'a' + s[i + 1:]

        return s[:-1] + 'b' if s[:-1] else ''


