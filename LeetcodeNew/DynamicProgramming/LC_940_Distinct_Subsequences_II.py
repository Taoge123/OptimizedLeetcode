
"""
https://zhanghuimeng.github.io/post/leetcode-940-distinct-subsequences-ii/

Given a string S, count the number of distinct, non-empty subsequences of S .

Since the result may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:

Input: "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and "aba".
Example 3:

Input: "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".

Note:

S contains only lowercase letters.
1 <= S.length <= 2000
"""
"""
嗯这里更具体讲一讲，思路是怎么一步一步想的。
最开始的思路是用Trie来表示所有可能subseq.
遍历string S，对Trie中每个节点新建叶节点。
提交后果然答案对了，但是Memory Limit Exceed。
转念一想，没必要存下所有节点，只需要知道当前节点的数量就好了。
Trie中一个节点对应一个seq。
假设当前有N个不同的seq，每个seq加上一个新的字母，又是新的N个不同sequence了。
但新的seq中，有一部分原来就有。
比如新的字母是'a'，那么原来以'a'结尾的seq，每一个都会存在新的这N个seq中。
到这里，解题思路就比较清楚了。
我们需要用一个数组int endsWith[26]，
endsWith[i]来表示以第i个字母结束的sequence数量。
最后修饰一下代码细节。

数组全部初始化为0。
正好按照题目要求，空string不计作subseq。
每次更新的时候，end[i] = sum(end) + 1。
加一的原因是，比如我们遇到新字母'a'，新的N个seq里不包含“a”，需要额外加上
"""

"""
使用一个endswith[26]数组，保存的是有多少个子序列以i结尾。
则，当前总共有N = sum(endswith)个不同的子序列，当我们新增加一个字符c时，
相当于在以前每个结尾的位置后面又增添了一个新的字符，所以现在有了N个以c结尾的不同的子序列了。

所以，我们遍历一遍s，更新的方式是end[c] = sum(end) + 1。加一是因为c本身也是一个子序列。

比如举个例子。

Input: "aba"
Current parsed: "ab"

endswith 'a': ["a"]
endswith 'b': ["ab","b"]

"a" -> "aa"
"ab" -> "aba"
"b" -> "ba"
"" -> "a"

endswith 'a': ["aa","aba","ba","a"]
endswith 'b': ["ab","b"]
result: 6
"""
import collections

class SolutionLee:
    def distinctSubseqII(self, S):
        end = [0] * 26
        for c in S:
            end[ord(c) - ord('a')] = sum(end) + 1
        return sum(end) % (10**9 + 7)


"""
这个方法比较简洁，时间O(26N)，空间O(26)
可以看心情优化的地方是，用一个变量保存当前数组和，避免重复计算。
时间优化到O(N).
"""
class SolutionLee2:
    def distinctSubseqII(self, S):
        res, end = 0, collections.Counter()
        for c in S:
            res, end[c] = res * 2 + 1 - end[c], res + 1
        return res % (10**9 + 7)


"""
题意分析：
又到了说这句话的时候。看到mod 1e9+7就要想到dp，这在我写的题解里面经常提到。

思路分析：
在我们知道要用dp的情况，如何去定义dp呢，首先看数据范围，看我们能定义几维的dp
len(s) <= 2000，看样子可以定义2维的，但是按照套路来定义dp[i][j]表示s[i:j+1]中不同子序列的个数，好像是行不通的，因为推不出递推关系式。

这个时候可以换个思路，我定义dp[i][c]表示以字符c结尾的长度为i的子序列的个数
那么我们来分析一下递推式：
dp[3]['a']表示长度为3的以’a’结尾的子序列的个数。
那么它是不是等于所有长度为2的以’abcd…xyz’结尾的序列之和。
所以有， dp[n][c] = sum(dp[n-1][k] for k in 'abcd...xyz')

我们所求的结果应该怎么用dp来表示呢？
既然求所有的不同子序列的个数，那么应该是包括：
以’a’结尾的长度为(1,2,3,..,n)的子序列的个数
以’b’结尾的长度为(1,2,3,..,n)的子序列的个数
…
以’z’结尾的长度为(1,2,3,..,n)的子序列的个数
也就是所有dp[i][j]的和

最后考虑初始化条件，显然长度为1的以c结尾的子序列个数必为1。
也就是dp[1][c] = 1 for c in S
"""
"""
但是很可惜，如果用空间这样迭代，会cost大量时间，并且最后计算res又要将整个dp重新迭代一遍
当len(s) = 2000时，平方就到了4000000，然后还迭代这么多次，最后超时了。

当然，len(s)<2000可以用2维dp这个理论是没错的，这里就涉及到leetcode中判题的方法了
像codeforces这种，都是每一个例子单独算，然后取所有例子中运行时间最大的时间作为你这道题的最终运行时间。
而leetcode是把所有的test case一起运，总时间作为你的运行时间。即使上面这个方法过单个2000长度的case很轻松，
但是case一多，就会超时，我们得想办法优化一下。(可惜，如果不优化成1维，按照我这个思路，我调了很久都没调出来ac的代码，
但是discuss里面好像有人是n^2的代码通过的)

我们注意到每一维的计算只与上一维的结果有关，可以用到滚动数组，这样就可以优化成一维的了。
"""
class Solution2:
    def distinctSubseqII(self, S):
        dp = [0] * 26
        mod = 10**9+7
        for ss in S:
            dp[ord(ss)-ord('a')] = sum(dp) + 1
        return sum(dp) % mod


"""
using dp, general idea:
if ch seen already:

    - dp[ j ] = d[ j-1 ]*2 - dp[ i = index of last occurance of character-1 ]
    - (Reason: one want to avoid overcounting in the case of a sequence with i to j all empty)
else:

    - dp[ j ] = d[ j-1 ]*2
    - (Reason: two ways to pick at index j, either empty or the new character)
final ans = last dp -1 (the empty seq)

52 ms
TiME = O(N), SPACE = O(N)
"""


class Solution3:
    def distinctSubseqII(self, S):

        dp, d = [1] + [0] * len(S), {}
        dp[1] = 2
        d[S[0]] = 0  # map from char to last location
        m = 10 ** 9 + 7

        for i in range(1, len(S)):
            ch = S[i]
            index = i + 1  # dp index
            if ch not in d:
                dp[index] = dp[index - 1] * 2 % m
            else:
                dp[index] = (dp[index - 1] * 2 - dp[d[ch]]) % m
            d[ch] = i

        return dp[-1] - 1


class Solution4:
    def distinctSubseqII(self, S):

        dp = [1] * len(S)
        dic = {S[0]: 0}
        m = 10 ** 9 + 7
        for i in range(1, len(S)):
            n = S[i]
            if n not in dic:
                dp[i] = sum(dp[:i]) + 1 % m
            else:
                dp[i] = sum(dp[dic[n]:i]) % m
            dic[n] = i
        return sum(dp) % m


""""
Thought:

Use a count array to record # of unique subsequences ended with for S[i] with one additional count[0] = 1 for the beginning empty space
For S[i] - if there is no same letter before this one, 
the total # of unique subsequences ended with S[i], i.e. count[i+1] is simply total of all previous unique subseqences
But if there is a prior letter same as S[i], any unique subsequences before the prev[S[i]] do not count, 
but everything after prev[S[i]] (inclusive) plus S[i] will still form new unique subsequences

The final total is sum of the count array excluding the count[0] = 1 for the beginning

Final code is given below with O(N^2) time (could be improved with a cumsum) and O(N) space
"""
class Solution5:
    def distinctSubseqII(self, S):
        if S == "":
            return 0
        count, prev = [1] * (len(S)+1), {}
        for i in range(len(S)):
            if S[i] in prev:
                count[i+1] = sum(count[prev[S[i]]:i+1])
            else:
                count[i+1] = sum(count[0:i+1])
            prev[S[i]] = i+1
        return sum(count[1:]) % 1000000007


# Optimize with cumsum - runtime from 120 ms to 40 ms:
class Solution6:
    def distinctSubseqII(self, S):
        if S == "":
            return 0
        count, prev, cumsum = [1] * (len(S) + 1), {}, [1] * (len(S) + 1)
        for i in range(len(S)):
            if S[i] in prev:
                count[i + 1] = cumsum[i] - cumsum[prev[S[i]] - 1]
            else:
                count[i + 1] = cumsum[i]
            prev[S[i]] = i + 1
            cumsum[i + 1] = (cumsum[i] + count[i + 1]) % 1000000007

        return (cumsum[-1] - 1) % 1000000007

"""
Assume that input is: abccbc

input a
a
input b
a/b ab
input c
a/b ab/c ac bc abc
input c
a/b ab/c ac bc abc/...
In this situation, we found that a/b ab/ has alread been connected to the previous c, so we can only connect the new c to the rest substring. The ... part should be cc acc bcc abcc
From the above example, we can infer that:
(1) if a new char appears, we just double the result number and add one(for the new char).
(2) if the char has appeared, we just add the count of the subsequences which behind the previous char's position.
"""


class Solution7:
    def distinctSubseqII(self, S):

        res = 0
        dic = {}
        for c in S:
            if c not in dic:
                dic[c] = res
                res = 2 * res + 1
            else:
                dic[c], res = res, 2 * res - dic[c]

        return res % (10 ** 9 + 7)


"""
动态规划
周赛的第四题，不会做，还是因为我的动态规划太弱了。。

瞻仰一下寒神的做法吧，膜拜！[C++/Java/Python] 4 lines O(N) Time, O(1) Space。

使用一个endswith[26]数组，保存的是有多少个子序列以i结尾。则，当前总共有N = sum(endswith)个不同的子序列，当我们新增加一个字符c时，相当于在以前每个结尾的位置后面又增添了一个新的字符，所以现在有了N个以c结尾的不同的子序列了。

所以，我们遍历一遍s，更新的方式是end[c] = sum(end) + 1。加一是因为c本身也是一个子序列。

比如举个例子。

Input: "aba"
Current parsed: "ab"

endswith 'a': ["a"]
endswith 'b': ["ab","b"]

"a" -> "aa"
"ab" -> "aba"
"b" -> "ba"
"" -> "a"

endswith 'a': ["aa","aba","ba","a"]
endswith 'b': ["ab","b"]
result: 6
时间复杂度是O(26N)，空间复杂度是O(1)。
"""
class Solution111:
    def distinctSubseqII(self, S):
        nums = [0] * 26
        for s in S:
            nums[ord(s) - ord("a")] = (sum(nums) + 1) % (10 ** 9 + 7)
        return sum(nums) % (10 ** 9 + 7)


"""
观察规律疑似， dp[i] = dp[0] + … dp[i-1] + 1
因为dp[i]一定是包括下面这些的和
* dp[0] + s.charAt(i)
* dp[1] + s.charAt(i)
* ….
* dp[i-1] + s.charAt(i)
* s.charAt(i)

所以， 这个dp递推规则是符合逻辑的。
这时候， 我们要去重, 假设j < i, 并且i和j字符重复， 那么可以看到， 所有的重复都会来自于j之前的，
比如abcc， 所有的重复都来自于第4个c和前面的ab任意选择后组成的结果，以及加上c自己，
而这个结果就是dp[j], 也就是所有下面这些会重复， 把其中的s.charAt(j)换成s.charAt(i)以后是一样的：
* dp[0]+s.charAt(j)
* dp[1]+s.charAt(j)
* …
* dp[j-1]+s.charAt(j)
* s.charAt(j)

如果这样的话，去重就好办了，对于i和j相等的情况，递推的时候不加上就好了。
"""

"""
解题思路：记dp[i]为以S[i]元素结尾可以组成的子串的个数，很显然dp[0] = 1。
显然dp[i]的前一个元素可以是dp[0] ~ dp[i-1]中的任何一个，那么应该有dp[i] = dp[0] + dp[1] +...dp[i-1]。
这是对于元素没有重复的情况。假设S[j]是S[0-i]中与S[i]下标最接近的元素并且有S[i] = S[j]，那么在以S[i]结尾的子串中，
前一个元素是在S[0]~S[j-1]中的任何一个，都会和以S[j]结尾的子串中并且前一个元素是在S[0]~S[j-1]中的任何一个重复，
因此这种情况下dp[i] = dp[j]+dp[j+1] + ... dp[i-1]。最后，返回的结果应该为sum(dp）。

"""

class Solution22:
    def distinctSubseqII(self, S):
        dp = [1] * len(S)
        for i in range(1,len(S)):
            for j in range(i-1,-1,-1):
                if S[i] != S[j]:
                    dp[i] += dp[j]
                else:
                    dp[i] += dp[j]
                    dp[i] -= 1
                    break
        #print dp
        return sum(dp) % (pow(10,9) + 7)


"""
使用一個endswith[26]數組，保存的是有多少個子序列以i結尾。則，當前總共有N = sum(endswith)個不同的子序列，
當我們新增加一個字符c時，相當於在以前每個結尾的位置後面又增添了一個新的字符，所以現在有了N個以c結尾的不同的子序列了。

所以，我們遍歷一遍s，更新的方式是end[c] = sum(end) + 1。加一是因爲c本身也是一個子序列。

"""
class Solution33:
    def distinctSubseqII(self, S):

        nums = [0] * 26
        for s in S:
            nums[ord(s) - ord("a")] = (sum(nums) + 1) % (10 ** 9 + 7)
        return sum(nums) % (10 ** 9 + 7)













