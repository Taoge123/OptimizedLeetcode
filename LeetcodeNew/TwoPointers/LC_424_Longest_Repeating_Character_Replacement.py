
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






