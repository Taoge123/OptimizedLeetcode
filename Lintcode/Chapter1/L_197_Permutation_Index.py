"""
Description
中文
English
给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。

Description
中文
English
Given a permutation which contains no repeated number,
find its index in all the permutations of these numbers,
 which are ordered in lexicographical order. The index begins at 1

Example
Example 1:

Input:[1,2,4]
Output:1
Example 2:

Input:[3,2,1]
Output:6
"""


class Solution:

    def permutationIndex(self, A):
        # write your code here

        result = 1

        factor = 1

        for i in range(len(A), -1, -1):
            rank = 0










