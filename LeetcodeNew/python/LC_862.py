
"""
LC209 ++++++
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/1515369/Python3-binary-search
https://buptwc.com/2018/07/02/Leetcode-862-Shortest-Subarray-with-Sum-at-Least-K/


209. Minimum Size Subarray Sum
Prepare
From @Sarmon:
"What makes this problem hard is that we have negative values.
If you haven't already done the problem with positive integers only,
I highly recommend solving it first"

Minimum Size Subarray Sum

Explanation
Calculate prefix sum B of list A.
B[j] - B[i] represents the sum of subarray A[i] ~ A[j-1]
Deque d will keep indexes of increasing B[i].
For every B[i], we will compare B[i] - B[d[0]] with K.


Complexity:
Every index will be pushed exactly once.
Every index will be popped at most once.

Time O(N)
Space O(N)


How to think of such solutions?
Basic idea, for array starting at every A[i], find the shortest one with sum at leat K.
In my solution, for B[i], find the smallest j that B[j] - B[i] >= K.
Keep this in mind for understanding two while loops.


What is the purpose of first while loop?
For the current prefix sum B[i], it covers all subarray ending at A[i-1].
We want know if there is a subarray, which starts from an index, ends at A[i-1] and has at least sum K.
So we start to compare B[i] with the smallest prefix sum in our deque, which is B[D[0]], hoping that [i] - B[d[0]] >= K.
So if B[i] - B[d[0]] >= K, we can update our result res = min(res, i - d.popleft()).
The while loop helps compare one by one, until this condition isn't valid anymore.


Why we pop left in the first while loop?
This the most tricky part that improve my solution to get only O(N).
D[0] exists in our deque, it means that before B[i], we didn't find a subarray whose sum at least K.
B[i] is the first prefix sum that valid this condition.
In other words, A[D[0]] ~ A[i-1] is the shortest subarray starting at A[D[0]] with sum at least K.
We have already find it for A[D[0]] and it can't be shorter, so we can drop it from our deque.


What is the purpose of second while loop?
To keep B[D[i]] increasing in the deque.


Why keep the deque increase?
If B[i] <= B[d.back()] and moreover we already know that i > d.back(), it means that compared with d.back(),
B[i] can help us make the subarray length shorter and sum bigger. So no need to keep d.back() in our deque.


"""

"""

A B C D E F  j
    -
    first while loop: j和C可以组成一对, 那么AB就不需要了
    second while loop: 
    
    
"""

import collections
import bisect


class Solution:
    def shortestSubarray(self, A, K: int) -> int:
        # index and summ
        queue = collections.deque([[0, 0]])
        res = float('inf')
        summ = 0
        for i, num in enumerate(A):
            summ += num
            # 思路中第2步, 满足条件下选最大index, 前面都不需要了
            # store the index the B in the deque, so that all index in deque are min
            # KEY 2 use B[0] to storet min value, so that B[i] can check whether it is able to find the possible answer
            # ==>  make sure deque is increasing, then it becomes 209
            while queue and summ - queue[0][1] >= K:
                res = min(res, i - queue[0][0] + 1)
                queue.popleft()
            # 思路中第3步， 保证queue是递增的, 只要前面出现>=最新summ, 都pop
            # negative number shouldn't become starting point
            while queue and summ <= queue[-1][1]:
                queue.pop()
            queue.append([i + 1, summ])
        return res if res < float('inf') else -1



class SolutionRika:
    def shortestSubarray(self, nums, k: int) -> int:
        presum = [0]
        for i in range(len(nums)):
            presum.append(presum[-1] + nums[i])

        queue = collections.deque()
        res = float('inf')

        for i in range(len(presum)):
            while queue and presum[i] - presum[queue[0]] >= k:
                res = min(res, i - queue[0])
                queue.popleft()
            # maintain min value in queue[0]
            while queue and presum[i] <= presum[queue[-1]]:
                queue.pop()

            queue.append(i)

        if res == float('inf'):
            return -1
        return res


class SolutionBinarySearch:
    def shortestSubarray(self, nums, k: int) -> int:

        summ_last_index = {0: -1}
        presum = [0]  # increasing stack
        summ = 0
        res = float("inf")

        for right, num in enumerate(nums):
            summ += num
            left = bisect.bisect_right(presum, summ - k)
            if left:
                res = min(res, right - summ_last_index[presum[left - 1]])
            summ_last_index[summ] = right

            while presum and presum[-1] >= summ:
                presum.pop()

            presum.append(summ)
        return res if res < float('inf') else -1


"""
SolutionTest does not work with two pointer
[84,-37,32,40,95]
167
"""
class SolutionTest:
    def shortestSubarray(self, nums, k: int) -> int:
        left = 0
        summ = 0
        n = len(nums)
        res = float('inf')
        for right in range(n):
            summ += nums[right]

            while left < right and summ >= k:
                if summ >= k:
                    res = min(res, right - left + 1)
                summ -= nums[left]
                left += 1

        return -1 if res == float('inf') else res


A = [84,-37,32,40,95]
K = 167
a = SolutionTest()
print(a.shortestSubarray(A, K))



