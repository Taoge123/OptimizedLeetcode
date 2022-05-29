
"""
https://github.com/wisdompeak/LeetCode/tree/master/Two_Pointers/1574.Shortest-Subarray-to-be-Removed-to-Make-Array-Sorted
Binary Search
https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/discuss/1010516/Python-binary-search

[X X X] [X X X X] [X X X]
 0   i             j   n-1

1. [0:i] increase
2. [j:n-1] increase
3. arr[i] <= arr[j]

"""


class Solution1:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        left, right = 0, n - 1

        # find left stop point
        while left + 1 < n and arr[left + 1] >= arr[left]:
            left += 1

        # find right stop point
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        if left >= right:
            return 0
        res = min(n - left - 1, right)
        i, j = 0, right
        while i <= left and j <= n - 1:
            if arr[i] <= arr[j]:
                res = min(res, j - i - 1)
                i += 1
            else:
                j += 1

        return res


class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:

        # if sorted(arr) == arr:
        #     return 0

        n = len(arr)
        j = n - 1
        res = n - 1

        while j - 1 >= 0 and arr[j] >= arr[j - 1]:
            j -= 1
        res = min(res, j)
        if res == 0:
            return 0

        for i in range(n):
            if i - 1 >= 0 and arr[i] < arr[i - 1]:
                break
            # find a j that > i
            while j < n and arr[j] < arr[i]:
                j += 1
            res = min(res, j - i - 1)

        return res





