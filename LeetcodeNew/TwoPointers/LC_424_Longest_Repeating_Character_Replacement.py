
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
import collections
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
class Solution111:
    def characterReplacement(self, s, k):

        count = collections.Counter()
        res = 0
        start = 0
        for i, char in enumerate(s):
            count[char] += 1
            maxCnt = count.most_common(1)[0][1]
            while i - start + 1 - maxCnt > k:
                count[s[start]] = count[s[start]] - 1
                start += 1
            res = max(res, i - start + 1)
        return res


class Solution11:
    def characterReplacement(self, s, k):
        count = {}
        max_count = start = result = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            max_count = max(max_count, count[s[end]])
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result

class Solution2:
    def characterReplacement(self, s, k):
        count = collections.Counter()
        start = result = 0
        for end in range(len(s)):
            count[s[end]] += 1
            max_count = count.most_common(1)[0][1]
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result


class Solution:
    def characterReplacement(self, s, k):
        dic, lo, ret = collections.defaultdict(int), 0, 0
        for hi,c in enumerate(s):
            dic[c] += 1
            while lo<hi and hi-lo+1-max(dic.values())>k:
                dic[s[lo]] -= 1
                lo += 1
            ret = max(ret, hi-lo+1)
        return ret

"""
Re: [Sliding window](similar to finding longest substring with k distinct characters)

Similar idea in Python but allowing any character, not just uppercase English letters [Updated based on comments below]:
"""

class Solution2:
    def characterReplacement(self, s, k):
        res = lo = hi = 0
        counts = collections.Counter()
        for hi in range(1, len(s) + 1):
            counts[s[hi - 1]] += 1
            max_char_n = counts.most_common(1)[0][1]
            if hi - lo - max_char_n > k:
                counts[s[lo]] -= 1
                lo += 1
        return hi - lo

# [Original code in order to understand comment from @StefanPochmann was:]
class Solution3:
    def characterReplacement(self, s, k):
        res = lo = 0
        counts = collections.Counter()
        for hi in range(len(s)):
            counts[s[hi]] += 1
            max_char_n = counts.most_common(1)[0][1]
            while (hi - lo - max_char_n + 1 > k):
                counts[s[lo]] -= 1
                lo += 1
            res = max(res, hi - lo + 1)
        return res

class Solution4:
    def characterReplacement(self, s, k):
        count = collections.defaultdict(int)
        maxLen = 0
        left = 0
        for i, num in enumerate(s):
            count[num] += 1
            while i - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, i - left + 1)

        return maxLen

"""
a readable python solution according to the
p0 is the start point,maxs is our solution, maxcount record the most frequency character.
"""
class Solution5:
    def characterReplacement(self, s, k):
        dic = {}
        p0, maxs, maxcount = 0, 0, 0
        for p1 in range(len(s)):
            dic[s[p1]] = dic.get(s[p1], 0) + 1
            if maxcount < dic[s[p1]]:
                maxcount = dic[s[p1]]
            while p1 - p0 - maxcount + 1 > k:
                dic[s[p0]] -= 1
                p0 += 1
            maxs = max(maxs, p1 - p0 + 1)
        return maxs






