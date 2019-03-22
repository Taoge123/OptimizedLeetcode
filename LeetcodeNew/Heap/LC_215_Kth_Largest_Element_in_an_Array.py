
"""
https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library


Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""
import heapq
import random

class Solution:
    def findKthLargest(self, nums, k):

        return heapq.nlargest(k, nums)[-1]


class Solution2:
    def findKthLargest(self, nums, k):

        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:  # If the list contains only one element,
                return nums[left]  # return that element

            # select a random pivot_index between
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)



"""
215. Kth Largest Element in an Array
这题是一个电面高频题，我们从最原始的方式慢慢的来讨论怎么解题

分析 Input Size 和 K
和面试官沟通过的时候，明确两点

nums这个array的大小如果很小，那么就直接Sort返回完事，没必要整那老多没用的
如果k的size大于len(nums)， 那么直接返回 '-1'
针对上面第一点，有了以下这个解法

Brute Froce"""

class Solution1:
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]


"""
那么好，面试官说，那能轻易饶了你么，size肯定要宇宙无敌爆炸大，我就静静的看着你装逼哈。
那么我们开始考虑如何做的比nlogn更快。

根据Max Heap数据结构来解
大家先别急着说，这是Min Heap啊，你个猪头怎么用Max Heap呢？
但其实大家第一次做这道题或者这一类型的题的时候，往往会先想打Max Heap，大家不要急着去背题，咱看看Max Heap怎么解
你要第Kth大的元素，那我就Heapify一个Max Heap，然后既然是要找第K个大的元素，
Max Heap顶端是最大的，第k个大的就是从最底层向上的第k个元素，实现方法从最底下一个一个pop不就完事了么

Time Complexity：Heapify用了O(N)，然后一共pop了k个元素，每个元素使用logn的时间复杂，所以一共是O(n + klog(n))
Max Heap
Time: O(n + klog(n)) | Space: O(n)

"""
class SolutionMaxHeap:
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res


"""
首先解释下为什么要nums = [-num for num in nums]. 因为Python的Standard Library里面调用heapify的时候，
永远是一个min_heap，然后因为没有Max Heap的implementation，你要做的就是通过Min Heap来模拟Max Heap的运算，
最简单的就是将所有的数变成-num，这是不是一个好的Practice？不一定，很多人也自己implement了Max Heap的数据结构。
具体推荐大家看看这个帖子：StackOverFlow
"""

class SolutionMinHeap:
    def findKthLargest(self, nums, k):
        min_heap = [-float('inf')] * k
        heapq.heapify(min_heap)
        for num in nums:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        return min_heap[0]


"""
我们先想想Min Heap是干什么的。
我们用Leetcode提供的例子来看看

Input: [3,2,1,5,6,4] and k = 2
Output: 5

假设我们初始化一个Size为K的Heap，每个大小都是无穷小，会是这样

  -infinite
    /           input: [3,2,1,5,6,4]
-infinite      

我们每次插入一个元素进我们的heap，只要这个元素比heap里面最小的值大，我们就把最小值pop出来，然后插入元素。
因为你每次pop最小元素，然后push过程中，heap都会重新把内部的数据进行整合，然后当pop和push执行完后，heap的顶端永远是最小的值，
所以用上面的例子全部走完以后，我们看看最终的heap长啥样

     5
    /           
   6      
最大的数6，在第二层，第二大(第k大)的数5，正好就是我们要找大kth largest element

这道题的时间复杂如果同学们不懂: StackOverFlow

上面这段代码额外开辟了O(K)这么一个数组，其实我们完全可以在开辟数组的同时，放入input array里面前k个数的元素，
这样我们的时间复杂度会有一定的提升 (谢谢@lzhang2指正)
Time: O(k) + O((n - k) * logk) | Space: O(K)


"""

class SolutionMinHeap2:
    def findKthLargest(self, nums, k):
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
        return min_heap[0]


"""
Max Heap vs. Min Heap
哪个算法更加好？

Max: Time: O(n + klog(n)) | Space: O(n)
Min: Time: O(k) + O((n-k) * logk) | Space: O(K)

如果考虑k无限接近n
Max: O(n + nlog(n)) ~= O(nlogn)
Min: O(n + logk) ~= O(n)

如果考虑k = 0.5n
Max: O(n + nlogn)
Min: O(n + nlogn)

如果考虑n 无限大
Max: O(constant * n) 为什么是constant * n，参考
Min: O(log(k) * n)

所以几个例子比下来，还真说不清道不明哪个更好，大家千万以后不要机械化上来就写Min Heap，到时候面试官问起来Max和Min区别在哪，
完全懵逼 (公瑾某家电面被问到这，然后没分析透，吃一堑长一智)
"""


class SolutionCaikehe:
    # O(nlgn) time
    def findKthLargest1(self, nums, k):
        return sorted(nums, reverse=True)[k - 1]

    # O(nk) time, bubble sort idea, TLE
    def findKthLargest2(self, nums, k):
        for i in xange(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    # exchange elements, time consuming
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums[len(nums) - k]

    # O(nk) time, selection sort idea
    def findKthLargest3(self, nums, k):
        for i in range(len(nums), len(nums) - k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i - 1] = nums[i - 1], nums[tmp]
        return nums[len(nums) - k]

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest4(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

    # O(k+(n-k)lgk) time, min-heap
    def findKthLargest5(self, nums, k):
        return heapq.nlargest(k, nums)[k - 1]

    # O(n) time, quick selection
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums) + 1 - k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1:], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low





