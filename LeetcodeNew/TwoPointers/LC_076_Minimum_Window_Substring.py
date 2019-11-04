
"""

https://leetcode.com/problems/minimum-window-substring/solution/



Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


"""
Basically I kept a dictionary to record the index of each character of T. 
Each time I found a window, (when miss == []), I checked the length of this window 
by subtracting the maximum index and the minimum index of the characters. 
If this window is the smallest one so far, I record its beginning and ending index as "start" and "end."
"""


"""
解题方法
统计字符出现的个数，而且时间复杂度要求O(N)，明显使用双指针解题。和567. Permutation in String有点相似，都是要求子字符串满足一定的次数要求。

使用right指针向右搜索，同时要记录在left～right这个区间内包含的T中每个元素出现的个数和。如果在[left,right]区间内，
元素出现的个数和与T长度相等了，说明在这个区间是符合要求的一个区间，但是不一定是最短区间。

因此，现在要移动left指针，要求，在[left, right]区间内的元素出现个数应该把T中所有的元素都包含。
同样使用cnt来验证是否包含了T所有的元素。cnt的含义是在s[left, right]区间内，和t的相等的字符个数统计。
cnt是个很重要的变量，它是来维护左右指针的参考。

在移动left指针的时候要注意存储最短的子串，当所有的循环都结束之后最短字符串即为题目要求了。
使用的minLen变量即当前满足题目要求的最短子串长度，要返回的结果res根据minLen和当前的满足题目要求的子串长度进行比较从而更新。

这个题难点就在于维护cnt，其实如果使用普通的求T的元素个数是不是S[left, right]的元素子集的方法应该更容易理解，
但是不知道能不能通过OJ。这个思路比较重要，其他都还好。

时间复杂度是O(N)，空间复杂度是O(N)。
"""

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res = ""
        left = 0
        minLen = float('inf')
        total = 0
        count = collections.Counter(t)

        for i, char in enumerate(s):
            count[char] -= 1
            if count[char] >= 0:
                total += 1
            while total == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left: i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    total -= 1
                left += 1
        return res




