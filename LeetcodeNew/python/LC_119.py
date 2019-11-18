"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?

"""
class Solution:
    def getRow(self, rowIndex):
        row = [1]
        for i in range(rowIndex):
            row = [x+y for x, y in zip([0] + row, row + [0])]
        return row

class Solution2:
    def getRow(self, rowIndex):
        pascal = [1]*(rowIndex + 1)
        for i in range(2,rowIndex+1):
            for j in range(i-1,0,-1):
                pascal[j] += pascal[j-1]
        return pascal

