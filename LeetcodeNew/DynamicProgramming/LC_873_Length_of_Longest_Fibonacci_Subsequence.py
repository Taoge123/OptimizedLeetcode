
"""
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence,
find the length of the longest fibonacci-like subsequence of A. If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A,
without changing the order of the remaining elements.
For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
"""
"""
Save array A to a hash set s.
Start from base (A[i], A[j]) as the first two element in the sequence,
we try to find the Fibonacci like subsequence as long as possible,

Initial (a, b) = (A[i], A[j])
While the set s contains a + b, we update (a, b) = (b, a + b).
In the end we update the longest length we find.

Time Complexity:
O(N^2logM), where M is the max(A).
"""
import collections

class SolutionLee1:
    def lenLongestFibSubseq(self, A):
        s = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b = A[i], A[j]
                l = 2
                while a + b in s:
                    a, b = b, a + b
                    l += 1
                res = max(res, l)
        return res if res > 2 else 0


"""
Another solution is kind of dp.
dp[a, b] represents the length of fibo sequence ends up with (a, b)
Then we have dp[a, b] = (dp[b - a, a] + 1 ) or 2
The complexity reduce to O(N^2).
In C++/Java, I use 2D dp and index as key.
In Python, I use value as key.

Time Complexity:
O(N^2)
"""
class SolutionLee2:
    def lenLongestFibSubseq(self, A):
        dp = collections.defaultdict(int)
        s = set(A)
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
        return max(dp.values() or [0])


"""
DP[i][j] means the result of index from (0, ... i, j)

The default value of DP is 2 because the case of subarray [i, j]. (of course 2 is invalid answer, 
we should update the result only if the length of subsequence is greater then 2)

We should check every pair (i, j) such that 0<i<j<length(A) to find DP[i][j].

Let's find the DP[i][j] as following.

DP[i][j] should be the result of DP[k][i]+1, such k is Array index of X that satisfies the following condition.

(X < A[i]), (X in A) and (X + A[i] = A[j])
and, both to check that X is in A and find the array index of X, we can store the value-index by using dictionary, 
only if index is less then i (because X < A[i]). this is idx dict.

Time complexity : O(N^2)
Space complexity : O(N) ( we store only if (i,j) satisfy the condition. 
Simply, think about that fix the i and if there are M pair (i, j) combinations to store, 
then there are also M number of another value k in A, so M is included in N)
"""

class Solution1:
    def lenLongestFibSubseq(self, A):
        dp = collections.defaultdict(lambda : 2)
        ret, idx = 0, { A[0] : 0 }
        for i in range(1, len(A)-1):
            idx[A[i]] = i
            for j in range(i+1, len(A)):
                x = A[j] - A[i]
                if x >= A[i] :
                    break
                elif x not in idx:
                    continue
                dp[i,j] = dp[idx[x], i] + 1
                ret = max(ret, dp[i,j])
        return ret


"""
The DP formula is straight forward. dp[i][j] represents the LFS ending at i and j, where i < j.
for j=[0..n], i=[0..j-1], dp[i][j] = max(dp[i][j], 1+dp[k][i]), where k=[0..i-1] if A[k]+A[i]=A[j].
"""
class Solution2:
    def lenLongestFibSubseq(self, A: 'List[int]') -> 'int':
        n = len(A)
        dp = [[2 for _ in range(n+1)] for _ in range(n+1)]
        for j in range(n):
            for i in range(j):
                for k in range(i):
                    if A[k]+A[i] == A[j]:
                        dp[i][j] = max(dp[i][j], 1+dp[k][i])
        ans = max([max(n) for n in dp])
        return 0 if ans <= 2 else ans

"""
分析：

对于这种找子串的问题，大家应该敏感一点，虽然不说绝对，但是极大可能是dp，在这里写一下我分析这道题的心路历程
第一反应，dp[i]表示nums[:i]的最长fiboc序列长度。但仔细想想dp[i]只记录长度，
我根本没法去判断nums[i]能否组出一个更长的序列，那用dp[i]记录下一个期望的数（序列中最后两个数的和）？
但是就想example2一样，首先可能会有很多期望的值，
其次，可能最后最长的那个序列在最初分析数组前几个数时根本不包括其中，所以这个方法应该是行不通。
第二反应，发现A的长度不超过1000，这不是暗示我n^2的方法嘛，一想dp[i][j]表示nums[i:j]的最长fibco序列长度，
乍一看好像可行诶，首先可以初始化，因为j-i<2则dp[i][j] = 0，所有的j-i=2都可以判断出来（因为就三个数），
对于j-i>2，可以依次分析dp[i][i+2],dp[i][i+3]…dp[i][j-1]与nums[j]能否构成更长的序列，
取最长的那个保存，但想到这里的时候，发现这个方法复杂度好像有点高哦，达到n^3了，
想了一会也没想到怎么优化，而且也还是会面临第2点中说的第一个问题，遂放弃。
第三反应，逆向思维一下，像上面两个方法都是判断最后一个数能不能和前面的组成更长的序列，
那为什么不固定住最后的序列，去找前面的序列呢(这个思维正好把第2点中提到的那个“其次”解决了)，
dp[i][j]表示以nums[i]和nums[j]结尾的fibco序列的最长长度，则dp[i][j] = dp[nums[j]-nums[i]的index][i] + 1，
当然这必须要满足nums[j]-nums[i]在A中
思路：

用一个字典保存值和下标的对应关系，用于获得nums[j]-nums[i]的index
集合记录A（有序）中元素，判断nums[j]-nums[i]是否在A中
这一点inspired by @lee215，判断nums[j]-nums[i] < nums[i] and nums[j]-nums[i] in s，
可以避免重复计算
inspired by @lee215，可以用值来代替下标(python版本，它的C++版本是用的我上面说的思路，
这么一看python实在太方便了)，可以让代码简洁很多（这是真的大神！！！）
"""

class Solution3:
    def lenLongestFibSubseq(self, A):
        dp = collections.defaultdict(int)
        s = set(A)
        res = 0
        for j in range(len(A)):
            for i in range(j):
                if A[j] - A[i] < A[i] and A[j] - A[i] in s:
                    dp[A[i], A[j]] = dp.get((A[j] - A[i], A[i]), 2) + 1
                    res = max(res, dp[A[i], A[j]])
        return max(dp.values() or [0])


"""
解题方法
使用最简单的方法竟然也能过。只需要双重循环，循环的含义是找出以这两个元素为起始点的费布拉奇数列。
然后继续向后面遍历，使用set用O(1)的时间复杂度来查找下面的一个费布拉奇数字是否在set之中，
然后继续再找下一个费布拉奇数字即可。

费布拉奇数字计算的时间复杂度接近于O(logM)，M代表数组A中的最大值。所以整个时间复杂度是O(n^2 * longM)。
"""
class Solution4:
    def lenLongestFibSubseq(self, A):

        s = set(A)
        n = len(A)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                count = 2
                while a + b in s:
                    a, b = b, a + b
                    count += 1
                    res = max(res, count)
        return res if res > 2 else 0



"""
DP.

使用一维DP解决不了这个问题，因为一维DP只保存了到某个为止的最长费布拉奇数列，
但是新的数字到来之后能不能满足之前的费布拉奇数列是未知的。所以使用二维DP.

这个DP[i][j]数组的含义是，以i和j为结尾两个数字的费布拉奇数列长度（i < j）
因此，转移方程可以这么写：

dp[j][k] = dp[i][j] + 1 
条件是 A[i] + A[j] = A[k]。

我们求解的过程是用j,k去遍历，然后查找满足条件的i。

使用字典保存每个数字和其下标的对应值，能用O(1)的时间复杂度求出i。

题目要求的结果是整个dp的最大值。

另外，如果出现A[i] >= A[j]直接break内层循环，因为我们指定了i < j。

这个题和一般dp不同的是，普通的dp的下标转移方程是固定的，而这个题需要我们先找出之前的i坐标，然后才去更新dp值。

这个算法的时间复杂度是O(n^2)，空间复杂度是O(n^2).
"""

class Solution5:
    def lenLongestFibSubseq(self, A):

        n = len(A)
        m = dict()
        for i, a in enumerate(A):
            m[a] = i
        res = 0
        # dp[i][j] := max len of seq ends with A[i], A[j]
        dp = [[2 for i in range(n)] for j in range(n)]
        for j in range(n):
            for k in range(j + 1, n):
                a_i = A[k] - A[j]
                if a_i >= A[j]:
                    break
                if a_i in m:
                    i = m[a_i]
                    dp[j][k] = dp[i][j] + 1
                    res = max(res, dp[j][k])
        return res



class Solution6:
    def lenLongestFibSubseq(self, A):

        vset = set(A)
        dp = collections.defaultdict(lambda: collections.defaultdict(int))
        size = len(A)
        ans = 0
        for i in range(size):
            x = A[i]
            for j in range(i + 1, size):
                y = A[j]
                if x + y not in vset: continue
                dp[y][x + y] = max(dp[y][x + y], dp[x][y] + 1)
                ans = max(dp[y][x + y], ans)
        return ans and ans + 2 or 0

