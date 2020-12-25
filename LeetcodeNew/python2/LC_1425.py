"""
huahua
https://www.youtube.com/watch?v=B5fa989qz4U
https://www.youtube.com/watch?v=B5fa989qz4U&t=1s
https://www.youtube.com/watch?v=FSbFPH7ejHk


dp[i] : the maximum sum of nn-empty subsequence of that array ending wth nums[i]

XXXX [X j XX] i

dp[i] = max{dp[j] + nums[i]} for j = i-1, i-2, ..., i-k
O(NK)


sliding window maximum


1425.Constrained-Subsequence-Sum
解法1：DP
显然，如果设计dp[i]表示以nums[i]结尾的subsequence能够得到的满足条件的最大和，那么我们可以很轻松地写出转移方程：

dp[i] = max{nums[i], dp[i-k] + nums[i]}, k=1,2,...,K
那么这显然是一个O(NK)级别的算法，根据数据范围肯定会超时。

解法2：Heap
一个优化的思路就是我们在这K个candidate中高效地找到最大值。这可以用自动排序的容器比如说multiset来实现。我们在Set中维护最近的K个dp值并保持升序，这样每次直接在Set尾部取值就行。但是注意的是，每一个回合我们需要弹出最老的那个DP值（即dp[i-k]），那个值是什么我们需要额外记录，并且手工从Set中删除掉。

解法2：单调队列 mono deque
数据结构“双端队列dequeu”不是很常用，但其最重要的用法就是维护单调队列。

我们想象，如果最近得到了一个dp[i]，如果它比我们以前所遇到的dp值都要大，那么就意味着以前所有的dp值我们都不需要再保留？为什么？因为i是最近的index，而且dp[i]又最大，这种“又新又大”的特点使得它在两个维度上都是最优的解。因此，在i之后的任何元素j都只可能与i关联，而不会与i之前的元素关联。所以我们不用保留任何i之前的dp值了。

这就提示了我们，我们需要保留的dp值应该是一个单调递减的序列。队列首端的元素最大，但是比较老；队列末端的元素最小，但是比较新。它们有各自的优势。对于任何新来的元素nums[i]，它要与队列中的哪个元素关联，都是有可能的。具体的方案是：首先看队列首的元素j（因为它最大），如果满足在index上的条件i-j>=K，那么就以为着关联成功，dp[i]=dp[j]+nums[i]。否则说明j这个index太老了，无法满足i-j>=k，以后也肯定不会再用到了，可以直接踢出队列。就这样不停地后移j，直到找到合适的元素。

再更新dp[i]之后，我们也需要将其加入队列。注意到之前的结论，我们需要保持队列单调递减。如果队列尾部的元素dp[j]比dp[i]小，那么我们就可以直接弹出j。道理已经解释过了，j相比于i而言“又老又小”，总是不合算的。

用单调队列的做法，时间复杂度就是o(N).

"""

import collections
import heapq


class Solution:
    def constrainedSubsetSum(self, nums, k: int) -> int:

        n = len(nums)
        dp = [0] * n
        queue = collections.deque()

        for i in range(n):
            while queue and queue[0] < i - k:
                queue.popleft()

            dp[i] = nums[i]
            if queue:
                dp[i] = max(dp[i], dp[queue[0]] + nums[i])

            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()

            queue.append(i)

        return max(dp)



class Solution2:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [nums[0]] * n
        res = dp[0]
        # use dequeue to calculate the max value for k items before i in O(1)
        queue = collections.deque([0])
        for i in range(1, n):
            # keep the size of dequeue to be k.
            if queue[0] < i - k:
                queue.popleft()
            maxi = max(dp[queue[0]], dp[queue[-1]])
            dp[i] = max(maxi + nums[i], nums[i])
            # discard values that are smaller than current value
            while queue and dp[queue[-1]] < dp[i]:
                queue.pop()
            queue.append(i)
            res = max(res, dp[i])
        return res


class SolutionHeap:
    def constrainedSubsetSum(self, nums, k: int) -> int:

        maxi = nums[0]
        heap = [(-maxi, 0)]
        res = maxi
        for i in range(1, len(nums)):
            # Ensure top of the heap is no more than k indices away
            while heap[0][1] < i - k:
                heapq.heappop(heap)

            maxi = max(nums[i], nums[i] - heap[0][0])
            res = max(res, maxi)
            heapq.heappush(heap, (-maxi, i))

        return res

