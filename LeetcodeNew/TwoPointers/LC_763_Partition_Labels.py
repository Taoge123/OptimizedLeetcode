
"""
A string S of lowercase letters is given. We want to partition this string
into as many parts as possible so that each letter appears in at most one part,
and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

"""

class Solution1:
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans

"""
首先用字典存储char出现最后的下标。空间换时间，用来避免O(N^2)的时间复杂。
在每次迭代的时候更新r的区间，在这里i作为我们的runner，l则保持在左区间的位置。
直到当i和r相等的时候，得到最长区间r-l+1并加入到数组。
"""


class Solution2:
    def partitionLabels(self, s):
        dic = {}
        for i, char in enumerate(s):
            dic[char] = i

        res = []
        l, r = 0, 0
        for i, char in enumerate(s):
            r = max(r, dic[char])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
        return res





