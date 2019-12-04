"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""


class Solution:

    # incrementing n - 1 elements by 1. is the same as decrement one element by 1
    # Then all we need is to deal with one of the num

    def minMoves(self, nums) -> int:

        mini = min(nums)
        res = 0

        for num in nums:
            res += num - mini

        return res


