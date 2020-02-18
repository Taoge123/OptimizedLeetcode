
"""
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
"""



class BinaryIndexTree:
    def __init__(self, nums):
        n = len(nums)
        self.nums = [0 for _ in range(n + 1)]
        self.BIT = [0 for _ in range(n + 1)]
        for i, num in enumerate(nums):
            self.set(i + 1, num)

    def _lowbit(self, a):
        return a & -a

    def set(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        while i < len(self.BIT):
            self.BIT[i] += diff
            i += self._lowbit(i)

    def get(self, i):
        res = 0
        while i > 0:
            res += self.BIT[i]
            i -= self._lowbit(i)
        return res


class NumArray:
    def __init__(self, nums):
        self.bit = BinaryIndexTree(nums)

    def update(self, i, val):
        self.bit.set(i + 1, val)

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

