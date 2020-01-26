"""
Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""


import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        visited = collections.defaultdict(bool)
        stack = []
        for char in s:
            count[char] -= 1
            if visited[char]:
                continue
            while stack and count[stack[-1]] and stack[-1] > char:
                visited[stack[-1]] = False
                stack.pop()
            visited[char] = True
            stack.append(char)
        return "".join(stack)


class Solution2:
    def removeDuplicateLetters(self, s):
        table = {}
        for i, char in enumerate(s):
            table[char] = i

        res = []
        for i, char in enumerate(s):
            if char not in res:
                while res and char < res[-1] and i < table[res[-1]]:
                    res.pop()
                res.append(char)

        return ''.join(res)



s = "cbacdcbc"
a = Solution2()
print(a.removeDuplicateLetters(s))




