"""
Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length,
then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.



Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.


Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]

"""
"""
找到最大的数字，假设它的下标是i
反转0到i之间的数字，使得A[i]变成第一个数
反转整个数组，让最大的数到末尾
"""
"""
Explanation
Find the index i of the next maximum number x.
Reverse i + 1 numbers, so that the x will be at A[0]
Reverse x numbers, so that x will be at A[x - 1].
Repeat this process N times.

Update:
Actually, I didn't use the condition permutation of [1,2,..., A.length].
I searched in the descending order of A.

Time Complexity:
O(N^2)

My idea is keep placing the kth smallest value at kth place by 2 (or 1 or 0) flips and k ranges from n to 1. So I call kth smallest value as a bottom value since it's the largest value in current iteration which should be placed at current bottom place.

The method is to find the index of current kth smallest value k, saying i, then make an i-swap. It will reverse first i elements so k will be swapped to the 1st place. Then I make a k-swap to make k reversed to the kth place.

For example A = [3,2,4,1]. First number I need to handle is 4. To place 4 to 4th place, I first make a 3-swap to place 4 to the 1st place([4,2,3,1]), then make a 4-swap to place 4 to the 4th place([1,3,2,4]).

Before these swaps, if k is already at the kth place, there is no need to swap at all. If k is already at the 1st place, then there is no need for the first i-swap. After the swaps, A will be updated to A[:i:-1] + A[:i]. 
(A[:i] is swapped twice so its internal sequence remains but it's placed after reversed(A[i+1:]). A[i+1:] is swapped once so its sequence is reversed to A[:i:-1]. A[i] is fixed since then so there is no need to include it for the next swaps).
"""


class Solution:
    def pancakeSort(self, A):
        res = []
        for x in range(len(A), 1, -1):
            i = A.index(x)
            res.extend([i+1, x])
            left = A[:i:-1]
            right = A[:i]
            print(left, right)
            # reversed(A[i+1:]) + A[:i], exclude k or A[i] after each iteration
            A = A[:i:-1] + A[:i]
            print(A, '-')

        return res


class Solution2:
    def pancakeSort(self, A):
        n = len(A)
        res = []
        for i in range(n):
            cur_max = max(A[0:n - i])
            j = 0
            while A[j] != cur_max:
                j += 1
            # should reverse j+1 elements
            A[:j + 1] = reversed(A[:j + 1])
            res.append(j + 1)
            # reverse all
            A[:n - i] = reversed(A[:n - i])
            res.append(n - i)
        return res



# A = [1,2,3,4,5,6,7,8,9]
A = [9,8,7,6,5,4,3,2,1]
a = Solution()
print(a.pancakeSort(A))



