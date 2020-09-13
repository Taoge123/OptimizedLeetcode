"""
1371.Find-the-Longest-Substring-Containing-Vowels-in-Even-Counts
本题是prefix+Hash+状压的综合考察。

本题要求寻找最长substring，使得其中元音字母的频次是偶数。对于一个区间内的频次，我们必然不会挨个去统计，通常会采用前缀数组的方法。这样就转化为了减法：freq[i:j] = preFreq[j]-preFreq[i-1].

我们考察以第j个元素结尾的、最长的符合要求的子串。那么如何确定这个子串的左边界i呢？假设我们只关心一个字母a，我们希望[i:j]区间内该字母频次是偶数，必然要求该字母的preFreq[j]和preFreq[i-1]的奇偶性要相同。目前我们对preFreq[j]是已知的（假设是奇数），所以只要知道最小的i使得preFreq[i-1]是偶数即可。于是我们可以建立一个hash表，在遍历j的过程中，存下最早出现奇数次preFreq的位置j即可。

本题要求区间内五个元音字母的频次都是偶数，所以我们可以用5个bit组成的二进制数来编码，来代表preFreq[j]里五个字母频次的奇偶性。比如说我们遍历到j时，preFreq[j]对应的key=00100，就表示前j个元素里，字母i出现了奇数次而其他元音字母出现了偶数次。此时我们只要查看Map里是否之前曾经出现过这个相同的key，有的话，那么最长区间的左端点就是i = Map[key]+1，而区间长度就是j-Map[key]. 考察完j之后，如果key未曾被加入过Map中，则要记录Map[key] = j.

substring, subarray

X X X [X X X X] X
       ^     ^
       |     |
       i     j

freq[i:j] = freq[1:j] - freq[1:i-1]
              odd          odd
              even         even
              01010        01010

              00000 - 代表aeiou都出现了偶数次


map[odd] : the earliest k so that freq[1:k] is odd
map[even]
hash + prefix + state compression
map[key]: key is a 5-bit state

"""

import collections

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        table = collections.defaultdict(int)
        table[0] = -1
        count = [0] * 5
        res = 0
        for i in range(len(s)):
            if s[i] == 'a':
                count[0] += 1
            elif s[i] == 'e':
                count[1] += 1
            elif s[i] == 'i':
                count[2] += 1
            elif s[i] == 'o':
                count[3] += 1
            elif s[i] == 'u':
                count[4] += 1
            key = self.convert(count)
            if key in table:
                res = max(res, i - table[key])
            else:
                # if key never there before, we add this key, because we want the largest bandwith
                table[key] = i
        return res

    def convert(self, count):
        key = 0
        for i in range(5):
            if count[i] % 2 == 1:
                key += (1 << i)
        return key





