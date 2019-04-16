
"""
We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words,
and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual.
It is expected that a 50 sticker test case can be solved within 35ms on average.
"""

"""
There are potentially a lot of overlapping sub problems, but meanwhile we don't exactly know what those sub problems are. 
DP with memoization works pretty well in such cases. The workflow is like backtracking, but with memoization. 
Here I simply use a sorted string of target as the key for the unordered_map DP. 
A sorted target results in a unique sub problem for possibly different strings.

dp[s] is the minimum stickers required for string s (-1 if impossible). Note s is sorted.
clearly, dp[""] = 0, and the problem asks for dp[target].

The DP formula is:

dp[s] = min(1+dp[reduced_s]) for all stickers, 
here reduced_s is a new string after certain sticker applied

Optimization: If the target can be spelled out by a group of stickers, at least one of them has to contain character target[0]. 
So I explicitly require next sticker containing target[0], which significantly reduced the search space.

"""
import sys
import collections

class Solution1:
    def minStickers(self, stickers, target):
        m = len(stickers)
        mp = [[0] * 26 for y in range(m)]
        for i in range(m):
            for c in stickers[i]:
                mp[i][ord(c) - ord('a')] += 1
        dp = {}
        dp[""] = 0

        def helper(dp, mp, target):
            if target in dp:
                return dp[target]
            n = len(mp)
            tar = [0] * 26
            for c in target:
                tar[ord(c) - ord('a')] += 1
            ans = sys.maxint
            for i in range(n):
                if mp[i][ord(target[0]) - ord('a')] == 0:
                    continue
                s = ''
                for j in range(26):
                    if tar[j] > mp[i][j]:
                        s += chr(ord('a') + j) * (tar[j] - mp[i][j])
                tmp = helper(dp, mp, s)
                if (tmp != -1):
                    ans = min(ans, 1 + tmp)
            dp[target] = -1 if ans == sys.maxint else ans
            return dp[target]

        return helper(dp, mp, target)

"""
1. The big idea is to use number from 0 to 2^n-1 as bitmap to represent every subset of target;
2. Then populate all of these subset from 0 to 2^n-1 by trying to apply 1 sticker at each time.
3. Eventually you might or might not get the ultimate result 2^n-1, which is target, populated.


class Solution {
    public int minStickers(String[] stickers, String target) {
        int n = target.length(), m = 1 << n; // if target has n chars, there will be m=2^n-1 subset of characters in target
        int[] dp = new int[m];
        for (int i = 0; i < m; i++) dp[i] = Integer.MAX_VALUE; // use index 0 - 2^n-1 as bitmaps to represent each subset of all chars in target
        dp[0] = 0; // first thing we know is : dp[empty set] requires 0 stickers,
        for (int i = 0; i < m; i++) { // for every subset i, start from 000...000
            if (dp[i] == Integer.MAX_VALUE) continue;
            for (String s : stickers) { // try use each sticker as an char provider to populate 1 of its superset, to do that:
                int sup = i;
                for (char c : s.toCharArray()) { // for each char in the sticker, try apply it on a missing char in the subset of target
                    for (int r = 0; r < n; r++) {
                        if (target.charAt(r) == c && ((sup >> r) & 1) == 0) {
                            sup |= 1 << r;
                            break;
                        }
                    }
                }
               // after you apply all possible chars in a sticker, you get an superset that take 1 extra sticker than subset
               // would take, so you can try to update the superset's minsticker number with dp[sub]+1;
                dp[sup] = Math.min(dp[sup], dp[i] + 1);
            }
        }
        return dp[m - 1] != Integer.MAX_VALUE ? dp[m - 1] : -1;
    }
}

There are three elegant ideas I appreciate most inside this solution

1. Applying bits to represent the "status", by the help of restriction where target's size is smaller than 15. 
   And if i is a subproblem of j, then must i < j holds.

2. The dp solution here is bottom-up, so at each turn we can check whether dp[i] == -1 
   or not to skip useless status. I've written a similar solution after reading dreamoon's codes, 
   but my version is top-down, at each turn I need to check many unreachable sub-situations.

3. Using unsigned_int, so that we can always say "dp[now] = min(dp[now], dp[i]+1) ", because for uint, -1 is something like INT_MAX.
"""

class Solution2:
    def minStickers(self, stickers, target):
        stickers, self.map = [collections.Counter(s) for s in stickers if set(s) & set(target)], {}
        def dfs(target):
            if not target:
                return 0
            if target in self.map:
                return self.map[target]
            cnt, res = collections.Counter(target), float('inf')
            for c in stickers: # traverse the stickers to get new target
                if c[target[0]] == 0:
                    continue # we can make sure the 1st letter will be removed to reduce the time complexity
                nxt = dfs(''.join([s * t for (s, t) in (cnt - c).items()]))
                if nxt != -1:
                    res = min(res, 1 + nxt)
            self.map[target] = -1 if res == float('inf') else res
            return self.map[target]
        return dfs(target)



class Solution3:
    def minStickers(self, stickers, target):
        cnt, res, n = collections.Counter(target), [float("inf")], len(target)
        def dfs(dic, used, i):
            if i == n:
                res[0] = min(res[0], used)
            elif dic[target[i]] >= cnt[target[i]]:
                dfs(dic, used, i + 1)
            elif used < res[0] - 1:
                for sticker in stickers:
                    if target[i] in sticker:
                        for s in sticker:
                            dic[s] += 1
                        dfs(dic, used + 1, i + 1)
                        for s in sticker:
                            dic[s] -= 1
        dfs(collections.defaultdict(int), 0, 0)
        return res[0] < float("inf") and res[0] or -1


class Solution4:
    def minStickers(self, stickers, target):

        def backtrack(index, used):
            if index == N:
                self.ans = min(self.ans, used)
                return
            if self.ans == used:
                return
            if cnt[target[index]] <= 0:
                backtrack(index + 1, used)
            else:
                for stick in stickers:
                    if target[index] in stick:
                        for s in stick:
                            cnt[s] -= 1
                        backtrack(index + 1, used + 1)
                        for s in stick:
                            cnt[s] += 1

        N = len(target)
        cnt = collections.Counter(target)
        self.ans = float('inf')
        backtrack(0, 0)
        return self.ans if self.ans < float('inf') else -1



class Solution5:
    def minStickers(self, stickers, target):
        from functools import lru_cache
        stickers = map(collections.Counter, stickers)
        @lru_cache(None)
        def dfs(target):
            res = 1e9
            if target == '' : return 0
            for st in stickers:
                if target[0] in st:
                    new = target
                    for i in st:
                        new = new.replace(i, '', st[i])
                    res = min(res, 1 + dfs(new))
            return res
        ans = dfs(target)
        return ans if ans < 1e9 else -1


"""
给定一个字符串集合S,以及一个目标字符串T.求使用S中字符串的最小个数，能够满足T需要的字符数。类似于多目标优化的问题（弄清这一类问题如何求解）
背包问题（变形）
给定物品的特点
给定背包的限制
求最小的物品的数量。

【位图法】因为待匹配串target的数量最多是15个，因此其子集的数量最多有 2^15个，而int类型占用四个字节，
能够容纳标识所有target的子集。所以我们可以将target的子集 映射到 int的整型数中。
【int 与 target子集之间的映射关系】将int类型分解为二进制的形式后，有些位置为0，有些位置为1.
表明在target中哪些位置的字符是否保留（1表示保留）。
【动态规划】dp中存储的是得到子集i,需要的最少的单词的数量。

class Solution {
    public int minStickers(String[] stickers, String target) {
        int n = target.length(), m = 1 << n; // if target has n chars, there will be m=2^n-1 subset of characters in target
        int[] dp = new int[m];
        for (int i = 0; i < m; i++) dp[i] = Integer.MAX_VALUE; // use index 0 - 2^n-1 as bitmaps to represent each subset of all chars in target
        dp[0] = 0; // first thing we know is : dp[empty set] requires 0 stickers,
        for (int i = 0; i < m; i++) { // for every subset i, start from 000...000。（起点这里很重要，因为大的集合往往依赖于小的集合）
            if (dp[i] == Integer.MAX_VALUE) continue;
            for (String s : stickers) { // try use each sticker as an char provider to populate 1 of its superset, to do that:
                int sup = i;//关键代码（下面：在i上面加入一个单词后的效果）
                for (char c : s.toCharArray()) { // for each char in the sticker, try apply it on a missing char in the subset of target
                    for (int r = 0; r < n; r++) {
                        if (target.charAt(r) == c && ((sup >> r) & 1) == 0) {  //如果target中包含字符c , 并且sup中相应位置没有c。
                            sup |= 1 << r;//在sup中相应位置，加入c，形成新的集合。
                            break;
                        }
                    }
                }
               // after you apply all possible chars in a sticker, you get an superset that take 1 extra sticker than subset
               // would take, so you can try to update the superset's minsticker number with dp[sub]+1;
                dp[sup] = Math.min(dp[sup], dp[i] + 1);//判断是否需要替换原来sup中的值。
            }
        }
        return dp[m - 1] != Integer.MAX_VALUE ? dp[m - 1] : -1;
    }
}

"""
"""
Let assume that we have partially spellout target by (i-1) picking words. 
Now we pick word k. Let dp[i][k] be all possible partial spelling of the target using word stickers[k] 
and differt partial spelling from i-1. Then dp[i][k] is the best 
(maximum len of partial spelling) of spelling using word k.
"""

class Solution6:
    def minStickers(self, stickers, target):

        dp = [0] + [-1] * ((1 <<  len(target)) - 1)
        tcnt = collections.Counter(target)
        scnts = [collections.Counter(s) & tcnt for s in stickers]
        for x in range(len(scnts) - 1, -1, -1):
            if any(scnts[x] & scnts[y] == scnts[x] for y in range(len(scnts) - 1, -1, -1) if x != y):
                scnts.pop(x)
        for status in range(1 << len(target)):
            if dp[status] < 0: continue
            for scnt in scnts:
                nstatus = status
                cnt = collections.Counter(scnt)
                for i, c in enumerate(target):
                    if cnt[c] > 0 and status & (1 << i) == 0:
                        nstatus |= (1 << i)
                        cnt[c] -= 1
                if dp[nstatus] < 0 or dp[nstatus] > dp[status] + 1:
                    dp[nstatus] = dp[status] + 1
        return dp[-1]


class Solution7:
    def minStickers(self, stickers, target):
        n_stickers = len(stickers)
        dp = [[[target]]*n_stickers for _ in range(len(target))]

        for i in range(len(target)):
            for k in range(n_stickers):
                res = set([])
                word = stickers[k]
                for j in range(n_stickers):
                    ws = dp[i-1][j]
                    for w in ws:
                        for s in word:
                            w = w.replace(s, '', 1)
                        if len(w) == 0:
                            return i+1
                        res.add(w)
                smallest_len_sofar = len(sorted(res, key=lambda x: len(x))[0])
                dp[i][k] = [x for x in res if len(x) == smallest_len_sofar]

        return -1


