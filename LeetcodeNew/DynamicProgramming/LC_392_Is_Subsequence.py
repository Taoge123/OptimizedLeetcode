
"""
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string
by deleting some (can be none) of the characters without disturbing
the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.
"""

"""
The first solution is to use two pointers, which is easy to understand and posted by others:
"""
import collections

class Solution1:
    def isSubsequence(self, s, t):
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]: i += 1
            j += 1
        return True if i == len(s) else False


"""
The running time is 356 ms with complexity of O(m+n), in which m is length of s and n is length of t.

For the follow-up question, however, this solution is not efficient as we need to compare s with t every time. 
For example, if we have k=1B, len(s) = 100, len(t)=500,000, the total complexity will be O(10^9*(100+500,000)). 
So the tricky is we don't want to scan t every time as it costs too much.

Here is solution 2, check comments for a brief explanation. The idea is to scan t once and save the index (as a sorted list) of each letter.

The running time is 525 ms. Although this one-time run cost of solution 2 is bigger than solution 1, 
if we have many s, we can save a lot of time by avoid comparing s with t every time.
"""

"""
解题思路：
利用队列（Queue）数据结构。

将s加入队列，遍历t，当t的当前字符c与队头相同时，将队头弹出。

最后判断队列是否为空即可

解题方法
其实这个题就考了一个相对顺序。s比较短，而t很长，那么尽量就对t进行一次遍历最好。可以使用一个队列保留s的每个元素，
这样对t进行遍历，如果遍历到的元素和队列的头元素相等，那么队列出头元素。这样最后返回队列是否为空即可。
"""

class Solution2:
    def isSubsequence(self, s, t):

        queue = collections.deque(s)
        for c in t:
            if not queue: return True
            if c == queue[0]:
                queue.popleft()
        return not queue


"""
如果不使用队列的话，可以使用两个指针，一个作为s的索引，一个作为t的索引。
如果在t中找到了s的元素，把s的指针右移，否则把t的指针右移。
"""
class Solution3:
    def isSubsequence(self, s, t):

        si, ti = 0, 0
        while si < len(s) and ti < len(t):
            if t[ti] == s[si]:
                si += 1
            ti += 1
        return si == len(s)




