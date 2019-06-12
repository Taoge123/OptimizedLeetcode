
"""
Given a string which consists of lowercase or uppercase letters,
find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution1:
    def longestPalindrome(self, s):
        hash = set()
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)
        # len(hash) is the number of the odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)


"""
思路
这题是说从原字符串中挑选若干字符，重新组合使其形成最长的回文字符串。那么不妨来看看回文字符串的特点，
以dccaccd为例，其中d出现了2次、c出现了4次、a出现了1次，也就是说，回文字符串除了最中间的字符可以仅出现1次外，
其他的字符都需要出现2的倍数次。

那么反推就可以知道，只需要统计原字符串中每个字符出现的次数，然后将其全部向下取偶数（即4->4、5->4）再求和，
以及如果存在出现奇数次的字符，则在和的基础上再加1，就是最终结果了。

“统计原字符串中每个字符出现的次数”一般是用Map来保存，而考虑到题目中字符串中字符只可能是小写或大写字母，
所以我们可以直接用数组来模拟Map。
"""
class Solution2:
    def longestPalindrome(self, s):
        count_array = [0] * (ord('z') - ord('A') + 1)
        pair = 0
        is_odd_exists = False
        for item in s:
            count_array[ord(item) - ord('A')] += 1
        for item in count_array:
            pair += item // 2
            if not is_odd_exists:
                is_odd_exists = item % 2 != 0
        return pair * 2 + (1 if is_odd_exists else 0)


class Solution3:
    def longestPalindrome(self, s):
        # h = collections.Counter(s)
        h = {}
        for i in s:
            if i in h:
                h[i] += 1
            else:
                h[i] = 1
        c = 0
        sig = 0
        for i in h:
            c += h[i]/2
            if h[i] % 2 != 0:
                sig = 1
        return c * 2 + sig


class Solution4:
    def longestPalindrome(self, s):
        d={}
        res=0
        for i in s:
            d[i] = 1 if i not in d else d[i]+1
        for i in d:
            res+=d[i]-d[i]%2
        return res+1 if res<len(s) else res


