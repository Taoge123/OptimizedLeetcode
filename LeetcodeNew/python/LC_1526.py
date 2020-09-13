"""
1526.Minimum-Number-of-Increments-on-Subarrays-to-Form-a-Target-Array
解法1： 线段树
直观上说比较容易想到贪心的解决方案。第一步，我们肯定会挑选全局最小的元素target[i]，然后让整个数组都增加target[i]。此后任何操作都不可横跨整个数组。我们会选择递归处理[0:i-1]和[i+1:n-1]这两个区间。方法也类似，就是在[0:i-1]这个区间内找到最小的元素target[j]，让这段区间都增加至target[j]，既然我递归处理[0:j-1]和[j+1:i-1]这两个区间...

所以上述方法的难点在于快速挑选一段区间内的最小元素和它所在的位置。这种数据结构显然合适线段树来处理。我们构建segmentTree的数据结构，提供一个函数[minVal, pos]=queryMin(start,end)来满足需求。递归的代码就是：

  void DFS(int a, int b, int cur)
    {
        if (a>b) return;
        auto x = queryTree(root, a, b);
        int val = x.first;
        int pos = x.second;
        if (val!=cur)
            ret += (val-cur);
        DFS(a, pos-1, val);
        DFS(pos+1, b, val);
    }
解法2： 贪心法
我们将target数组想象成连绵起伏的山峦。我们在上坡走的时候，每一步肯定都需要做“增加”的操作（相当于垒土造山）。但是在下坡走的时候实际上不需要任何操作，因为任何一个下坡的位置j，都可以找到一个对应的上坡位置i，可以认为在i位置通过“增加”操作成就了target[j]。举个例子：1 3 4 2。我们在处理j=3的时候，target[3]可以认为是在i=1的时候，对于区间[1:3]增加1而构造得到的。至于taget[1]=3本身，则可以认为是再通过一步对区间[1:2]增加1得到。这两个效果的叠加，等效于在i=1的位置，直接增加2，也就是target[1]相对于target[0]的增量。

同理，当我们走过“山谷”，重新上坡的时候，又要开始计数“增加”的操作。
"""

"""
[1,2,3,2,1]
任何一个subarray都加1, 直到达到target array

queryMin(start, end) -> return the {minMin, minPos} within range[start, end]

"""


class SegTree:
    def __init__(self, array):
        self.seg_tree = {}
        self.build_seg_tree(0, len(array) - 1, array)

    def build_seg_tree(self, left, right, array):
        if left == right:
            self.seg_tree[(left, right)] = (left, array[left])
            return
        mid = (left + right) // 2
        self.build_seg_tree(left, mid, array)
        self.build_seg_tree(mid + 1, right, array)
        lindex, lvalue = self.seg_tree[(left, mid)]
        rindex, rvalue = self.seg_tree[(mid + 1, right)]
        self.seg_tree[(left, right)] = (lindex, lvalue) if lvalue < rvalue else (rindex, rvalue)

    def find_min(self, left, right, begin, end):
        if left == begin and right == end:
            return self.seg_tree[(left, right)]
        mid = (left + right) // 2
        if begin > mid:
            return self.find_min(mid + 1, right, begin, end)
        elif end <= mid:
            return self.find_min(left, mid, begin, end)
        else:
            lindex, lvalue = self.find_min(left, mid, begin, mid)
            rindex, rvalue = self.find_min(mid + 1, right, mid + 1, end)
            return (lindex, lvalue) if lvalue < rvalue else (rindex, rvalue)


class Solution:
    def minNumberOperations(self, target) -> int:
        length = len(target)
        if length == 0:
            return 0
        tree = SegTree(target)
        stack = [(0, length - 1, 0)]
        steps = 0
        while stack:
            (left, right, have_move) = stack.pop()
            min_index, min_value = tree.find_min(0, length - 1, left, right)
            steps += min_value - have_move
            if left <= min_index - 1:
                stack.append((left, min_index - 1, min_value))
            if right >= min_index + 1:
                stack.append((min_index + 1, right, min_value))
        return steps




class Solution2:
    def minNumberOperations(self, target) -> int:
        res = 0
        cur = 0
        for i in range(len(target)):
            if target[i] > cur:
                res += target[i] - cur
            cur = target[i]
        return res




target = [1,2,3,2,1]
a = Solution2()
print(a.minNumberOperations(target))





