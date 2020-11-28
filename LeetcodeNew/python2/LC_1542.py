"""

1542.Find-Longest-Awesome-Substring
本题的本质是求一个最长的区间，使得区间内的字符能够重组成为回文数。重组成为回文数的条件是：统计每个字符的词频，词频为奇数的字符最多只能有1个。

对于区间的词频统计，我们不会手工来数。用前缀数组的方法比较常见，也就是转化成了前缀数组的减法。我们用prefix[j]-prefix[i-1]，就可以求出区间[i:j]范围内每个字符的频次。

现在我们固定区间的右端点j，来探索区间的左端点i在哪里？我们希望找到这样的一个左端点i：使得区间[i:j]的字符频次满足重组回文数的要求，那么就是说prefix[j]-prefix[i-1]需要满足重组回文数的要求。我们可以发现两种情况：

所有的字符，prefix[j]和prefix[i-1]的奇偶性相同，那么说明prefix[j]-prefix[i-1]必然是偶数，即[i:j]区间里所有字符的词频必然都是偶数，即满足重组回文数的要求。
只有一种字符，prefix[j]和prefix[i-1]的奇偶性不同，那么对于该字符而言prefix[j]-prefix[i-1]必然是奇数，即[i:j]区间里仅有一种字符的词频是奇数，也满足重组回文数的要求。
也就是说，我们知道了prefix[j]的奇偶性，想求一个最小的i，使得prefix[i-1]的奇偶性满足特定的条件。这就需要用到hash表。key是前缀频次的奇偶性（我们想要的），value是相应的前缀的index（我们相查的）。

那么如何用一个key来表达十个字符的频次奇偶性呢？显然我们用10个二进制位来编码就行了。注意，如果你用10个字01符组成的字符串来作为key存储，会TLE。

具体的做法就是我们每次处理完一个元素k之后，都会将截止k的所有字符的前缀频次编码为key放入hash表。如果后续操作中，需要寻找特定的“字符频次奇偶性”，就可以通过这个表找到这个前缀所在的位置i，那么[i:j]就是一个符合要求的subarray。

注意上述的第二种情况，我们需要创建10个新key来在hash表中查找。比如说pefix[j]的所有字符奇偶性是1000000001，那么我们会操作十次，每次将1000000001中的一个bit反转，查看hash表中是否存在了这样的一个key。如果存在的话，说明在这个区间内，该字符对应的频次是奇数，而其他的都是偶数，故符合重组回文数的要求。

the character w/ odd count must be no longer than 1
for a given character
freq[i:j] = prefix[j] - prefix[i-1]

1. all characters: count are even
2. only one character: count is odd

with prefix[i-1] is odd/even known, we'd like to know the smallest i
key: odd/even of prefix, value : idx
prefix[j] : 1000001 -> prefix[i-1] : 1000001
prefix[j] : 1000001 -> prefix[i-1] : 0000001
                                     1100001
                                     1100001

"""


class Solution:
    def longestAwesome(self, s: str) -> int:
        table = {0 : -1}
        count = [0] * 10
        res = 0
        for i in range(len(s)):
            count[int(s[i])] += 1
            key = self.convert(count)
            if key in table:
                res = max(res, i - table[key])
            # if any of the newKey, which is to include one key diff
            for k in range(10):
                newKey = key
                if ((key>>k)&1)==0:
                    newKey += (1<<k)
                else:
                    newKey -= (1<<k)
                if newKey in table:
                    res = max(res, i - table[newKey])
            if key not in table:
                table[key] = i
        return res

    def convert(self, count):
        key = 0
        for i in range(10):
            key += ((count[i]%2)<<i)
        return key



