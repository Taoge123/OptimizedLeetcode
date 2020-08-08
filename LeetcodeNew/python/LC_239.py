"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

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

Follow up:
Could you solve it in linear time?

1. maintian a mono decreasing queue
2. chec if the queue head is out dated
3. the maximum of the sliding window is the queue head

解法1
我们希望设计这样一个队列，每次读入一个新数nums[i]之后，希望队列弹出的就是当前窗口的最大值。当然，这个最大值不一定要真正“弹出去”，
因为可能它处于窗口的中间位置，等下一个新数来的时候，可能依然是读取这个最大值。所以我们希望这个最大值能就一直保持在队列的首端，等待需要的时候再真正清除。什么时候需要清除呢？那就是发现当这个最大值的index等于i-k的时候，说明它超出了窗口长度，不得不踢掉了。

如果把这个最大值踢掉了，我们希望在队列首端的是接下来第二大的值。于是，这就提示了我们：这个队列盛装的是一个递减的序列！
这个序列是这个窗口里的最大的几个值的降序排列。这就告诉我们，每进入一个新数nums[i]，这个队列尾端的那些小于nums[i]的都可以踢掉了，
然后把新数装进去。这样，直到nums[i]离开窗口之前，函数读取的最大值都是这些比nums[i]大的数。

可以想见，我们需要的数据结构就是一个双端队列dequeu。每次加入新数nums[i]，但从后端弹出一些，以使得里面保持一个递减的序列。
每次的队首元素就是当前k窗口的最大值，直到这个队首元素对应的index超出了k窗口的范围才被弹出。
"""

import collections

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

            if i >= k - 1:
                res.append(nums[queue[0]])

        return res


