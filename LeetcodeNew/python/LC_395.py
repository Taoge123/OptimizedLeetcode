
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

"""

the sliding window must contain m different characters
[X X X X X a a a b] X X X X
O(26N)

"""


class SolutionTony:
    def longestSubstring(self, s: str, k: int) -> int:

        res = 0
        for m in range(1, 27):
            res = max(res, self.helper(s, m, k))

        return res

    def helper(self, s, m, k):
        right = 0
        count = 0
        table = collections.Counter()
        res = 0

        for left in range(len(s)):
            while right < len(s) and len(table) <= m:
                table[s[right]] += 1
                if table[s[right]] == k:
                    count += 1
                right += 1

                if len(table) == m and count == m:
                    res = max(res, right - left)

            table[s[left]] -= 1
            if table[s[left]] == k - 1:
                count -= 1
            if table[s[left]] == 0:
                del table[s[left]]

        return res




class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        count = collections.Counter(s)
        res = 0
        for ch in set(s):
            if count[ch] < k:
                # return max(self.longestSubstring(z, k) for z in s.split(char))
                for subS in s.split(ch):
                    res = max(res, self.longestSubstring(subS, k))
                return res

        return len(s)



class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:
        table = collections.Counter(s)
        for c in table.keys():
            if table[c] < k:
                print(c)
                return max(self.longestSubstring(t, k) for t in s.split(c))
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



