"""
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc]
which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:

Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]
"""


class Solution:
    def getModifiedArray(self, length: int, updates):
        res = [0] * length
        for num in updates:
            start, end, inc = num
            res[start] += inc
            if end + 1 <= length - 1:
                res[end + 1] -= inc
        total = 0
        for i in range(length):
            total += res[i]
            res[i] = total
        return res




class Solution2:
    def getModifiedArray(self, length: int, updates):

        res = [0] * (length + 1)
        for num in updates:
            res[num[0]] += num[2]
            res[num[1] + 1] -= num[2]
        total = 0
        for i in range(length):
            total += res[i]
            res[i] = total
        # res.pop()
        return res[:-1]






