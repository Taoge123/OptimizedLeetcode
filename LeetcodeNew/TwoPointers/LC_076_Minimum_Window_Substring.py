
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
import collections

class Solution1:
    def minWindow(self, s, t):


        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = collections.Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

            # Keep expanding the window once we are done contracting.
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]




class Solution2:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        dict_t = collections.Counter(t)

        required = len(dict_t)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1

            r += 1
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


"""
Basically I kept a dictionary to record the index of each character of T. 
Each time I found a window, (when miss == []), I checked the length of this window 
by subtracting the maximum index and the minimum index of the characters. 
If this window is the smallest one so far, I record its beginning and ending index as "start" and "end."
"""

class Solution3:
    # @return a string
    def minWindow(self, S, T):
        indices = {}
        for char in T:
            indices[char] = []
        miss = list(T)
        start = 0
        end = len(S)
        for i in range(len(S)):
            if S[i] in T:
                if S[i] not in miss and indices[S[i]] != []:
                    indices[S[i]].pop(0)
                elif S[i] in miss:
                    miss.remove(S[i])
                indices[S[i]].append(i)
            if miss == []:
                maximum = max([x[-1] for x in indices.values()])
                minimum = min([x[0] for x in indices.values()])
                if maximum-minimum+1 < end-start+1:
                    start = minimum
                    end = maximum
        if miss != []:
            return ""
        else:
            return S[start:end+1]


class Solution4:
    def minWindow(self, s, t):
        score = 0
        wanted = collections.Counter(t)
        start, end = len(s), 3 * len(s)
        d = {}
        deq = collections.deque([])
        for i, c in enumerate(s):
            if c in wanted:
                deq.append(i)
                d[c] = d.get(c, 0) + 1
                if d[c] <= wanted[c]:
                    score += 1
                while deq and d[s[deq[0]]] > wanted[s[deq[0]]]:
                    d[s[deq.popleft()]] -= 1
                if score == len(t) and deq[-1] - deq[0] < end - start:
                    start, end = deq[0], deq[-1]
        return s[start:end + 1]


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


class Solution5:
    def minWindow(self, s, t):

        res = ""
        left, right, cnt, minLen = 0, 0, 0, float('inf')
        tcount = collections.Counter(t)
        scount = collections.defaultdict(int)
        while right < len(s):
            scount[s[right]] += 1
            if s[right] in tcount and scount[s[right]] <= tcount[s[right]]:
                cnt += 1
            while left <= right and cnt == len(t):
                if minLen > right - left + 1:
                    minLen = right - left + 1
                    res = s[left : right + 1]
                scount[s[left]] -= 1
                if s[left] in tcount and scount[s[left]] < tcount[s[left]]:
                    cnt -= 1
                left += 1
            right += 1
        return res


"""
一种稍微简单的方法，增减对T字符串统计用的字典的词频的方式，可以省略对S切片中元素个数的维护，也省去了中间的一大堆判断。
"""
class Solution6:
    def minWindow(self, s, t):

        res = ""
        left, cnt, minLen = 0, 0, float('inf')
        count = collections.Counter(t)
        for i, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                cnt += 1
            while cnt == len(t):
                if minLen > i - left + 1:
                    minLen = i - left + 1
                    res = s[left : i + 1]
                count[s[left]] += 1
                if count[s[left]] > 0:
                    cnt -= 1
                left += 1
        return res

class Solution8:
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]



