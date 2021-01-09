"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it.
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""


class SolutionRollingHash:
    def shortestPalindrome(self, s: str) -> str:
        base = 26
        aL = 1
        idx = 0
        mod = 10 ** 9 + 7
        hash1, hash2 = 0, 0
        nums = [ord(s[i]) - ord('a') for i in range(len(s))]

        for i in range(len(s)):
            hash1 = (hash1 * base + nums[i]) % mod
            hash2 = (hash2 + nums[i] * aL) % mod
            if (hash1 == hash2):
                idx = i
            aL = aL * base % mod
        return s[idx + 1:][::-1] + s



class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        j, n = 0, len(s)

        for i in reversed(range(n)):
            if s[i] == s[j]:
                j += 1
        part1 = s[::-1][:n-j]
        part2 = s[j-n:]
        rest = s[:j-n]
        print(part1, rest, part2)
        return part1 + self.shortestPalindrome(rest) + part2


class SolutionTLE:
    def shortestPalindrome(self, s: str) -> str:
        i = 0
        j = end = len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                i = 0
                end -= 1
                j = end
        return s[end + 1:][::-1] + s


s = "aacebaaa"
a = Solution()
print(a.shortestPalindrome(s))
