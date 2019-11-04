
"""
Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""
"""
The problem says that we can make at most k changes to the string 
(any character can be replaced with any other character). 
So, let's say there were no constraints like the k. 
Given a string convert it to a string with all same characters with minimal changes. 
The answer to this is

length of the entire string - number of times of the maximum occurring character in the string

Given this, we can apply the at most k changes constraint and maintain a sliding window such that

(length of substring - number of times of the maximum occurring character in the substring) <= k
"""

"""
字符串牵扯到个数的问题，一般是想到用字典去做。对于这个题，我们使用变长的滑动窗口去做。我们刚开始从0个字符开始，
把start作为滑动窗口的左边界，依次遍历字符串的每个字符作为窗口的右边界。统计该窗口内出现最多的字符出现了多少次。
我们把窗口的长度减去出现最多的字符出现的次数，那么就是最少需要修改多少个字符才能把该滑动窗口变为相同的字符。
如果差值大于k，说明我们要修改的字符数多于k，不满足条件，那么把窗口的左边界向右移动到满足该条件为止，
移动的同时把因为左边界移动导致的字符离开窗口数-1。我们用res保存最大的滑动窗口长度。
"""
"""
这道题给我们了一个字符串，说我们有k次随意置换任意字符的机会，让我们找出最长的重复字符的字符串。
这道题跟之前那道Longest Substring with At Most K Distinct Characters很像，都需要用滑动窗口Sliding Window来解。
我们首先来想，如果没有k的限制，让我们求把字符串变成只有一个字符重复的字符串需要的最小置换次数，
那么就是字符串的总长度减去出现次数最多的字符的个数。如果加上k的限制，
我们其实就是求满足(子字符串的长度减去出现次数最多的字符个数)<=k的最大子字符串长度即可，搞清了这一点，
我们也就应该知道怎么用滑动窗口来解了吧我们用一个变量start记录滑动窗口左边界，初始化为0，然后我们遍历字符串，
每次累加出现字符的个数，然后更新出现最多字符的个数，然后我们判断当前滑动窗口是否满足之前说的那个条件，如果不满足，
我们就把滑动窗口左边界向右移动一个，并注意去掉的字符要在counts里减一，直到满足条件，我们更新结果res即可
"""


"""
Re: [Sliding window](similar to finding longest substring with k distinct characters)

Similar idea in Python but allowing any character, not just uppercase English letters [Updated based on comments below]:
"""


"""
a readable python solution according to the
p0 is the start point,maxs is our solution, maxcount record the most frequency character.
"""

import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        start, maxi, res = 0, 0, 0
        count = collections.Counter()

        for i in range(len(s)):
            count[s[i]] += 1
            maxi = max(maxi, count[s[i]])
            while i - start + 1 - maxi > k:
                count[s[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res






