
"""
Given an array nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. ou can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

https://www.jianshu.com/p/7662caf4f39c


Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note:
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
"""

"""
Keep indexes of good candidates in deque d. The indexes in d are from the current window, 
they're increasing, and their corresponding nums are decreasing. 
Then the first deque element is the index of the largest window value.

For each index i:

1. Pop (from the end) indexes of smaller elements (they'll be useless).
2. Append the current index.
3. Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
4. If our window has reached size k, append the current window maximum to the output."""




"""
Max Heap Solution: O(NlogN)

- Add k elements and their indices to heap. Python has min-heap. 
  So for max-heap, multiply by -1.
- Set start = 0 and end = k-1 as the current range.
- Extract the max from heap which is in range i.e. >= start. Add the max to the result list. 
  Now add the max back to the heap - it could be relevant to other ranges.
- Move the range by 1. Add the new last number to heap.
- This is an O(NlgN) solution.
- Note that we need not invest into thinking about deleting the obsolete entry every time the window slides.
  That would be very hard to implement. Instead we maintain the index in heap and "delete" 
  when the maximum number is out of bounds.
"""


"""
Solution Using Dequeue: O(N)

- Very similar code structure to heap solution
- http://yuanhsh.iteye.com/blog/2190852
- https://docs.python.org/2/library/collections.html#collections.deque
- Add to dequeue at tail using the rule where you pop all numbers from tail which are less than equal to the number. 
  Think why? 300->50->27 and say 100 comes. 50 and/or 27 can never be the maximum in any range.
- When you do the above, the largest number is at head. But you still need to test if front is within the range or not.
- Pop or push each element at-max once. O(N)
*So, to maintain the queue in order,

- When moves to a new number, iterate through back of the queue, 
  removes all numbers that are not greater than the new one, and then insert the new one to the back.
findMax only need to take the first one of the queue.
- To remove a number outside the window, 
- only compare whether the current index is greater than the front of queue. If so, remove it.*"""


"""
We create a Deque, Qi of capacity k, that stores only useful elements of current window of k elements. 
An element is useful if it is in current window 
and is greater than all other elements on left side of it in current window. 
We process all array elements one by one and maintain Qi to contain useful elements of current window 
and these useful elements are maintained in sorted order. 
The element at front of the Qi is the largest and element at rear of Qi is the smallest of current window. 
"""

"""
遍历数组nums，使用双端队列deque维护滑动窗口内有可能成为最大值元素的数组下标

由于数组中的每一个元素至多只会入队、出队一次，因此均摊时间复杂度为O(n)

记当前下标为i，则滑动窗口的有效下标范围为[i - (k - 1), i]

若deque中的元素下标＜ i - (k - 1)，则将其从队头弹出，deque中的元素按照下标递增顺序从队尾入队。

这样就确保deque中的数组下标范围为[i - (k - 1), i]，满足滑动窗口的要求。

当下标i从队尾入队时，顺次弹出队列尾部不大于nums[i]的数组下标（这些被弹出的元素由于新元素的加入而变得没有意义）

deque的队头元素即为当前滑动窗口的最大值
"""

"""
Algorithm

The algorithm is quite straigthforward :

    - Process the first k elements separately to initiate the deque.

    - Iterate over the array. At each step :

        - Clean the deque :

            - Keep only the indexes of elements from the current sliding window.

            - Remove indexes of all elements smaller than the current one, since they will not be the maximum ones.

        - Append the current element to the deque.

        - Append deque[0] to the output.

    - Return the output array.

"""
import heapq
import collections

class Solution3:
    def get_next_max(self, heap, start):
        while True:
            x, idx = heapq.heappop(heap)
            if idx >= start:
                return x * -1, idx

    def maxSlidingWindow(self, nums, k):
        if k == 0:
            return []
        heap = []
        for i in range(k):
            heapq.heappush(heap, (nums[i] * -1, i))
        result, start, end = [], 0, k - 1
        while end < len(nums):
            x, idx = self.get_next_max(heap, start)
            result.append(x)
            heapq.heappush(heap, (x * -1, idx))
            start, end = start + 1, end + 1
            if end < len(nums):
                heapq.heappush(heap, (nums[end] * -1, end))
        return result


class Solution:
    def maxSlidingWindow(self, nums, k):

        queue = collections.deque([])
        res = []

        for i in range(len(nums)):
            # checking front
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            # checking back
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            if queue and i >= k - 1:
                res.append(nums[queue[0]])

        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3

a = Solution()
print(a.maxSlidingWindow(nums, k))








