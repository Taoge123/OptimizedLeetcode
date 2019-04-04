
"""
You have k lists of sorted integers in ascending order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.

Example 1:
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Note:
The given list may contain duplicates, so ascending order means >= here.
1 <= k <= 3500
-105 <= value of elements <= 105.
For Java users, please note that the input type has been changed to List<List<Integer>>.
And after you reset the code template, you'll see this point.
"""

"""
Image you are merging k sorted array using a heap. Then everytime you pop the smallest element out 
and add the next element of that array to the heap. By keep doing this, you will have the smallest range.
"""

"""
Keep a heap of the smallest elements. As we pop element A[i][j], we'll replace it with A[i][j+1]. 
For each such element left, we want right, the maximum of the closest value 
in each row of the array that is >= left, which is also equal to the current maximum of our heap. 
We'll keep track of right as we proceed.
"""

import heapq

class Solution1:
    def smallestRange(self, A):
        pq = [(row[0], i, 0) for i, row in enumerate(A)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in A)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(A[i]):
                return ans
            v = A[i][j + 1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j + 1))


"""
Clearly, each left and right bound must be a value in some array.

For each candidate left bound equal to some value in some array, 
let's determine the next-rightmost value of each array. If it doesn't exist, 
then our left is already too large for any subsequent candidates to have a solution. 
Otherwise, we can choose the maximum of these to be the corresponding right bound for our candidate left bound. 
We take the maximum of all such candidates.
"""

class Solution2:
    def smallestRange(self, A):
        A = [row[::-1] for row in A]

        ans = -1e9, 1e9
        for left in sorted(reduce(set.union, map(set, A))):
            right = -1e9
            for B in A:
                while B and B[-1] < left:
                    B.pop()
                if not B:
                    return ans
                right = max(right, B[-1])
            if right - left < ans[1] - ans[0]:
                ans = left, right
        return ans


"""
Really nice solution. I upvoted. A little improvement:
A = [row[::-1] for row in A] takes a lot of time and it is not necessary.
The following solution improve the original one, from 450ms to 250ms.
"""
class SolutionLee:
    def smallestRange(self, A):
        ans = -1e9, 1e9
        for right in sorted(set(x for l in A for x in l))[::-1]:
            for B in A:
                while B and right < B[-1]:
                    B.pop()
                if not B:
                    return ans
            left = min(B[-1] for B in A)
            if right - left <= ans[1] - ans[0]:
                ans = left, right
        return ans


class Solution3:
    def smallestRange(self, nums):

        heap = [(List[0], index, 0) for index, List in enumerate(nums)]  # First element of each list with list number and index of the element in each list
        heapq.heapify(heap)  # to get the min value from all the elements of each list

        max_val = max([List[0] for List in nums])  # To get the max value for the range
        smallest_range = -1e9, 1e9  # max and min for the range

        while heap:
            min_val, list_index, num_index = heapq.heappop(
                heap)  # get the min value, the list its from and the index it is at in the particular list

            if max_val - min_val < smallest_range[1] - smallest_range[
                0]:  # To find the smallest difference which will be the range
                smallest_range = min_val, max_val

            if num_index + 1 == len(nums[list_index]):  # once any one of the list is exhausted, return the range
                return smallest_range

            next_num = nums[list_index][num_index + 1]  # To get the next element from the list that has the min value

            max_val = max(max_val, next_num)
            heapq.heappush(heap, (next_num, list_index, num_index + 1))


class Solution4:
    def smallestRange(self, nums):

        q = []  # element in the heap: val, i, j, where val is nums[i][j]
        max_val = nums[0][0]
        for i in range(len(nums)):
            heapq.heappush(q, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])  # also remember max of the heap
        min_range = [-10 ** 5, 10 ** 5]
        while q:
            min_val, i, j = heapq.heappop(q)
            if max_val - min_val < min_range[1] - min_range[0] or (
                                max_val - min_val == min_range[1] - min_range[0] and min_val < min_range[0]):
                min_range = [min_val, max_val]
            # push the next value in the ith array if any
            if j + 1 < len(nums[i]):
                max_val = max(max_val, nums[i][j + 1])
                heapq.heappush(q, (nums[i][j + 1], i, j + 1))
            else:  # ths ith array is exhausted
                return min_range

"""
Suppose we have formed a range with one element from each list. 
We can form another range by advancing one value along its belonging list. 
If we're not advancing the smallest value, the left bound will remain unchanged and the right bound will be increased. 
It's impossible to find the smallest range within such searching space. In other words, 
it's safe to advancing the smallest value in the current range.
"""

class Solution5:
    def smallestRange(self, nums):
        iters = [iter(l) for l in nums]
        heap = [(next(it), i) for i, it in enumerate(iters)]
        heapq.heapify(heap)

        lo, hi = 0, float('inf')
        rbound = max(heap)[0]
        while True:
            lbound, i = heap[0]
            if rbound - lbound < hi - lo:
                lo, hi = lbound, rbound
            nxt = next(iters[i], None)
            if nxt is None:
                return [lo, hi]
            rbound = max(rbound, nxt)
            heapq.heappushpop(heap, (nxt, i))




