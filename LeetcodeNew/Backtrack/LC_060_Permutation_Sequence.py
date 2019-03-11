
"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

"""

"""
The idea is as follow:

For permutations of n, the first (n-1)! permutations start with 1, next (n-1)!
ones start with 2, ... and so on. And in each group of (n-1)! permutations, 
the first (n-2)! permutations start with the smallest remaining number, ...

take n = 3 as an example, the first 2 (that is, (3-1)! ) 
permutations start with 1, next 2 start with 2 and last 2 start with 3. 
For the first 2 permutations (123 and 132), the 1st one (1!) starts with 2, 
which is the smallest remaining number (2 and 3). 
So we can use a loop to check the region that the sequence number falls in and get the starting digit. 
Then we adjust the sequence number and continue.
"""


import math
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation


class Solution2:
    def getPermutation(self, n, k):
        res, nums = "", range(1, n + 1)
        k -= 1
        while n:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            res += str(nums.pop(index))
        return res







