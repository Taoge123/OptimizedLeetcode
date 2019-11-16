
"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

"""


class Solution(object):
    def find132pattern(self, nums):

        mid = float('-inf')
        stack = []

        for item in nums[::-1]:
            if item < mid:
                return True

            while stack and stack[-1] < item:
                mid = stack.pop()
            stack.append(item)

        return False




