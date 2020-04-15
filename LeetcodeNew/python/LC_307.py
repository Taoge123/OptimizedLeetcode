
"""
https://www.cnblogs.com/grandyang/p/4985506.html

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""
"""
Use self.c to represent Binary Indexed Tree. 
Section sums are stored in self.c[1..len(nums)]. 
x & -x is lowbit function, which will return x's rightmost bit 1, 
e.g. lowbit(7) = 1, lowbit(20) = 4.

self.c[1] = nums[0]

self.c[2] = nums[0] + nums[1]

self.c[3] = nums[2]

self.c[4] = nums[0] + nums[1] + nums[2] + nums[3]

self.c[5] = nums[4]

self.c[6] = nums[4] + nums[5]

self.c[7] = nums[6]

self.c[8] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]

C1 = A1
C2 = A1 + A2
C3 = A3
C4 = A1 + A2 + A3 + A4
C5 = A5
C6 = A5 + A6
C7 = A7
C8 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8

那么是如何确定某个位置到底是有几个数组成的呢，原来是根据坐标的最低位 Low Bit 来决定的，
所谓的最低位，就是二进制数的最右边的一个1开始，加上后面的0(如果有的话)组成的数字，
例如1到8的最低位如下面所示：

坐标          二进制       最低位

1               0001          1

2               0010          2

3               0011          1

4               0100          4

5               0101          1

6               0110          2

7               0111          1

8               1000          8

最低位的计算方法有两种，一种是 x&(x^(x–1))，另一种是利用补码特性 x&-x。
这道题我们先根据给定输入数组建立一个树状数组 bit，
比如，对于 nums = {1, 3, 5, 9, 11, 13, 15, 17}，建立出的 bit 数组为：

bit -> 0 1 4 5 18 11 24 15 74
         -   -    --    --   
    
0 1 4 5 18 11 24 15 74

0 1 4 2 18 11 24 15 74
      -
0 1 4 2 15 11 24 15 74
        --
0 1 4 2 15 11 24 15 71
                    --


"""


class BinaryIndexTree:
    def __init__(self, nums):
        self.nums = [0] * len(nums)
        self.BIT = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.update(i, num)

    def _lowbit(self, a):
        return a & -a

    def update(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += diff
            i += self._lowbit(i)

    def get(self, i):
        res = 0
        while i:
            res += self.BIT[i]
            i -= self._lowbit(i)
        return res


class NumArray:
    def __init__(self, nums):
        self.bit = BinaryIndexTree(nums)

    def update(self, i, val):
        self.bit.update(i, val)

    def sumRange(self, i, j):
        return self.bit.get(j + 1) - self.bit.get(i)






class NumArrayShorter:
    def __init__(self, nums):
        self.arr = [0] * len(nums)
        self.BIT = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.update(i, num)
        self.sumRange = lambda i, j: self.Sum(j + 1) - self.Sum(i)

    def update(self, i, val):
        diff, self.arr[i] = val - self.arr[i], val
        i += 1
        while i < len(self.BIT):
            self.BIT[i] += diff
            i += (i & -i) # to next

    def Sum(self, k):
        res = 0
        while k:
            res += self.BIT[k]
            k -= (k & -k) # to parent
        return res




class SegmentTreeNode:
    def __init__(self, val, start, end):
        self.val = val
        self.start, self.end = start, end
        self.left, self.right = None, None

class SegmentTree(object):
    def __init__(self, n):
        self.root = self.buildTree(0, n-1)

    def buildTree(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(0, start, end)
        if start == end:
            return root
        mid = (start+end) / 2
        root.left, root.right = self.buildTree(start, mid), self.buildTree(mid+1, end)
        return root

    def update(self, i, diff, root=None):
        root = root or self.root
        if i < root.start or i > root.end:
            return
        root.val += diff
        if i == root.start == root.end:
            return
        self.update(i, diff, root.left)
        self.update(i, diff, root.right)

    def sum(self, start, end, root=None):
        root = root or self.root
        if end < root.start or start > root.end:
            return 0
        if start <= root.start and end >= root.end:
            return root.val
        return self.sum(start, end, root.left) + self.sum(start, end, root.right)


class NumArrayST:
    def __init__(self, nums):
        self.seg_tree = SegmentTree(len(nums))
        self.nums = nums
        for i, num in enumerate(nums):
            self.seg_tree.update(i, num)

    def update(self, i, val):
        self.seg_tree.update(i, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        return self.seg_tree.sum(i, j)



"""
------------------------------------------------------------------------------------------------------------------------
"""
class NumArray2:
    def __init__(self, nums):
        self.n = len(nums)
        self.a = nums
        self.nums = [0] * (self.n + 1)
        for i in range(self.n):
            k = i + 1
            while k <= self.n:
                self.nums[k] += nums[i]
                k += (k & -k)

    def update(self, i, val):
        diff = val - self.a[i]
        self.a[i] = val
        i += 1
        while i <= self.n:
            self.nums[i] += diff
            i += (i & -i)

    def sumRange(self, i, j):
        res = 0
        j += 1
        while j:
            res += self.nums[j]
            j -= (j & -j)
        while i:
            res -= self.nums[i]
            i -= (i & -i)
        return res


nums = [1, 3, 5]
a = NumArray(nums)
print(a.sumRange(1,2))

