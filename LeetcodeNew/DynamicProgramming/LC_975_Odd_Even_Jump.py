
"""
You are given an integer array A.  From some starting index, you can make a series of jumps.
The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps,
and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...),
you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.
If there are multiple such indexes j, you can only jump to the smallest such index j.
During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j
such that A[i] >= A[j] and A[j] is the largest possible value.
If there are multiple such indexes j, you can only jump to the smallest such index j.
(It may be the case that for some index i, there are no legal jumps.)
A starting index is good if, starting from that index,
you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)

Return the number of good starting indexes.



Example 1:

Input: [10,13,12,14,15]
Output: 2
Explanation:
From starting index i = 0, we can jump to i = 2 (since A[2]
is the smallest among A[1], A[2], A[3], A[4] that is greater or equal to A[0]),
then we can't jump any more.
From starting index i = 1 and i = 2, we can jump to i = 3, then we can't jump any more.
From starting index i = 3, we can jump to i = 4, so we've reached the end.
From starting index i = 4, we've reached the end already.
In total, there are 2 different starting indexes (i = 3, i = 4)
where we can reach the end with some number of jumps.
Example 2:

Input: [2,3,1,1,4]
Output: 3
Explanation:
From starting index i = 0, we make jumps to i = 1, i = 2, i = 3:

During our 1st jump (odd numbered), we first jump to i = 1
because A[1] is the smallest value in (A[1], A[2], A[3], A[4]) that is greater than or equal to A[0].

During our 2nd jump (even numbered), we jump from i = 1 to i = 2
because A[2] is the largest value in (A[2], A[3], A[4])
that is less than or equal to A[1].  A[3] is also the largest value,
but 2 is a smaller index, so we can only jump to i = 2 and not i = 3.

During our 3rd jump (odd numbered), we jump from i = 2 to i = 3
because A[3] is the smallest value in (A[3], A[4]) that is greater than or equal to A[2].

We can't jump from i = 3 to i = 4, so the starting index i = 0 is not good.

In a similar manner, we can deduce that:
From starting index i = 1, we jump to i = 4, so we reach the end.
From starting index i = 2, we jump to i = 3, and then we can't jump anymore.
From starting index i = 3, we jump to i = 4, so we reach the end.
From starting index i = 4, we are already at the end.
In total, there are 3 different starting indexes (i = 1, i = 3, i = 4) where we can reach the end with some number of jumps.
Example 3:

Input: [5,1,3,4,2]
Output: 3
Explanation:
We can reach the end from starting indexes 1, 2, and 4.


Note:

1 <= A.length <= 20000
0 <= A[i] < 100000
"""
"""
给定一个整数数组 A，你可以从某一起始索引出发，跳跃一定次数。
在你跳跃的过程中，第 1、3、5… 次跳跃称为奇数跳跃，而第 2、4、6… 次跳跃称为偶数跳跃。

你可以按以下方式从索引 i 向后跳转到索引 j（其中 i < j）：

在进行奇数跳跃时（如，第 1，3，5… 次跳跃），你将会跳到索引 j，使得 A[i] <= A[j]，A[j] 是可能的最小值。
如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。
在进行偶数跳跃时（如，第 2，4，6… 次跳跃），你将会跳到索引 j，使得 A[i] => A[j]，A[j] 是可能的最大值。
如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。
（对于某些索引 i，可能无法进行合乎要求的跳跃。）
如果从某一索引开始跳跃一定次数（可能是 0 次或多次），就可以到达数组的末尾（索引 A.length - 1），
那么该索引就会被认为是好的起始索引。

返回好的起始索引的数量。
"""
"""
We need to jump higher and lower alternately to the end.

Take [5,1,3,4,2] as example.

If we start at 2,
we can jump either higher first or lower first to the end,
because we are already at the end.
higher(2) = true
lower(2) = true

If we start at 4,
we can't jump higher, higher(4) = false
we can jump lower to 2, lower(4) = higher(2) = true

If we start at 3,
we can jump higher to 4, higher(3) = lower(4) = true
we can jump lower to 2, lower(3) = higher(2) = true

If we start at 1,
we can jump higher to 2, higher(1) = lower(2) = true
we can't jump lower, lower(1) = false

If we start at 5,
we can't jump higher, higher(5) = false
we can jump lower to 4, lower(5) = higher(4) = false
"""
"""
所以，我们可以看出，从后向前进行遍历，找出每个位置能不能跳到最终的位置。由于跳高、跳低是轮流的，
所以，当前的跳高跳低都要维护，而且分别后面一个跳低、跳高状态。

另外就是，这个题让我们找到最小或者最大的数字的位置，最简单的方法当然是查找，这里对查找的要求就大了。
如果是线性查找，那么时间复杂度是O(N)，同时由于不是有序的，所以不能二分。一个优化的策略就是C++的map，
和Java的TreeMap，即红黑树的实现版本。这个查找同样能达到O(NlogN)的时间复杂度。

定义了连个数组higher,lower分别表示当前位置开始跳高或者跳低能不能达到结尾。
定义了基于红黑树的m变量来保存每个数字的位置。对于每个位置都去查找就好了，由于题目限定的条件，
我们每次只会查找到一个确定的结果。对应的更新当前的跳高和跳低的状态。

注意，在C++中，lower_bound找到的是第一个满足条件的位置，而upper_bound指向的是第一个不满足的位置，
即[low, high)是满足条件的所有范围。

题外话：有没有感觉这个题像不像买卖股票问题？
"""
"""
public int oddEvenJumps(int[] A) {
    int n  = A.length, res = 1;
    boolean[] higher = new boolean[n], lower = new boolean[n];
    higher[n - 1] = lower[n - 1] = true;
    TreeMap<Integer, Integer> map = new TreeMap<>();
    map.put(A[n - 1], n - 1);
    for (int i = n - 2; i >= 0; --i) {
        Map.Entry hi = map.ceilingEntry(A[i]), lo = map.floorEntry(A[i]);
        if (hi != null) higher[i] = lower[(int)hi.getValue()];
        if (lo != null) lower[i] = higher[(int)lo.getValue()];
        if (higher[i]) res++;
        map.put(A[i], i);
    }
    return res;
}
"""

class SolutionLee:
    def oddEvenJumps(self, A):
        n = len(A)
        next_higher, next_lower = [0] * n, [0] * n

        stack = []
        for a, i in sorted([a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for a, i in sorted([-a, i] for i, a in enumerate(A)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        higher, lower = [0] * n, [0] * n
        higher[-1] = lower[-1] = 1
        for i in range(n - 1)[::-1]:
            higher[i] = lower[next_higher[i]]
            lower[i] = higher[next_lower[i]]
        return sum(higher)



class Solution2:
    def oddEvenJumps(self, A: 'List[int]') -> 'int':

        # sort indexes of A by values in A
        sorted_indexes = sorted(range(len(A)), key=lambda i: A[i])

        # generate list of indexes we can jump to next on odd jumps
        oddnext = self.makeStack(sorted_indexes)

        # sort indexes of A by reverse order of their value in A
        sorted_indexes.sort(key=lambda i: A[i], reverse=True)

        # generate list of indexes we can jump to next on even jumps
        evennext = self.makeStack(sorted_indexes)

        # initialize odd and even lists that will contain
        # the information of if the end can be reached
        # from the respective index
        odd = [False] * len(A)
        even = [False] * len(A)

        # the last index is always counted
        odd[len(A) - 1] = even[len(A) - 1] = True

        # iterate through A backwards, starting at next to last element
        for i in range(len(A) - 2, -1, -1):

            # if an odd jump is available from current index,
            # check if an even jump landed on the index of the available
            # odd jump and set current index in odd to True if it did
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]

            # if an even jump is available from current index,
            # check if an odd jump landed on the index of the available
            # even jump and set current index in even to True if it did
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        # return the number of spots marked True in odd
        # we always start with an odd jump, so odd will
        # contain the number of valid jumps to reach the end
        return sum(odd)

    # makes monotonic stack
    def makeStack(self, sorted_indexes):
        result = [None] * len(sorted_indexes)
        stack = []
        for i in sorted_indexes:
            while stack and i > stack[-1]:
                result[stack.pop()] = i
            stack.append(i)
        # delete stack as a memory optimization
        del stack
        return result

"""
给定一个整数数组 A，你可以从某一起始索引出发，跳跃一定次数。在你跳跃的过程中，第 1、3、5… 次跳跃称为奇数跳跃，而第 2、4、6… 次跳跃称为偶数跳跃。

你可以按以下方式从索引 i 向后跳转到索引 j（其中 i < j）：
在进行奇数跳跃时（如，第 1，3，5… 次跳跃），你将会跳到索引 j，使得 A[i] <= A[j]，A[j] 是可能的最小值。

如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。
在进行偶数跳跃时（如，第 2，4，6… 次跳跃），你将会跳到索引 j，使得 A[i] => A[j]，A[j] 是可能的最大值。

如果存在多个这样的索引 j，你只能跳到满足要求的最小索引 j 上。
（对于某些索引 i，可能无法进行合乎要求的跳跃。）

如果从某一索引开始跳跃一定次数（可能是 0 次或多次），就可以到达数组的末尾（索引 A.length - 1），那么该索引就会被认为是好的起始索引。

返回好的起始索引的数量。

示例 1：
输入：[10,13,12,14,15]
输出：2
解释：
从起始索引 i = 0 出发，我们可以跳到 i = 2，（因为 A[2] 是 A[1]，A[2]，A[3]，A[4] 中大于或等于 A[0] 的最小值），然后我们就无法继续跳下去了。
从起始索引 i = 1 和 i = 2 出发，我们可以跳到 i = 3，然后我们就无法继续跳下去了。
从起始索引 i = 3 出发，我们可以跳到 i = 4，到达数组末尾。
从起始索引 i = 4 出发，我们已经到达数组末尾。
总之，我们可以从 2 个不同的起始索引（i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。

示例 2：
输入：[2,3,1,1,4]
输出：3
解释：
从起始索引 i=0 出发，我们依次可以跳到 i = 1，i = 2，i = 3：
在我们的第一次跳跃（奇数）中，我们先跳到 i = 1，因为 A[1] 是（A[1]，A[2]，A[3]，A[4]）中大于或等于 A[0] 的最小值。
在我们的第二次跳跃（偶数）中，我们从 i = 1 跳到 i = 2，因为 A[2] 是（A[2]，A[3]，A[4]）中小于或等于 A[1] 的最大值。
A[3] 也是最大的值，但 2 是一个较小的索引，所以我们只能跳到 i = 2，而不能跳到 i = 3。
在我们的第三次跳跃（奇数）中，我们从 i = 2 跳到 i = 3，因为 A[3] 是（A[3]，A[4]）中大于或等于 A[2] 的最小值。
我们不能从 i = 3 跳到 i = 4，所以起始索引 i = 0 不是好的起始索引。
类似地，我们可以推断：
从起始索引 i = 1 出发， 我们跳到 i = 4，这样我们就到达数组末尾。
从起始索引 i = 2 出发， 我们跳到 i = 3，然后我们就不能再跳了。
从起始索引 i = 3 出发， 我们跳到 i = 4，这样我们就到达数组末尾。
从起始索引 i = 4 出发，我们已经到达数组末尾。
总之，我们可以从 3 个不同的起始索引（i = 1, i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。

示例 3：
输入：[5,1,3,4,2]
输出：3
解释：
我们可以从起始索引 1，2，4 出发到达数组末尾。

提示：

1 <= A.length <= 20000
0 <= A[i] < 100000
题意分析：
现在给定一个数组，让你从某个数开始向右移动，当前位置为i，移动规则如下：

第1,3,5,7…，次移动时，移动到所有不小于A[i]的数中的最小的数的位置
第2,4,6,8…，次移动时，移动到所有不大于A[i]的数中的最大的数的位置
若有多个位置满足，移动到最小index处。
思路分析：
对于任意一个位置i，这里使用odd[i]表示奇数次跳跃时下一个可以跳跃的位置，even[i]表示偶数次跳跃时下一个可以跳跃的位置。若无法跳跃，则值默认为-1。

可以保证，odd[i]和even[i]都是可以计算出来的某个确定的值，不存在能同时跳两个位置。
我们先思考这样一个问题，假设我们已经把odd数组和even数组计算出来了，如何去找最后的结果呢？
我们直接使用dfs去找，如果当前值为-1（代表已经无法跳跃），那么我们判断当前的index是否为终点。
如果dfs返回true，则说明该位置是一个good starting index。

"""

# Dynamic programming
class Solution3:
    def oddEvenJumps(self, A):

        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key=lambda i:A[i])
        oddnext = make(B)
        B = sorted(range(N), key=lambda i:-A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N - 1] = even[N - 1] = True
        for i in range(N - 2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]
        return sum(odd)


