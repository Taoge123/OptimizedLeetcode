
"""
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        table = collections.Counter(s)
        for c in table.keys():
            if table[c] < k:
                print(c)
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        maxi = 0
        for char in set(s):
            if s.count(char) < k:
                # return max(self.longestSubstring(z, k) for z in s.split(char))
                for z in s.split(char):
                    maxi = max(maxi, self.longestSubstring(z, k))
                return maxi

        return len(s)


class Solution3:
    def longestSubstring(self, s: str, k: int) -> int:

        stack = []
        stack.append(s)
        res = 0
        while stack:
            s = stack.pop()
            for char in set(s):
                if s.count(char) < k:
                    stack.extend([z for z in s.split(char)])
                    break
            else:
                res = max(res, len(s))
        return res



s = "ababbc"
k = 2

a = Solution3()
print(a.longestSubstring(s, k))



