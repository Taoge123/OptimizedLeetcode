"""
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree:

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?

"""


class Solution:
    def verifyPreorder(self, preorder) -> bool:

        stack, mini = [], float('-inf')

        for num in preorder:
            if num < mini:
                return False

            while stack and num > stack[-1]:
                mini = stack.pop()

            stack.append(num)

        return True



