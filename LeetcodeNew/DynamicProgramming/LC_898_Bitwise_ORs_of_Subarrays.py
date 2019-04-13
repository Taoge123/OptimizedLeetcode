
"""
https://www.geeksforgeeks.org/sum-of-bitwise-or-of-all-possible-subsets-of-given-set/
https://blog.csdn.net/fuxuemingzhu/article/details/83511833
https://zhanghuimeng.github.io/post/leetcode-898-bitwise-ors-of-subarrays/

We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j),
we take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

Example 1:

Input: [0]
Output: 1
Explanation:
There is only one possible result: 0.
Example 2:

Input: [1,1,2]
Output: 3
Explanation:
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: [1,2,4]
Output: 6
Explanation:
The possible results are 1, 2, 3, 4, 6, and 7.


Note:

1 <= A.length <= 50000
0 <= A[i] <= 10^9

"""

"""
Intuition

Let's try to speed up a brute force answer. Evidently, 
the brute force approach is to calculate every result result(i, j) = A[i] | A[i+1] | ... | A[j]. 
We can speed this up by taking note of the fact that result(i, j+1) = result(i, j) | A[j+1]. 
Naively, this approach has time complexity O(N^2)O(N 2 ), where NN is the length of the array.

Actually, this approach can be better than that. At the kth step, say we have all the result(i, k) in some set cur. 
Then we can find the next cur set (for k -> k+1) by using result(i, k+1) = result(i, k) | A[k+1].

However, the number of unique values in this set cur is at most 32, 
since the list result(k, k), result(k-1, k), result(k-2, k), ... is monotone increasing, 
and any subsequent values that are different must have more 1s in it's binary representation (to a maximum of 32 ones).

Algorithm

In the kth step, we'll maintain cur: the set of results A[i] | ... | A[k] for all i. 
These results will be included in our final answer set.
"""
"""
Intuition:
Assume B[i][j] = A[i] | A[i+1] | ... | A[j]
Hash set cur stores all wise B[0][i], B[1][i], B[2][i], B[i][i].

When we handle the A[i+1], we want to update cur
So we need operate bitwise OR on all elements in cur.
Also we need to add A[i+1] to cur.

In each turn, we add all elements in cur to res.

Time Complexity:
O(30N)

Normally this part is easy.
But for this problem, time complexity matters a lot.

The solution is straight forward,
while you may worry about the time complexity up to O(N^2)
However, it's not the fact.
This solution has only O(30N)

The reason is that, B[0][i] >= B[1][i] >= ... >= B[i][i].
B[0][i] covers all bits of B[1][i]
B[1][i] covers all bits of B[2][i]
....

There are at most 30 bits for a positive number 0 <= A[i] <= 10^9.
So there are at most 30 different values for B[0][i], B[1][i], B[2][i], ..., B[i][i].
Finally cur.size() <= 30 and res.size() <= 30 * A.length()

In a worst case, A = {1,2,4,8,16,..., 2 ^ 29}
And all B[i][j] are different and res.size() == 30 * A.length()
"""
class SolutionLee:
    def subarrayBitwiseORs(self, A):
        res, cur = set(), set()
        for i in A:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)

class Solution1:
    def subarrayBitwiseORs(self, A):

        ORs = set()
        queue = set()
        for a in A:
            queue = {q|a for q in queue}
            queue.add(a)
            ORs |= queue
        return len(ORs)


"""
There are O(n²) possible sets. A brute force algorithm that checks each of these sets would be O(n³), 
or O(n²) with a few optimisations. However, this isn't fast enough. 
The question is then... how can we do less doubling up of work?

One way is to go through the array once, attempting to OR the current number with all subsets that included the number before it. 
The number of subsets in the previous number isn't n, 
it's actually never going to be bigger than the number of bits in the largest numbers of the array. 
This is because each step we go back from the previous number could add at least one more bit in, or none at all. It's impossible to subtract them.

For example, let's say we have the following (5 bit) numbers:
[4, 5, 10, 2, 16, 4, 5, 2, 1, 3]
In binary, these are:
[00100, 00101, 01010, 00010, 10000, 00100, 00101, 00010, 00001, 00011].

The last number in the list is 00011. Let's look at what happens when we make increasingly larger sublists 
with the numbers before it and get the result of OR'ing all those numbers.

[00011] ==> 00011
[00001, 00011] ==>  00011
[00010, 00001, 00011]  ==>  00011
[00101, 00010, 00001, 00011] ==>  00111
[00100, 00101, 00010, 00001, 00011] ==>  00111
[10000, 00100, 00101, 00010, 00001, 00011] ==> 10111
[00010, 10000, 00100, 00101, 00010, 00001, 00011] ==> 10111
[01010, 00010, 10000, 00100, 00101, 00010, 00001, 00011] ==> 11111
[00101, 01010, 00010, 10000, 00100, 00101, 00010, 00001, 00011] ==> 11111
[00100, 00101, 01010, 00010, 10000, 00100, 00101, 00010, 00001, 00011] ==> 11111
Notice how a lot of these are the same? Once a bit appears in a particular position, 
it's impossible for it to disappear! What this means, is that we only need to OR the last number with previous ones that are actually unique. 
This is proportional to the number of bits in the largest number rather than n. That is, it's a lot smaller!

So, for each number in the array, we start with a set containing just that number 
(because that's what we'd get OR'ing it with itself). We then add all the possibilities 
we can get by OR'ing the number with results that include the previous number.

And here's an algorithm that uses that idea.
"""
class Solution2:
    def subarrayBitwiseORs(self, A):
        # Tabulation is a list of sets, one for each number in A.
        # Each set, at position i, is initialised to containing the element at A[i]
        tabulation = [set([A[i]]) for i in range(len(A))]

        # And now we need to go through, updating the sets based on the previous set.
        for i in range(1, len(A)):
            for previous_result in tabulation[i - 1]:
                tabulation[i].add(A[i] | previous_result)

                # Return the number of unique numbers in the tabulation list.
        return len(set.union(*tabulation)) if len(A) > 0 else 0

# Naive solution
class Solutio3:
    def subarrayBitwiseORs(self, A):
        nums, n = set(), len(A)
        for i in range(n):
            num = A[i]
            for j in range(i, n):
                num |= A[j]
                nums.add(num)
        return len(nums)

"""
Naive solution gets TLE due to O(N^2) runtime
We can do bitwise ORs of current number {a} in array with previous results {pre} whose subarrays end with previous index
Also current number {a} can start new result array, so previous results {pre} become current number {a} 
and bitwise ORs of current number {a} with previous results {pre}
"""
class Solution4:
    def subarrayBitwiseORs(self, A):
        nums, n, pre = set(), len(A), set()
        for a in A:
            pre = {a} | {num | a for num in pre}
            nums |= pre
        return len(nums)

# More readable my contest solution
class Solution5:
    def subarrayBitwiseORs(self, A):
        nums, n, pre = set(), len(A), set()
        for i in range(n):
            new = {A[i]}
            for num in pre:
                new |= {num|A[i]}
            pre = new
            nums |= pre
        return len(nums)


"""
for each index j I computed all
a[j]
a[j-1] | a[j]
a[j-2] | a[j-1] | a[j]
...
a[0] | a[1] | ... | a[j-2] | a[j-1] | a[j]

for j in range(len(A)):
	compute all 
	and keep track of this in an ongoing set , I call it og 
	hs is the hashset that keeps track of all the elementss that I ve seen so far 
	hs |=  og

"""

"""
题目大意
一个数组的所有子数组的异或结果，总共有多少个不同？

解题方法
动态规划
题目不是一般的难啊，如果是普通的DP方法，那么使用二维dp[i][j]表示子数组的起始和结束区间，能做到O(n^2)的时间复杂度，
但是题目对时间复杂度要求的很死，必须O(N).

正确的做法也是动态规划，dp[i]表示以A[i]结尾的所有子数组的异或结果，其实是个set。

转移方程式dp[i] = [b | A[i] for b in dp[i - 1]] + A[i]，
即以A[i]结尾的所有子数组异或结果等于以A[i-1]结尾的所有子数组异或结果，和当前的A[i]异或，再加上A[i]这个结果。

同时使用一个set保存所有的异或结果。最后返回这个结果set的长度。


dp[i]的大小至多是32个，即 |dp[i]| <= 32 的证明：

dp[i] = {A[i], A[i] | A[i - 1], A[i] | A[i - 1] | A[i - 2], … , A[i] | A[i - 1] | … | A[0]}，
这个序列单调递增，通过把A[i]中的0变成1。A[i]最多有32个0。所以这个集合的大小 <= 32。

举例：最坏情况 A = [8, 4, 2, 1, 0] 都是2^k。
A[5] = 0，dp[5] = {0, 0 | 1, 0 | 1 | 2, 0 | 1 | 2 | 4, 0 | 1 | 2 | 4 | 8} = {0, 1, 3, 7, 15}.

时间复杂度是O(32*N)，空间复杂度是O(32N).
"""
class Solution11:
    def subarrayBitwiseORs(self, A):

        res = set()
        cur = set()
        for a in A:
            cur = {n | a for n in cur} | {a}
            res |= cur
        return len(res)


"""
分析
我也不知道这道题做了多久，总之首先就看错题了（把“或”看成了“异或”），做出来是不太可能的了。
其次当时Leetcode服务器大概比较爆炸，平均5分钟才能运行一次。

记数组为A，显然我们的目标就是求出所有or(i, j) = A[i] | ... | A[j] (i <= j)的可能取值。
如果直接暴力计算，则复杂度为O(N^3)。一个显而易见的优化是，对于当前的j，我们可以维护一个数组，
其中保存了所有以j结尾的子序列的取值；or(0, j), or(1, j), ..., or(j, j)的值；对于j+1，
我们可以通过这些值递推出所有以j+1结尾的子序列的取值：
or(0, j+1)=or(0, j)|A[j+1], or(1, j+1)=or(1, j)|A[j+1], ... or(j, j+1)=or(j, j)|A[j+1], or(j+1, j+1)=A[j+1]。
于是复杂度降低到O(N^2)。

（也许我可以推导到这一步，但是后来我信心丧失直接去看题解了）

然后是一个信仰之跃：我们要利用一下或操作的性质，在一个或和中不断或上新的数值，其二进制表示中1的数量不会减少。
刚才维护的子序列除了能够递推之外，还满足一个很好的性质：
or(0, j) = or(1, j) | A[0] = ... = or(j, j) | A[0] | A[1] | .. | A[j-1]；
因此，cnt1(or(0, j)) >= cnt1(or(1, j)) >= ... >= cnt1(or(j, j))，且同一位置上的1出现后就不会消失。
而题目给定了0 <= A[i] <= 10^9，所以这些数的二进制位最多只有30个。

这也就说明，以j结尾的所有子序列的或和的取值最多只有30种。

所以只需把上述保存以j结尾的子序列的或和的数组改成HashSet，然后维护这个HashSet中的值，就可以得到O(30N)的复杂度。
"""

class Solution22:
    def subarrayBitwiseORs(self, A):

        result, curr = set(), {0}
        for i in A:
            curr = {i} | {i | j for j in curr}
            result |= curr
        return len(result)



