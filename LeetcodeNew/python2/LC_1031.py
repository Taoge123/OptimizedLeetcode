"""
So the problem is essentially 2 separate cases.

But it's important to keep in mind that the L+M maximum could be reached before L & M separate from each other
So you cannot divide each case into simply 2 steps:

find the global maximum of the window on the left
find the maximum of the second window in the region to the right of the first window
case 1: L-window comes before M-windows
Once L-window reaches it's global maximum, it will stop sliding but M window can keep going on

case 2: M-window comes before L-windows
Once M-window reaches it's global maximum, it will stop sliding but L window can keep going on
"""


class Solution:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:
        for i in range(1, len(A)):
            A[i] += A[ i -1]

        res = A[ L + M -1]
        left = A[ L -1]
        right = A[ M -1]

        for i in range( L +M, len(A)):
            left = max(left, A[ i -M] - A[ i - L -M])
            res = max(res, left + A[i] - A[ i -M])

        for i in range( L +M, len(A)):
            right = max(right, A[ i -L] - A[ i - L -M])
            res = max(res, right + A[i] - A[ i -L])

        return res



