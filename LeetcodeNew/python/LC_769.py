
"""
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 10].
arr[i] will be a permutation of [0, 1, ..., arr.length - 1].

"""
"""
Explanation:
Iterate the array, if the max(A[0] ~ A[i]) = i,
then we can split the array into two chunks at this index.
"""


class Solution:
    def maxChunksToSorted(self, arr) -> int:
        res = 0
        sum1, sum2 = 0, 0
        for a, b in zip(arr, sorted(arr)):
            sum1 += a
            sum2 += b
            if sum1 == sum2:
                res += 1
        return res


class SolutionTony:
    def maxChunksToSorted(self, arr) -> int:
        expect = sorted(arr)
        nums1 = [0]
        nums2 = [0]
        for i in range(len(arr)):
            nums1.append(arr[i] + nums1[-1])
            nums2.append(expect[i] + nums2[-1])

        res = 0
        for i in range(1, len(nums1)):
            if nums1[i] == nums2[i]:
                res += 1
        return res


"""
3 7 8 4 6 5 9
3
3 7
3 7 8
3 8
3 8
3 8
3 8 9

"""


class Solution:
    def maxChunksToSorted(self, arr) -> int:
        stack = []
        curMax = 0
        for num in arr:
            if not stack or stack[-1] <= num:
                stack.append(num)
                curMax = num
            else:
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(curMax)
        return len(stack)



class Solution3:
    def maxChunksToSorted(self, arr) -> int:
        res = 0
        maxi = 0
        for i in range(len(arr)):
            maxi = max(maxi, arr[i])
            if maxi == i:
                res += 1
        return res


class SolutionLee:
    def maxChunksToSorted(self, arr):
        curMax, res = -1, 0
        for i, v in enumerate(arr):
            curMax = max(curMax, v)
            res += curMax == i
        return res

