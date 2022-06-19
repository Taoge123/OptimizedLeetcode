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
"""
1081. Smallest Subsequence of Distinct Characters

总体思想是贪心法，用stack做辅助。基本方法仍然是用手头的字符尽量维持一个递增字符序列，因为递增序列意味着字典序最小。

首先，在维护栈的过程中，遇到已经用过的字符就跳过。比如当前待处理的字符是c，而当前的栈已经有c了，意味着什么呢？
因为栈在维护着一个递增序列，说明c后面的字符要比c大。如果舍弃已经用过的c，那么必将导致后续的大字符前移，使得构建的栈内的单词字典序会变小。

接下来，如果遇到非递增的字符，则大致方向就是退栈--处理掉一些栈顶元素，使得新加入的仍能保持递增。
但需要注意，如果待退栈处理的字符在后面还有出现的机会，就放心退栈，扔到后面去考虑；如果后面已经没有再出现的机会，
则保留这个栈顶元素同时结束退栈。所以需要一个Hash表来实时记录每个字符剩下来还会出现几次，也就是说每遍历一个字符，就把Map[s[i]]--.

本题和1081. Smallest Subsequence of Distinct Characters一模一样。
"""


import collections


class SolutionTony:
    def smallestSubsequence(self, s: str) -> str:
        last = collections.defaultdict(int)
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        for i, ch in enumerate(s):
            if ch in stack:
                continue
            # identical to 316, only difference is to make sure the ch we delete will show up again (i < last[stack[-1]])
            while stack and stack[-1] > ch and i < last[stack[-1]]:
                stack.pop()
            stack.append(ch)
        return "".join(stack)


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



s = "cbacdcbc"
a = SolutionTony()
print(a.removeDuplicateLetters(s))




