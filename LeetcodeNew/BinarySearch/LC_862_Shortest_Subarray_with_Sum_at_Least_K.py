
"""
https://github.com/xiaoylu/leetcode_category
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143850/Python-Simple-and-Readable-AC-Heapq-Solution-w-Detailed-Explanation

The following question can be solved by monotonic queue:

LC84. Largest Rectangle in Histogram
LC239. Sliding Window Maximum
LC739. Daily Temperatures
LC862. Shortest Subarray with Sum at Least K
LC901. Online Stock Span
LC907. Sum of Subarray Minimums

https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/204290/Monotonic-Queue-Summary

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.



Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
"""
import collections
import heapq

class Solution1:
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1

"""
Calculate prefix sum B of list A.
B[j] - B[i] represents the sum of subarray A[i] ~ A[j-1]
Deque d will keep indexes of increasing B[i].
For every B[i], we will compare B[i] - B[d[0]] with K.

Time Complexity:
Loop on B O(N)
Every index will be pushed only once into deque. O(N)
"""

class SolutionLee:
    def shortestSubarray(self, A, K):
        N = len(A)
        B = [0] * (N + 1)
        for i in range(N): B[i + 1] = B[i] + A[i]
        d = collections.deque()
        res = N + 1
        for i in range(N + 1):
            while d and B[i] - B[d[0]] >= K:
                res = min(res, i - d.popleft())
            while d and B[i] <= B[d[-1]]:
                d.pop()
            d.append(i)
        return res if res <= N else -1

"""
FAQ
Q: How to think of such solutions?
A: Basic idea, for array starting at every A[i], find the shortest one with sum at leat K.
In my solution, for B[i], find the smallest j that B[j] - B[i] >= K.
Keep this in mind for understanding two while loops.

Q: What is the purpose of first while loop?
A: For the current prefix sum B[i], it covers all subarray ending at A[i-1].
We want know if there is a subarray, which starts from an index, ends at A[i-1] and has at least sum K.
So we start to compare B[i] with the smallest prefix sum in our deque, which is B[D[0]], hoping that [i] - B[d[0]] >= K.
So if B[i] - B[d[0]] >= K, we can update our result res = min(res, i - d.popleft()).
The while loop helps compare one by one, until this condition isn't valid anymore.

Q: Why we pop left in the first while loop?
A: This the most tricky part that improve my solution to get only O(N).
D[0] exists in our deque, it means that before B[i], we didn't find a subarray whose sum at least K.
B[i] is the first prefix sum that valid this condition.
In other words, A[D[0]] ~ A[i-1] is the shortest subarray starting at A[D[0]] with sum at least K.
We have already find it for A[D[0]] and it can't be shorter, so we can drop it from our deque.

Q: What is the purpose of second while loop?
A: To keep B[D[i]] increasing in the deque.

Q: Why keep the deque increase?
A: If B[i] <= B[d.back()] and moreover we already know that i > d.back(), it means that compared with d.back(),
B[i] can help us make the subarray length shorter and sum bigger. So no need to keep d.back() in our deque.


Please let me know if there is still anything unclear.
"""
class Solution2:
    def shortestSubarray(self, A, K):
        heap, l, sm = [], float("inf"), 0
        heapq.heappush(heap, (0, -1))
        for i, num in enumerate(A):
            sm += num
            dif = sm - K
            while heap and (heap[0][0] <= dif or i - heap[0][1] >= l):
                preSum, preIndex = heapq.heappop(heap)
                if i - preIndex < l:
                    l = i - preIndex
            heapq.heappush(heap, (sm, i))
        return l < float("inf") and l or -1


class Solution3:
    def shortestSubarray(self, A, K):

        N = len(A)
        pre_sum = [0] * (N + 1)
        for i, n in enumerate(A):
            pre_sum[i + 1] = pre_sum[i] + n

        ans = N + 1
        queue = collections.deque()

        for j in range(N + 1):
            while queue and pre_sum[queue[-1]] >= pre_sum[j]:
                queue.pop()

            while queue and pre_sum[j] - pre_sum[queue[0]] >= K:
                i = queue.popleft()
                ans = min(ans, j - i)

            queue.append(j)

        return ans if ans < N + 1 else -1


class Solution4:
    def shortestSubarray(self, A, K):
        prefix = [0]
        for i in A: prefix.append(prefix[-1] + i)
        ans = float('inf')
        deque = collections.deque([0])
        for i in range(1, len(A)+1):
            while deque and prefix[i] - prefix[deque[0]] >= K:
                ans = min(ans, i - deque.popleft())
            while deque and prefix[deque[-1]] >= prefix[i]:
                deque.pop()
            deque.append(i)
        return ans if ans != float('inf') else -1

