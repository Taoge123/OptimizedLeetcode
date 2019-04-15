"""
Similar to strange printer
Longest Palindromic Subsequence
Longest Palindromic Substring
Palindromic Substrings

https://leetcode.com/problems/count-different-palindromic-subsequences/discuss/109510/Python-DP%2BDFS-O(n2)-with-Explanations
http://www.cnblogs.com/grandyang/p/7942040.html
https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-730-count-different-palindromic-subsequences/
https://leetcode.com/problems/count-different-palindromic-subsequences/solution/


Given a string S, find the number of different non-empty palindromic subsequences in S,
and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:
Input:
S = 'bccb'
Output: 6
Explanation:
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
Example 2:
Input:
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation:
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
Note:

The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""

"""
Approach #1 Dynamic Programming (using 3D array) [Accepted]
Intuition and Algorithm

Let dp[x][i][j] be the answer for the substring S[i...j] where S[i] == S[j] == 'a'+x. 
Note that since we only have 4 characters a, b, c, d, thus 0 <= x < 4. The DP formula goes as follows:

If S[i] != 'a'+x, then dp[x][i][j] = dp[x][i+1][j], 
note that here we leave the first character S[i] in the window out due to our definition of dp[x][i][j].

If S[j] != 'a'+x, then dp[x][i][j] = dp[x][i][j-1], leaving the last character S[j] out.

If S[i] == S[j] == 'a'+x, 
then dp[x][i][j] = 2 + dp[0][i+1][j-1] + dp[1][i+1][j-1] + dp[2][i+1][j-1] + dp[3][i+1][j-1]. 
When the first and last characters are the same, we need to count all the distinct palindromes 
(for each of a,b,c,d) within the sub-window S[i+1][j-1] plus the 2 palindromes contributed by the first and last characters.

Let n be the length of the input string S, 
The final answer would be dp[0][0][n-1] + dp[1][0][n-1] + dp[2][0][n-1] + dp[3][0][n-1] mod 1000000007.
"""

"""
Let dp[len][i][x] be the number of distinct palindromes of the subtring starting at i of length len, 
where the first (and last) character is x. The DP formula is simple :

- If s[i] != x, then dp[len][i][x] = dp[len-1][i+1][x] (ignoring the first character in this window)
- If s[i+len-1] != x then dp[len][i][x] = dp[len-1][i][x] (ignoring the last character in this window)
- If both the first and last characters are x, 
  then we need to count the number of distinct palindromes in the sub-window from i+1 to i + len -2. 
  Need to be careful with how we count empty string.
  Since we only need to subproblems of length len-1, len-2, 
  we only need to remember the solutions for the subproblems of length len, len-1, len-2. 
  This is needed to pass the max test case.
"""
"""
Nice way to deal with duplicates! A little hard to understand, here is my explaination @wang.senyuan @shuoshuo70
:

Let palindromes[c] be palindromes starting and ending with c

If s[i] != c, dp[l][i][c] = dp[l-1][i+1][c] (When s[i]!=c, all palindromes[c] in substrings of s[i:j] are in substrings of s[i+1:j], which is dp[l-1][i+1][c])

If s[j] != c, dp[l][i][c] = dp[l-1][i][c] (When s[j]!=c, all palindromes[c] in substrings of s[i:j] are in substrings of s[i:j-1], which is dp[l-1][i][c])

If s[i] == s[j] == c, dp[l][i][c] = 2 + sum(dp[l-2][i+1]) 

(The two basics are c and cc, others are all distinct palindromes[x] in substrings of s[i+1:j-1], 
in the format of c palindromesInS[i+1:j-1] c, since all palindromesInS[i+1:j-1] are distinct, 
c palindromesInS[i+1:j-1] c are distinct too, so the distinctiveness is never broken in the process)

So the result is comprehensive and doesn't contain duplicates.

Here is my Python Solution, but it use terrible 5500ms...
"""
class SolutionSlow:
    def countPalindromicSubsequences(self, S):

        mod = 10 ** 9 + 7
        N = len(S)
        S = [ord(_) - ord('a') for _ in S]
        dp = [[[0 for _ in range(4)] for __ in range(N)] for ___ in range(2)]

        for l in range(N):
            dp.append([[0 for _ in range(4)] for __ in range(N)])
            for i in range(N - l):
                j = i + l

                for c in range(4):
                    if l == 0:
                        dp[2][i][c] = 1 if S[i] == c else 0
                    else:
                        if S[i] != c:
                            dp[2][i][c] = dp[1][i + 1][c]
                        elif S[j] != c:
                            dp[2][i][c] = dp[1][i][c]
                        else:
                            dp[2][i][c] = 2 + (sum(dp[0][i + 1]) % mod if l > 1 else 0)
            dp.pop(0)
            # for _ in dp[2]:
            #     print(_)
            # print()

        return sum(dp[-1][0]) % mod


"""
I started out with only the DFS part, got TLE, then designed the DP part cache and passed.

The computations are done in DFS(start, end) in which I computed the answer for the string S[start, end]. cache is only to save the results of the computations in order to avoid repetitions.

In DFS(start, end), for instance, for the letter 'a', I compute the number of palindromes that start and end with 'a' in the following way:

First of all, I compute when 'a' appears first (index i) and last (index j) in the segment I am considering. Then it breaks down into two cases:

If i == j. There is only one 'a' in the segment. So the answer is 1.
If i != j. The possible palindromes are 'a', 'aa', and 'a*a' where '*' stands for any palindromes contained in S[i+1:j]. The answer would be DFS(i+1,j) + 2. Since I want to avoid repetitive computation, I write cache(i+1,j) + 2 instead.
The worst case time complexity is O(n^2). The best case time complexity is O(n).

Btw, to make this algorithm even faster, one could set check to be a 2D list instead of a dictionary, but that would occupy more space.
"""


class Solution1:
    def countPalindromicSubsequences(self, S):

        def helper(start, end):  # res for S[start:end]
            if (start, end) in self.cache:
                return self.cache[(start, end)]
            res = 0
            for char in 'abcd':
                l, r = S[start:end].find(char), S[start:end][::-1].find(char)
                if l != -1 and r != -1:
                    i = start + l
                    j = end - 1 - r
                    res += helper(i + 1, j) + 2 if i != j else 1
            self.cache[(start, end)] = res % (10 ** 9 + 7)
            return self.cache[(start, end)]

        self.cache = {}
        return helper(0, len(S))


class Solution11:
    def countPalindromicSubsequences(self, S):

        def count(S, i, j):
            if i > j: return 0
            if i == j: return 1
            if self.m_[i][j]:
                return self.m_[i][j]
            if S[i] == S[j]:
                ans = count(S, i + 1, j - 1) * 2
                l = i + 1
                r = j - 1
                while l <= r and S[l] != S[i]:
                    l += 1
                while l <= r and S[r] != S[i]:
                    r -= 1
                if l > r:
                    ans += 2
                elif l == r:
                    ans += 1
                else:
                    ans -= count(S, l + 1, r - 1)
            else:
                ans = count(S, i + 1, j) + count(S, i, j - 1) - count(S, i + 1, j - 1)

            self.m_[i][j] = ans % (10 ** 9 + 7)
            return self.m_[i][j]

        n = len(S)
        self.m_ = [[None for _ in range(n)] for _ in range(n)]
        return count(S, 0, n - 1)

"""
这道题给了给了我们一个字符串，让我们求出所有的非空回文子序列的个数，虽然这题限制了字符只有四种，
但是我们还是按一般的情况来解吧，可以有26个字母。然后说最终结果要对一个很大的数字取余，
这就暗示了结果会是一个很大的值，那么对于这种问题一般都是用DP或者是带记忆数组memo的递归来解，二者的本质其实是一样的。
我们先来看带记忆数组memo的递归解法，这种解法的思路是一层一层剥洋葱，比如"bccb"，按照字母来剥，先剥字母b，
确定最外层"b _ _ b"，这会产生两个回文子序列"b"和"bb"，然后递归进中间的部分，把中间的回文子序列个数算出来加到结果res中，
然后开始剥字母c，找到最外层"cc"，此时会产生两个回文子序列"c"和"cc"，然后由于中间没有字符串了，所以递归返回0，
按照这种方法就可以算出所有的回文子序列了。

我们建立一个二维数组chars，外层长度为26，里面放一个空数组。这是为了统计每个字母在原字符串中出现的位置，
然后定义一个二维记忆数组memo，其中memo[i][j]表示第i个字符到第j个字符之间的子字符串中的回文子序列的个数，
初始化均为0。然后我们遍历字符串S，将每个字符的位置加入其对应的数组中，比如对于"bccb"，那么有：

b -> {0, 3}

c -> {1, 2}

然后在[0, n]的范围内调用递归函数，在递归函数中，首先判断如果start大于等于end，返回0。
如果当前位置在memo的值大于0，说明当前情况已经计算过了，直接返回memo数组中的值。
否则进行所有字母的遍历，如果某个字母对应的数组中没有值，说明该字母不曾在字符串中出现，跳过。
然后我们在字母数组中查找第一个不小于start的位置，查找第一个小于end的位置，当前循环中，start为0，end为4，
当前处理字母b，我们的new_start指向0，new_end指向3，如果当前new_start指向了end()，或者其指向的位置大于end，
说明当前范围内没有字母b，直接跳过，否则结果res自增1，因为此时new_start存在，至少有个单个的字母b，也可以当作回文子序列，
然后看new_start和new_end如果不相同，说明两者各指向了不同的b，此时res应自增1，因为又增加了一个新的回文子序列"bb"，
下面就是对中间部分调用递归函数了，把返回值加到结果res中。此时字母b就处理完了，现在处理字母c，此时的start还是0，
end还是4，new_start指向1，new_end指向2，跟上面的分析相同，new_start在范围内，结果自增1，因为加上了"c"，
然后new_start和new_end不同，结果res再自增1，因为加上了"cc"，其中间没有字符了，调用递归的结果是0，for循环结束，
我们将memo[start][end]的值对超大数取余，将该值返回即可

class Solution {
public:
    int countPalindromicSubsequences(string S) {
        int n = S.size();
        vector<vector<int>> chars(26, vector<int>());
        vector<vector<int>> memo(n + 1, vector<int>(n + 1, 0));
        for (int i = 0; i < n; ++i) {
            chars[S[i] - 'a'].push_back(i);
        }
        return helper(S, chars, 0, n, memo);
    }
    int helper(string S, vector<vector<int>>& chars, int start, int end, vector<vector<int>>& memo) {
        if (start >= end) return 0;
        if (memo[start][end] > 0) return memo[start][end];
        long res = 0;
        for (int i = 0; i < 26; ++i) {
            if (chars[i].empty()) continue;
            auto new_start = lower_bound(chars[i].begin(), chars[i].end(), start);
            auto new_end = lower_bound(chars[i].begin(), chars[i].end(), end) - 1;
            if (new_start == chars[i].end() || *new_start >= end) continue;
            ++res;
            if (new_start != new_end) ++res;
            res += helper(S, chars, *new_start + 1, *new_end, memo);
        }
        memo[start][end] = res % int(1e9 + 7);
        return memo[start][end];
    }
};

"""
"""
我们再来看一种迭代的写法，使用一个二维的dp数组，其中dp[i][j]表示子字符串[i, j]中的不同回文子序列的个数，
我们初始化dp[i][i]为1，因为任意一个单个字符就是一个回文子序列，其余均为0。这里的更新顺序不是正向，也不是逆向，
而是斜着更新，对于"bccb"的例子，其最终dp数组如下，我们可以看到其更新顺序分别是红-绿-蓝-橙。


  b c c b
b 1 2 3 6
c 0 1 2 3
c 0 0 1 2
b 0 0 0 1

这样更新的好处是，更新当前位置时，其左，下，和左下位置的dp值均已存在，而当前位置的dp值需要用到这三个位置的dp值。
我们观察上面的dp数组，可以发现当S[i]不等于S[j]的时候，
dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]，即当前的dp值等于左边值加下边值减去左下值，
因为算左边值的时候包括了左下的所有情况，而算下边值的时候也包括了左下值的所有情况，那么左下值就多算了一遍，所以要减去。
而当S[i]等于S[j]的时候，情况就比较复杂了，需要分情况讨论，因为我们不知道中间还有几个和S[i]相等的值。
举个简单的例子，比如"aba"和"aaa"，当i = 0, j = 2的时候，两个字符串均有S[i] == S[j]，
此时二者都新增两个子序列"a"和"aa"，但是"aba"中间的"b"就可以加到结果res中，而"aaa"中的"a"就不能加了，
因为和外层的单独"a"重复了。我们的目标就要找到中间重复的"a"。所以我们让left = i + 1, right = j - 1，
然后对left进行while循环，如果left <= right, 且S[left] != S[i]的时候，left向右移动一个；
同理，对right进行while循环，如果left <= right, 且S[right] != S[i]的时候，left向左移动一个。
这样最终left和right值就有三种情况：

1. 当left > righ时，说明中间没有和S[i]相同的字母了，就是"aba"这种情况，
   那么就有dp[i][j] = dp[i + 1][j - 1] * 2 + 2，其中dp[i + 1][j - 1]是中间部分的回文子序列个数，
   为啥要乘2呢，因为中间的所有子序列可以单独存在，也可以再外面包裹上字母a，所以是成对出现的，要乘2。
   加2的原因是外层的"a"和"aa"也要统计上。

2. 当left = right时，说明中间只有一个和S[i]相同的字母，就是"aaa"这种情况，
   那么有dp[i][j] = dp[i + 1][j - 1] * 2 + 1，其中乘2的部分跟上面的原因相同，
   加1的原因是单个字母"a"的情况已经在中间部分算过了，外层就只能再加上个"aa"了。

3. 当left < right时，说明中间至少有两个和S[i]相同的字母，就是"aabaa"这种情况，
   那么有dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]，
   其中乘2的部分跟上面的原因相同，要减去left和right中间部分的子序列个数的原因是其被计算了两遍，要将多余的减掉。

class Solution {
public:
    int countPalindromicSubsequences(string S) {
        int n = S.size(), M = 1e9 + 7;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = 0; i < n; ++i) dp[i][i] = 1;
        for (int len = 1; len < n; ++len) {
            for (int i = 0; i < n - len; ++i) {
                int j = i + len;
                if (S[i] == S[j]) {
                    int left = i + 1, right = j - 1;
                    while (left <= right && S[left] != S[i]) ++left;
                    while (left <= right && S[right] != S[i]) --right;
                    if (left > right) {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2;
                    } else if (left == right) {
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1;
                    } else {
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1];
                    }
                } else {
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1];
                }
                dp[i][j] = (dp[i][j] < 0) ? dp[i][j] + M : dp[i][j] % M;
            }
        }
        return dp[0][n - 1];
    }
};

"""

class Solution2:
    def countPalindromicSubsequences(self, S):
        N = len(S)
        A = [ord(c) - ord('a') for c in S]
        prv = [None] * N
        nxt = [None] * N

        last = [None] * 4
        for i in xrange(N):
            last[A[i]] = i
            prv[i] = tuple(last)

        last = [None] * 4
        for i in xrange(N-1, -1, -1):
            last[A[i]] = i
            nxt[i] = tuple(last)

        MOD = 10**9 + 7
        memo = [[None] * N for _ in xrange(N)]
        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            ans = 1
            if i <= j:
                for x in xrange(4):
                    i0 = nxt[i][x]
                    j0 = prv[j][x]
                    if i <= i0 <= j:
                        ans += 1
                    if None < i0 < j0:
                        ans += dp(i0+1, j0-1)
            ans %= MOD
            memo[i][j] = ans
            return ans

        return dp(0, N-1) - 1

class Solution3:
    def countPalindromicSubsequences(self, S):
        n = len(S)
        mod = 1000000007
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(4)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                for k in range(4):
                    c = chr(ord('a') + k)
                    if j == i:
                        if S[i] == c:
                            dp[k][i][j] = 1
                        else:
                            dp[k][i][j] = 0
                    else:  # j > i
                        if S[i] != c:
                            dp[k][i][j] = dp[k][i + 1][j]
                        elif S[j] != c:
                            dp[k][i][j] = dp[k][i][j - 1]
                        else:  # S[i] == S[j] == c
                            if j == i + 1:
                                dp[k][i][j] = 2  # "aa" : {"a", "aa"}
                            else:  # length is > 2
                                dp[k][i][j] = 2
                                for m in range(4):  # count each one within subwindows [i+1][j-1]
                                    dp[k][i][j] += dp[m][i + 1][j - 1]
                                    dp[k][i][j] %= mod

        ans = 0
        for k in range(4):
            ans += dp[k][0][n - 1]
            ans %= mod

        return ans




