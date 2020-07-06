"""
local == global means there are no global inversions
curMax[i-1] < A[i+1]
curMax[i+2] > A[i]
对于A[i]而言，它不在乎A[i-1]是否比它大。即使比它大，也只是引入了一个local inversion，而不会有额外的global inversion。
而要避免牵扯更多的global inversion，唯一的要求就是第i-2个元素及之前的所有元素都要比A[i]小。于是我们可以在遍历元素i的过程中，维护一个curMax，
记录的是从第0个元素到第i-2个元素的最大值。只要出现curMax > A[i]即返回false。

"""


class Solution:
    def isIdealPermutation(self, A) -> bool:
        curMax = A[0]
        for i in range(len(A)):
            if i >= 2:
                curMax = max(curMax, A[i - 2])

            if i >= 2 and A[i] < curMax:
                return False

        return True


