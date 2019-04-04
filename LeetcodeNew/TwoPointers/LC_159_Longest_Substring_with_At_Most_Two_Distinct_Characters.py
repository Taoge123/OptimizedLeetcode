
"""
https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
"""
"""
思路：

一道two pointers的题目：我们维护一个哈希表，记录当前有效子字符串中出现的字符以及其对应个数，
以及当前合法子字符串的起始位置start。在扫描字符串的过程中，如果发现当前字符在哈希表中已经出现了，
那么直接更新哈希表中相应字符的出现次数即可；否则就需要将该字符添加到哈希表中。但是注意添加之后有可能会导致哈希表的容量大于k，
这时就要移动起始位置start，并且更新哈希表，直到哈希表的容量重新不大于k。该算法的空间复杂度是O(k)，
因为哈希表中最多有k + 1个字符。时间复杂度是O(n)（请读者分析，for循环里面出现了while循环，为什么时间复杂度还是O(n)呢？
答案：用后向分析可知，字符串中的每个字符最多加入哈希表一次，弹出哈希表一次，所以while循环的整个执行次数不超过2n次，
其中n是字符串的长度。）
"""

"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
Accepted
67,793
Submissions
"""

"""
这道题给我们一个字符串，让我们求最多有两个不同字符的最长子串。那么我们首先想到的是用哈希表来做，哈希表记录每个字符的出现次数，
然后如果哈希表中的映射数量超过两个的时候，我们需要删掉一个映射，比如此时哈希表中e有2个，c有1个，此时把b也存入了哈希表，
那么就有三对映射了，这时我们的left是0，先从e开始，映射值减1，此时e还有1个，不删除，left自增1。
这是哈希表里还有三对映射，此时left是1，那么到c了，映射值减1，此时e映射为0，将e从哈希表中删除，left自增1，
然后我们更新结果为i - left + 1，以此类推直至遍历完整个字符串
"""

"""

 

我们除了用哈希表来映射字符出现的个数，我们还可以映射每个字符最新的坐标，比如题目中的例子"eceba"，
遇到第一个e，映射其坐标0，遇到c，映射其坐标1，遇到第二个e时，映射其坐标2，当遇到b时，映射其坐标3，
每次我们都判断当前哈希表中的映射数，如果大于2的时候，那么我们需要删掉一个映射，我们还是从left=0时开始向右找，
我们看每个字符在哈希表中的映射值是否等于当前坐标left，比如第一个e，哈希表此时映射值为2，不等于left的0，那么left自增1，
遇到c的时候，哈希表中c的映射值是1，和此时的left相同，那么我们把c删掉，left自增1，再更新结果，以此类推直至遍历完整个字符串
"""

"""
后来又在网上看到了一种解法，这种解法是维护一个sliding window，指针left指向起始位置，right指向window的最后一个位置，
用于定位left的下一个跳转位置，思路如下：

1. 若当前字符和前一个字符相同，继续循环。

2. 若不同，看当前字符和right指的字符是否相同

    (1) 若相同，left不变，右边跳到i - 1

    (2) 若不同，更新结果，left变为right+1，right变为i - 1

最后需要注意在循环结束后，我们还要比较res和s.size() - left的大小，返回大的，这是由于如果字符串是"ecebaaa"，
那么当left=3时，i=5,6的时候，都是继续循环，当i加到7时，跳出了循环，而此时正确答案应为"baaa"这4个字符，
而我们的res只更新到了"ece"这3个字符，所以我们最后要判断s.size() - left和res的大小。

另外需要说明的是这种解法仅适用于于不同字符数为2个的情况，如果为k个的话，还是需要用上面两种解法。
"""


import collections

class Solution1:
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n

        # sliding window left and right pointers
        left, right = 0, 0
        # hashmap character -> its rightmost position
        # in the sliding window
        hashmap = collections.defaultdict()

        max_len = 2

        while right < n:
            # slidewindow contains less than 3 characters
            if len(hashmap) < 3:
                hashmap[s[right]] = right
                right += 1

            # slidewindow contains 3 characters
            if len(hashmap) == 3:
                # delete the leftmost character
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                # move left pointer of the slidewindow
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

"""
I used a hash to store a mapping of the character to its latest position within the string. 
When the hash has K+1 different characters, the key is here to find the character 
with the smallest (left-most) position and eliminate it from the hash. 
The left pointer then starts from the next character after the eliminated character.
"""

class Solution2:
    def lengthOfLongestSubstringTwoDistinct(self, s):

        left, longest, d = 0, 0, {}
        maximum_distinct = 2
        for index, char in list(enumerate(s)):
            d[char] = index
            if len(d.keys()) == maximum_distinct + 1:
                index_to_remove = min([d[char] for char in d.keys()])
                d.pop(s[index_to_remove], None)
                left = index_to_remove + 1
            longest = max(longest, index - left + 1)
        return longest

class Solution3:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        dic = collections.defaultdict(int)
        start, end = 0, 0
        maxlen = -float('inf')
        n = len(s)
        while end < n:
            cur = s[end]
            if len(dic) == 2 and cur not in dic:  # find the third distinct char
                maxlen = max(maxlen, end - start)  # update max length
                pos = min(dic.values())  # find the last position of the first char in current window
                start = pos + 1  # update window (start from the second char)
                del dic[s[pos]]  # update dictionary by deleting the first char
            dic[cur] = end  # update position of current char
            end += 1
        return max(maxlen, n - start)





