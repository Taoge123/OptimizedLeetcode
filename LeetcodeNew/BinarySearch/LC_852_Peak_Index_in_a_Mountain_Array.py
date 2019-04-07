
"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i
such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""


class SolutionLee1:
    def peakIndexInMountainArray(self, A):
        return A.index(max(A))


class SolutionLee2:
    def peakIndexInMountainArray(self, A):
        l, r = 0, len(A) - 1
        while l < r:
            mid = (l + r) // 2
            if A[mid] < A[mid + 1]:
                l = mid
            elif A[mid - 1] > A[mid]:
                r = mid
            else:
                return mid


"""
Because the array is sorted in some sense, you can use binary search. 
If the midpoint is less than the values on the left and right, 
then you know you reached the mountain.
If the midpoint index is bigger than the value to the left of it, 
but less than the value to the right, then you know you are on the ascending part of the mountain, 
so the peak is to the right, so shift search space to the right. 
If midpoint index is bigger than the value to the right of it but less than the value to the left of it, 
then you know you are on the descending part of the mountain, so shift search space to the left.
"""


class Solution1:
    def peakIndexInMountainArray(self, A):

        low = 0
        high = len(A) - 1
        peak = 0

        while low <= high:
            mid = low + (high - low) // 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                peak = mid
                break
            elif A[mid - 1] < A[mid] < A[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        return peak


class Solution2:
    def peakIndexInMountainArray(self, A):

        low, high = 0, len(A) - 1
        peak = 0

        while low <= high:
            mid = low + (high - low) // 2
            if A[mid - 1] < A[mid] > A[mid + 1]:
                peak = mid
                return peak
            elif A[mid - 1] < A[mid]:
                low = mid + 1
            else:
                high = mid - 1



A = [0,2,1,0]
a = Solution1()
print(a.peakIndexInMountainArray(A))



