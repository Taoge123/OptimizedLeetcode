
"""
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/119830/Python-14-line-O(1)-space-O(n)-time-DP-solution
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/discuss/161887/Bottom-up-DP-with-Optimization-(Java-Python)
http://www.cnblogs.com/grandyang/p/9311385.html
https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/


We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].
Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.
(A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
It is guaranteed that the given input always makes it possible.

Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation:
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
Note:

A, B are arrays with the same length, and that length will be in the range [1, 1000].
A[i], B[i] are integer values in the range [0, 2000].

"""

"""
Approach #1: Dynamic Programming [Accepted]
Intuition

The cost of making both sequences increasing up to the first i columns 
can be expressed in terms of the cost of making both sequences increasing up to the first i-1 columns. 
This is because the only thing that matters to the ith column is whether the previous column was swapped or not. 
This makes dynamic programming an ideal choice.

Let's remember n1 (natural1), the cost of making the first i-1 columns increasing and not swapping the i-1th column; 
and s1 (swapped1), the cost of making the first i-1 columns increasing and swapping the i-1th column.

Now we want candidates n2 (and s2), the costs of making the first i columns increasing 
if we do not swap (or swap, respectively) the ith column.

Algorithm

For convenience, say a1 = A[i-1], b1 = B[i-1] and a2 = A[i], b2 = B[i].

Now, if a1 < a2 and b1 < b2, then it is allowed to have both of these columns natural (unswapped), 
or both of these columns swapped. This possibility leads to n2 = min(n2, n1) and s2 = min(s2, s1 + 1).

Another, (not exclusive) possibility is that a1 < b2 and b1 < a2. 
This means that it is allowed to have exactly one of these columns swapped. 
This possibility leads to n2 = min(n2, s1) or s2 = min(s2, n1 + 1).

Note that it is important to use two if statements separately, because both of the above possibilities might be possible.

At the end, the optimal solution must leave the last column either natural or swapped, 
so we take the minimum number of swaps between the two possibilities.
"""
import sys

class Solution1:
    def minSwap(self, A, B):
        n1, s1 = 0, 1
        for i in xrange(1, len(A)):
            n2 = s2 = float("inf")
            if A[i-1] < A[i] and B[i-1] < B[i]:
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)
            if A[i-1] < B[i] and B[i-1] < A[i]:
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)

            n1, s1 = n2, s2

        return min(n1, s1)


"""
This problem can be solved using dynamic programming, at each position, we can choose to swap or not. 
Since we want two sorted arrays, at each position, 
whether to swap or not depends on the choice at previous position, so we can form a recursive formula.

N = len(A)
dp = [[maxint]*2 for _ in range(N)]
Let initialize a N*2 array dp,

dp[i][0] means the least swaps used to make A[:i+1] and B[:i+1] sorted having no swap at i-th position.
dp[i][1] means the least swaps used to make A[:i+1] and B[:i+1] sorted having swap at i-th position.
Picture explanation:

Here is the recursive formula:

There are two cases that can make the two arrays sorted:

A . B
C . D
Here our cases are A<B and C<D and A<D and C<B.

Because the possible combination to be sorted are only A B in array1 C D in array2 or A D in array1 C B in array2, 
so only the 2 cases, and they can holds at the same time: for example A=1, B=2, C=1, D=2. 
If both don't hold, swapping can't make them in order.

For $i in [1, N]$:

If A[i]>A[i-1] and B[i]>B[i-1] (they are in order without swap):
dp[i][0]=min(dp[i][0], dp[i-1][0]) (no swap at i-1 and no swap at i)
dp[i][1]=min(dp[i][1], dp[i-1][1]+1) (swap at i-1 so swap at i to make in order)

If A[i]>B[i-1] and B[i]>A[i-1] (they are in order with a swap):
dp[i][0]=min(dp[i][0], dp[i-1][1]) (swap at i-1, no need to swap at i)
dp[i][1]=min(dp[i][1], dp[i-1][0]+1) (no swap at i-1, so swap at i)

The two cases don't conflict with each other, so we choose minimum of them when both holds.

What we want to return is min(dp[N-1][0], dp[N-1][1]).

At every recursion, we only need the last result, so we can use less space, from O(N) to O(1), time complexity O(N).

20-Line Python Solution：
"""
class Solution2:
    def minSwap(self, A, B):

        n = len(A)
        pre = [0, 1]
        for i in range(1, n):
            cur = [sys.maxsize, sys.maxsize]
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                cur[0] = min(cur[0], pre[0])
                cur[1] = min(cur[1], pre[1] + 1)
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                cur[0] = min(cur[0], pre[1])
                cur[1] = min(cur[1], pre[0] + 1)
            pre = cur
            return min(pre)

"""
swap[n] means the minimum swaps to make the A[i] 
and B[i] sequences increasing for 0 <= i <= n in condition that we swap A[n] and B[n]
not_swap[n] is the same with A[n] and B[n] not swapped.

In case that (A[i - 1] < B[i] && B[i - 1] < A[i]).
If A[i-1] and B[i-1] are swapped, we don't need to swap A[i] and B[i].
Otherwise, we need to swap A[i] and B[i].

"""
class Solution3:
    def minSwap(self, A, B):
        N = len(A)
        not_swap, swap = [N] * N, [N] * N
        not_swap[0], swap[0] = 0, 1
        for i in range(1, N):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                not_swap[i] = not_swap[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                not_swap[i] = min(not_swap[i], swap[i - 1])
                swap[i] = min(swap[i], not_swap[i - 1] + 1)
        return min(swap[-1], not_swap[-1])


"""
if (A[i - 1] < B[i] && B[i - 1] < A[i]) {
                not_swap[i] = Math.min(not_swap[i], swap[i - 1]);
                swap[i] = Math.min(swap[i], not_swap[i - 1] + 1);
            }
            
This case we need to either swap the current i element or i-1 element. 
Here not_swap[i] stands for not swapping A[i] and B[i]. So, we need to swap i-1.
If we swap[i], we don't need to swap i-1, hence not_swap[i - 1] + 1(for current swapping)
"""
"""
state	
whether we swap the element at index i to make A[0..i] 
and B[0..i] both increasing can uniquely identify a state, i.e. a node in the state graph.
state function	
state(i, 0) is the minimum swaps to make A[0..i] and B[0..i] both increasing if we donot swap A[i] with B[i]
state(i, 1) is the minimum swaps to make A[0..i] and B[0..i] both increasing if we do swap A[i] with B[i]
goal state	
min{state(n - 1, 0), state(n - 1, 1)} where n = A.length
state transition	
We define areBothSelfIncreasing: A[i - 1] < A[i] && B[i - 1] < B[i], areInterchangeIncreasing: A[i - 1] < B[i] && B[i - 1] < A[i].
Since 'the given input always makes it possible', at least one of the two conditions above should be satisfied.

if i == 0, 
	        state(0, 0) = 0; 
	        state(0, 1) = 1;
			
Generally speaking,
	if areBothSelfIncreasing && areInterchangeIncreasing
	        // Doesn't matter whether the previous is swapped or not.
	        state(i, 0) = Math.min(state(i - 1, 0), state(i - 1, 1));
	        state(i, 1) = Math.min(state(i - 1, 0), state(i - 1, 1)) + 1;
	else if areBothSelfIncreasing
	        // Following the previous action.
	        state(i, 0) =  state(i - 1, 0);
	        state(i, 1) =  state(i - 1, 1) + 1;
	else if areInterchangeIncreasing
	        // Opposite to the previous action.
	        state(i, 0) = state(i - 1, 1);
	        state(i, 1) = state(i - 1, 0) + 1;
"""


"""
Best explanation so far, appreciate!
so based on my understanding, we have three cases in total:

case 1 : if (A[i - 1] < A[i] && B[i - 1] < B[i] && A[i - 1] < B[i] && B[i - 1] < A[i])
means A[i - 1, i] and B[i - 1, i] are sorted, and we can swap to keep the sorted status
so we can do nothing state[i][0] = Math.min(state[i - 1][0], state[i - 1][1]) or swap state[i][1] = Math.min(state[i - 1][0], state[i - 1][1]) + 1

case 2 :else if (A[i - 1] < A[i] && B[i - 1] < B[i])
means A[i - 1, i] and B[i -1, i] are sorted while if we swap , the sorted status may be broken
so we better do nothing state[i][0] = state[i - 1][0], or if we have swapped before, then we will have swap once more state[i][1] = state[i - 1][1] + 1.

case 3 :else if (A[i - 1] < B[i] && B[i - 1] < A[i])
means A[i - 1, i] or B[i -1, i] are nor sorted(maybe both not sorted), while we can swap to make it sorted again.
if we have swapped before, then we do not need to swap state[i][0] = state[i - 1][1], otherwise we have to swap state[i][1] = state[i - 1][0] + 1.
"""
class Solution4:
    def minSwap(self, A, B):
        n = len(A)
        prevNotSwap = 0
        prevSwap = 1
        for i in range(1, n):
            areBothSelfIncreasing = A[i - 1] < A[i] and B[i - 1] < B[i]
            areInterchangeIncreasing = A[i - 1] < B[i] and B[i - 1] < A[i]
            if areBothSelfIncreasing and areInterchangeIncreasing:
                newPrevNotSwap = min(prevNotSwap, prevSwap)
                prevSwap = min(prevNotSwap, prevSwap) + 1
                prevNotSwap = newPrevNotSwap
            elif areBothSelfIncreasing:
                prevSwap += 1
            else: # if areInterchangeIncreasing:
                newPrevNotSwap = prevSwap
                prevSwap = prevNotSwap + 1
                prevNotSwap = newPrevNotSwap
        return min(prevNotSwap, prevSwap)


class Solution5:
    def minSwap(self, A, B):
        d, p = 0, 1 # rolling arrays: d: the min exhangements so far when i is fixed; p: the min exchangements so far when i is exchanged.
        for i in range(1, len(A)):
            u, v = d, d + 1 # temp vars for d and p respectively, min exchangements at i (d and p are at (i - 1)).
            # case 0: i is fixed:
            if A[i] > A[i - 1] and B[i] > B[i - 1]: # u has default value d
                if A[i] > B[i - 1] and B[i] > A[i - 1] and d > p: u = p
            else: u = p # (i - 1) must exchange.
            # case 1: i is exchanged:
            if A[i] > B[i - 1] and B[i] > A[i - 1]: # v has default value (d + 1)
                if A[i] > A[i - 1] and B[i] > B[i - 1] and d > p: v = p + 1
            else: v = p + 1 # (i - 1) must exchange.
            d, p = u, v
        return min(d, p)


class Solution6:
    def minSwap(self, A, B):
        swap = [0, 1]
        for i in range(1, len(A)):
            if A[i] > A[i - 1] and B[i] > B[i - 1] and A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap = [min(swap), min(swap) + 1]
            elif A[i] > A[i - 1] and B[i] > B[i - 1]:
                swap[1] += 1
            else:
                swap = [swap[1], swap[0] + 1]
        return min(swap)


"""
思路：

我们定义dp1[i]表示在不交换A[i]和B[i]的情况下，使得A的前i + 1个元素和B的前i + 1个元素严格递增的最小交换次数；
定义dp2[i]表示在交换A[i]和B[i]的情况下，使得A的前i + 1个元素和B的前i + 1个元素严格递增的最小交换次数。
那么递推可以分为两种可能性（由于题目保证一定有正确答案，所以以下两种可能性会至少满足一个，也有可能两个都满足）：

1）A[i] > A[i - 1] && B[i] > B[i - 1]：这说明在维持第i对元素和第i - 1对元素同序的情况下可以满足条件，
所以我们可以让dp1[i]和dp2[i]分别从INT_MAX降低到dp1[i - 1]和dp2[i - 1] + 1，也就是如果A[i - 1]和B[i - 1]交换了，
那么我们也让A[i]和B[i]也交换；如果A[i - 1]和B[i - 1]维持原序，那么我们也让A[i]和B[i]维持原序。

2）B[i] > A[i - 1] && A[i] > B[i - 1]：这说明维护第i对元素和第i - 1对元素反序的情况下也可以满足条件，
所以我们就看看能不能进一步降低dp1[i]和dp2[i]的数组：如果dp2[i - 1] < dp[i]，那么说明交换第i - 1对元素之后，
保持第i对元素的次序可以达到更优解；如果dp1[i - 1] + 1 < dp2[i]，那么说明在维持第i - 1对元素的次序的情况下，交换第i对元素可以达到更优解。

算法的时间复杂度和空间复杂度都是O(n)，不过我们发现dp1[i]和dp2[i]都只和dp1[i - 1]，dp2[i - 1]有关，
所以还可以将空间复杂度进一步降低到O(1)，读者可以自行实现。
"""
"""
题目大意
一个字符串中有0有1，问最少翻转多少个字符能够使得这个字符串编程一个单调递增的字符串。

解题方法
动态规划
这个题和周赛926. Flip String to Monotone Increasing基本一模一样，如果我早点把这个题搞明白的话，
周赛的926应该也能做出来了。926题我写的非常的详细，是我写的最认真的一次，强烈建议看下926题的动态规划部分。

我是看了画画酱的讲义的，如下图。这个题也是需要做交换，可以定义两个数组keep和swap，
这两个数组的含义是我们交换或者不交换第i个位置使得两个数组都保持严格的单调递增需要进行的交换数量。

那么，当A[i] > A[i - 1] and B[i] > B[i - 1]时，我们可以不交换当前的数字，这个时候前面的数字也不能交换；
也可以交换当前的数字，同时需要把前面的数字也进行交换。即，这种情况下，前面的位置和现在的位置做的是同样的交换。

在做了上面的操作之后，我们得到的仍然是有序的部分，但是没有结束，
因为我们可能还会出现A[i] > B[i - 1] and B[i] > A[i - 1]这种交叉的情况。这个时候考虑前面的位置和现在的位置做相反的交换。

当A[i] > B[i - 1] and B[i] > A[i - 1]时，我们如果不交换当前的数字，同时对前面的位置强制交换，
判断交换后的次数是不是比当前的交换次数少；如果我们交换这个位置，同时强制前面的数字不交换，
那么当前的交换次数应该是前面不交换的次数+1和当前交换次数的最小值。

上面两种判断并不是if-else的关系，因为，这两种情况同时存在。我们通过这两种情况，考虑了4种情况：
当前位置换、不换与前面的位置换、不换的组合。注意第二个判断里面求最小值是相对于自身做比较的，
因为我们不一定需要对前面的位置进行操作

另外，需要注意的是，一般情况的dp初始化都是0或者1，但是这个题需要求最小值，其实已经提醒我们不是0或者1.实际上，
需要使用无穷大表示初始情况下，还没有做翻转操作时交换次数应该是无穷多。而不是0表示初始情况下不用交换就能到达有序。

时间复杂度是O(N)，空间复杂度是O(N).
"""
class Solution7:
    def minSwap(self, A, B):

        N = len(A)
        keep = [float('inf')] * N
        swap = [float('inf')] * N
        keep[0] = 0
        swap[0] = 1
        for i in range(1, N):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)
        return min(keep[N - 1], swap[N - 1])


# 这个题如果改成和926题一样的二维数组的dp的话，应该这么写，其实和上面的做法没有任何区别。
class Solution8:
    def minSwap(self, A, B):

        N = len(A)
        dp = [[float('inf'), float('inf')] for _ in range(N)]
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, N):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1] + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                dp[i][0] = min(dp[i][0], dp[i - 1][1])
                dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)
        return min(dp[N - 1][0], dp[N - 1][1])


"""
显然，上面的做法中，每次dp转移操作只和前面的一个状态有关，所以，可以优化空间复杂度到O(1)。对于每次
"""
class Solution9:
    def minSwap(self, A, B):

        N = len(A)
        keep, swap = 0, 1
        for i in range(1, N):
            curswap, curkeep = float('inf'), float('inf')
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                curkeep, curswap = keep, swap + 1
            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                curkeep, curswap = min(curkeep, swap), min(curswap, keep + 1)
            keep, swap = curkeep, curswap
        return min(keep, swap)

"""
解题思路：
动态规划（Dynamic Programming）

swap和keep分别记录A[i]与B[i]交换或者不交换时的最小代价
分三种情况讨论：

A[i]与B[i]必须交换
A[i]与B[i]可以交换也可以保持原状
A[i]与B[i]必须保持原状
"""
class Solution10:
    def minSwap(self, A, B):

        swap, keep = 1, 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1] or B[i] <= B[i - 1]:
                # swap
                nswap = keep + 1
                nkeep = swap
            elif A[i] > B[i - 1] and B[i] > A[i - 1]:
                # swap or keep
                nkeep = min(keep, swap)
                nswap = nkeep + 1
            else:
                # keep
                nkeep = keep
                nswap = swap + 1
            swap, keep = nswap, nkeep
        return min(swap, keep)



