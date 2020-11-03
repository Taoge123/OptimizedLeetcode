
"""
[1,4,2,5,3]
 3 3
Consider the subarray that contains A[i],
we can take 0,1,2..,i elements on the left,
from A[0] to A[i],
we have i + 1 choices.

we can take 0,1,2..,n-1-i elements on the right,
from A[i] to A[n-1],
we have n - i choices.

In total, there are (i + 1) * (n - i) subarrays, that contains A[i].
And there are ((i + 1) * (n - i) + 1) / 2 subarrays with odd length, that contains A[i].
A[i] will be counted ((i + 1) * (n - i) + 1) / 2 times.


Example of array [1,2,3,4,5]
1 2 3 4 5 subarray length 1
1 2 X X X subarray length 2
X 2 3 X X subarray length 2
X X 3 4 X subarray length 2
X X X 4 5 subarray length 2
1 2 3 X X subarray length 3
X 2 3 4 X subarray length 3
X X 3 4 5 subarray length 3
1 2 3 4 X subarray length 4
X 2 3 4 5 subarray length 4
1 2 3 4 5 subarray length 5

5 8 9 8 5 total times each index was added.
3 4 5 4 3 total times in odd length array with (x + 1) / 2
2 4 4 4 2 total times in even length array with x / 2


Complexity
Time O(N)
Space O(1)

"""


class SolutionLee:
    def sumOddLengthSubarrays(self, arr) -> int:
        res = 0
        n = len(arr)
        for i, num in enumerate(arr):
            res += ((i + 1) * (n - i) + 1) // 2 * arr[i]
        return res


class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:
        res = 0
        n = len(arr)

        for i in range(n):
            end = i + 1
            start = n - i
            total = start * end
            odd = total // 2
            if total % 2 == 1:
                odd += 1
            res += odd * arr[i]

        return res




class SolutionTony:
    def sumOddLengthSubarrays(self, arr) -> int:
        res = 0
        n = len(arr)
        for k in range(1, n + 1, 2):
            for t in range(n - k + 1):
                res += sum(arr[t:t + k])

        return res


