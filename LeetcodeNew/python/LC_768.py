
"""
This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].
"""
"""
https://leetcode.com/problems/max-chunks-to-make-sorted-ii/solution/
"""


import collections


class Solution:
    def maxChunksToSorted(self, arr) -> int:
        n = len(arr)
        maxOfLeft = [0] * n
        minOfRight = [0] * n

        maxOfLeft[0] = arr[0]
        for i in range(1, n):
            maxOfLeft[i] = max(maxOfLeft[i - 1], arr[i])

        minOfRight[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            minOfRight[i] = min(minOfRight[i + 1], arr[i])

        res = 0
        for i in range(n - 1):
            if maxOfLeft[i] <= minOfRight[i + 1]:
                res += 1

        return res + 1




class Solution2:
    def maxChunksToSorted(self, arr) -> int:

        res = 0

        counter1 = collections.Counter()
        counter2 = collections.Counter()

        for a, b in zip(arr, sorted(arr)):
            counter1[a] += 1
            counter2[b] += 1
            if counter1 == counter2:
                res += 1

        return res






