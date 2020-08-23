"""
Iddentical to 316

"""

import collections

class Solution:
    def smallestSubsequence(self, s: str) -> str:
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




