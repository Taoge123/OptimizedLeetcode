
"""

[6 5 4 3 2 1 ] 4

[6 5 4] 5


"""

"""
解法1
比赛的时候，比较容易想到的是o(NlogN)的解法。

遍历这个数组，同时维护一个数值递减的栈。比如，我们考察A[i]的时候，就会在这个stack里通过二分法，找到恰好小于等于A[i]的数以及它对应的索引（比如是j）。那么i-j就是考察A[i]时能得到的"最宽"的pair。然后我们需要将A[i]加入这个栈中，可以想象，如果A[i]大于等于栈顶元素，那么A[i]就没有再入栈的意义，这是因为此时的栈顶元素，数值既比A[i]小，索引也比i小，无论如何在后续的处理中都是比A[i]更好的选择。于是，依此处理完所有的A[i]，找到最宽的(j,i)配对，就是答案。

以上的算法在实际代码过程中需要用到较多的数据结构。我们其实需要维护两个栈，一个栈存数值，一个栈存索引。两个栈的压入都是同步的。但是二分法查找的时候是用的数值栈，而在更新(j,i)配对的时候用的是索引栈。

另外，由于这是一个递减的栈，所以用lower_bound的时候，要注意用逆向的迭代器auto it = upper_bound(q.rbegin(),q.rend(),nums[i])在根据迭代器计算索引位置的时候：int k = it-q.rbegin()表示在数组中倒数的位置。

解法2
本题还有更惊艳的o(N)的解法。

同样遍历这个数组，同时维护一个数组递减的栈。但是在生成这个栈的过程中，我们并不针对每个A[i]取找最宽的配对。而是直接先把这个栈生成完毕。

        for i in range(len(A)):
            if len(Stack)==0 or A[Stack[-1]]>=A[i]:
                Stack.append(i)
绝妙的下一步是：从后往前依次考察A，对于每个A[i]，我们从栈尾依次弹出元素直至遇到一个恰好小于等于A[i]的索引j，那么(j,i)就是关乎A[i]我们能得到的最宽的配对。至于那些已经弹出栈的元素，其实丢了就丢了，并不会对答案有更多的贡献。比如说，j+1和i-1即使配对成功，也不能超越(j,i)的宽度。这样将A从后往前扫一遍，就能找到最宽的配对。

"""

import bisect

class Solution:
    def maxWidthRamp(self, A) -> int:
        stack = []
        for i, num in enumerate(A):
            if not stack or num < A[stack[-1]]:
                stack.append(i)
        res = 0
        for i in range(len(A)-1, -1, -1):
            while stack and A[i] >= A[stack[-1]]:
                res = max(res, i - stack.pop())
        return res




class SolutionBS:
    def maxWidthRamp(self, A):
        stack = []
        res = 0
        for i in range(len(A))[::-1]:
            if not stack or A[i] > stack[-1][0]:
                stack.append([A[i], i])
            else:
                j = stack[bisect.bisect(stack, [A[i], i])][1]
                res = max(res, j - i)
        return res




A = [6,0,8,2,1,5]
a = Solution()
print(a.maxWidthRamp(A))

