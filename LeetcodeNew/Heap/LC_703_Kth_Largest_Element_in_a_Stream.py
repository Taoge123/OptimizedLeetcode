
"""
Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k
and an integer array nums, which contains initial elements from the stream.
For each call to the method KthLargest.add,
return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

"""

"""
这道题让我们在数据流中求第K大的元素，跟之前那道Kth Largest Element in an Array很类似，
但不同的是，那道题的数组是确定的，不会再增加元素，这样确定第K大的数字就比较简单。
而这道题的数组是不断在变大的，所以每次第K大的数字都在不停的变化。那么我们其实只关心前K大个数字就可以了，
所以我们可以使用一个最小堆来保存前K个数字，当再加入新数字后，最小堆会自动排序，
然后把排序后的最小的那个数字去除，则堆中还是K个数字，返回的时候只需返回堆顶元素即可
"""

import heapq

class KthLargest1:

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
      # heappushpop 是先压入，在弹出，压入候有一个排序调整过程
      # 而heapreplace是先弹出最小的，然后压入，不存在对堆的扩容过程

"""
通过这道题复习一下python heap操作：
import heapq
python里面heapq用list实现的是最小堆，也就是每次pop（）出来的是最小的数字。有以下method：
q = []
heappush(q, item)
heappop(q) # 如果只想看一下最小的不取出来，则用q[0]即可
heappushpop(q, item) # 先push再pop
heapify(q) # Transform list x into a heap, in-place, in linear time.
heapreplace(q, item) #先pop再push
nlargest(n, q) # return 前n个最大的数作为list
"""


class KthLargest2:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        heapq.heapify(nums)
        self.heap = nums
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)

        return self.heap[0]






