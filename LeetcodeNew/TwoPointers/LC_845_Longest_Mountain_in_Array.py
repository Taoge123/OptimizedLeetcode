
"""
https://leetcode.com/problems/longest-mountain-in-array/discuss/180347/Python-using-state-machine-thinking

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""

class Solution1:
    def longestMountain(self, A):
        N = len(A)
        ans = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: #if base is a left-boundary
                #set end to the peak of this potential mountain
                while end+1 < N and A[end] < A[end+1]:
                    end += 1

                if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
                    #set 'end' to right-boundary of mountain
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                    #record candidate answer
                    ans = max(ans, end - base + 1)

            base = max(end, base + 1)

        return ans


"""
Intuition:
We have already many 2-pass or 3-pass problems, like 821. Shortest Distance to a Character.
They have almost the same idea.
One forward pass and one backward pass.
Maybe another pass to get the final result, or you can merge it in one previous pass.

Explanation:
In this problem, we take one forward pass to count up hill length (to every point).
We take another backward pass to count down hill length (from every point).
Finally a pass to find max(up[i] + down[i] + 1) where up[i] and down[i] should be positives.

Time Complexity:
O(N)

"""

class SolutionLee:

    def longestMountain(self, A):
        up, down = [0] * len(A), [0] * len(A)
        for i in range(1, len(A)):
            if A[i] > A[i - 1]: up[i] = up[i - 1] + 1
        for i in range(len(A) - 1)[::-1]:
            if A[i] > A[i + 1]: down[i] = down[i + 1] + 1
        return max([u + d + 1 for u, d in zip(up, down) if u and d] or [0])

"""
Can you solve this problem with only one pass?
Can you solve this problem in O(1) space?

In this solution, I count up length and down length.
Both up and down length are clear to 0 when A[i - 1] == A[i] or down > 0 && A[i - 1] < A[i].
"""

class SolutionLeeFollowUp:
    def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)
        return res


class Solution2:
    def longestMountain(self, A, res = 0):
        for i in range(1, len(A) - 1):
            if A[i + 1] < A[i] > A[i - 1]:
                l = r = i
                while l and A[l] > A[l - 1]: l -= 1
                while r + 1 < len(A) and A[r] > A[r + 1]: r += 1
                if r - l + 1 > res: res = r - l + 1
        return res


"""
Thought process:
Because we have a subarray that expands from a central point where the central point is the highest value, and our array min length is 3,
intuitively, we should know that there is a 'expanding window' of min size 3. 
Therefore we start the problem by creating a iterative loop start at index 1 to index len(A) - 2, 
since we don't need to check index 0 or index len(A) - 1 as central indices.

With our windows decided, first we need to check if the starting values on the left, 
and right of the center value are less than the center value.
If either of them aren't, we skip this window.

If the conditions of the base window are satisfied then all we have to do is loop the left, 
and right side, and make sure each successive value is less than that of the previous. 
However the left and right side are independent of each other, 
meaning if the left side encounters a value that is higher than the previous, 
does not mean the right side stops checking for the next value.

Once the width of our subarray is identify, then we continue 
from where the end of our subarray was to check for other subarrays that may be greater
"""


class Solution4:
    def longestMountain(self, A):
        longest_chain = 0

        for i in range(1, len(A) - 1):
            begin, end = i - 1, i + 1

            if A[begin] < A[i] and A[end] < A[i]:
                while begin > 0:
                    if A[begin] > A[begin - 1]:
                        begin -= 1
                    else:
                        break

                while end < len(A) - 1:
                    if A[end] > A[end + 1]:
                        end += 1
                    else:
                        break

                longest_chain = max(longest_chain, len(A[begin:end + 1]))
                i = end + 1

        return longest_chain


"""
The idea is extremely simple and clean:

search for summits of mountain
count the length of up and down side
A typical solution for contest: not the fastest, but the safest.
"""
class Solution5:
    def longestMountain(self, A):
        s=0
        A.append(float('Inf'))
        for i in range(1,len(A)-2):
            if A[i]>A[i-1] and A[i]>A[i+1]:
                ii,jj=i-1,i+1
                while A[ii]>A[ii-1] and A[ii]<A[ii+1]: ii-=1
                while A[jj]>A[jj+1] and A[jj]<A[jj-1]: jj+=1
                s=max(s,jj-ii+1)
        return s



