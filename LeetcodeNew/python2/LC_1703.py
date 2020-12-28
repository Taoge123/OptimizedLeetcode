
"""
1703.Minimum-Adjacent-Swaps-for-K-Consecutive-Ones
首先我们要有这样的意识：想要以最少的操作把k个1靠拢，显然这个k个1必然是在原数组中相邻的（刨除零元素）。所以我们先构造一个新数组p，里面的元素就是原数组中所有1的位置。接下来我们就在数组p中考察所有长度为k的滑窗。在每个滑窗里，我们有k个离散的位置点，我们的任务是研究如何用最少的操作，得到k个连续的位置。

此时我们会想到一个类似的问题。我们有k个离散点的位置，如何确定一个中心位置x，使得所有k个点离x的距离之和最短？这个问题就是296.Best-Meeting-Point，答案是，“中心”应该选在这k个点的中位数处。此时的总距离total = sum |pi-x|, i=0,1,..,k-1能够最小。

我们再切回之前所考虑的问题，我们不是把所有的点都移到“中心”位置x，而是把所有的点移到以x为中心的连续k个位置。因此我们最小化的是 sum |pi-x| (for i=0,1,..,k-1) - sum|i-k/2| (for i=0,1,..,k-1) . 我们发现第二项其实是一个常数。所以本题的最优解其实和LC296是一样：最佳的“中心”位置依然是所有点的中位数。

因此，回到我们最初所考虑的第一个滑窗，对于p[0]~p[k-1]这k个位置的点，我们的目的应该把它们移动到[p[k/2] - k/2, p[k/2]+k/2-1]这个区间。为了计算方便，我们省略掉上一段里面的第二项，只考虑把它们都移动到p[k/2]所需要的操作总数。这个是很容易算的，记做是sum。

接下来我们看从第一个滑窗到第二个滑窗的变化：原先的k个位置是p[0]~p[k-1]，中心是在p[mid]；滑动之后的k个位置是p[1]~p[k]，中心是在p[mid+1]。

0  1  2 mid .  . k-1 k
X  X  X  O  X  X  X
   X  X  X  O  X  X  X
相应地，操作总数sum的变化有四个部分：

原先p[0]在滑窗里，贡献了p[mid]-p[0]这么多操作。现在要减去他们。
原先p[k]不在滑窗里，现在加入了滑窗，需要加上它的贡献p[k]-p[mid+1]
原先p[1]~p[mid]到中心p[mid]的距离，现在都变成了p[1]~p[mid]到新中心p[mid+1]的距离，每个数到新中心都多出了p[mid+1]-p[mid]，所以我们需要把sum补上(p[mid+1]-p[mid])*(k/2)
原先p[mid+1]~p[k-1]到中心p[mid]的距离，现在都变成了p[mid+1]~p[k-1]到新中心p[mid+1]的距离，每个数到心中都减少了p[mid+1]-p[mid]，所以我们需要把sum扣除(p[mid+1]-p[mid])*(k-k/2-1)
可见，我们将第一个滑窗的sum，通过四步o(1)的修正，就可以到第二个滑窗的sum。我们将滑窗走一遍，就可以得到最小的sum。注意，最后的答案是把最小的sum减去常数项 sum|i-k/2|.
"""

"""
296 best meeting points

p = [0 4 7 8], k = 2


[p1, p2, p3, p4]
[q1, q2, q3, q4]

min sum |pi - qi| for i in {0, 1, 2, ....., k-1}

"""


class Solution:
    def minMoves(self, nums, k: int) -> int:

        p = []
        for i in range(len(nums)):
            if nums[i] == 1:
                p.append(i)

        summ = 0
        for i in range(k):
            summ += abs(p[i] - p[k // 2])

        res = summ

        for i in range(len(p) - k):
            mid = i + k // 2
            summ -= abs(p[i] - p[mid])
            summ += abs(p[mid + 1] - p[mid]) * (k // 2)
            summ += abs(p[i + k] - p[mid + 1])
            summ -= abs(p[mid + 1] - p[mid]) * (k - k // 2 - 1)
            res = min(res, summ)

        offset = 0
        for i in range(k):
            offset += abs(i - k // 2)

        return res - offset



