
"""
A sequence of numbers is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given.
A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk)
such that 0 ≤ P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic
if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic. In particular, this means that k ≥ 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers. Every integer is in the range of -231 and 231-1 and 0 ≤ N ≤ 1000.
The output is guaranteed to be less than 231-1.


Example:

Input: [2, 4, 6, 8, 10]

Output: 7

Explanation:
All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
"""

"""
We memoize with an array of dicts, dp, 
such that dp[i][j] stores the number of arithmetic slices 
(including those with only length 2) whose constant difference is j ending at i. 
The key is basically to store all 2+-length arithmetic slices 
(which is helps to build up the solution from its sub-problems) while only adding valid 3+-length slices to the total.

The we iterate over all pairs in the array. 
Each (A[j], A[i]) is a 2-length slice with constant difference A[i] - A[j] that we've never encountered before, 
so increment dp[i][A[i] - A[j]] by 1 (but leave the total as is, because its not length 3 or more).

If there are any slices with A[i] - A[j] length that finish at index j (if A[i]-A[j] in dp[j]:), 
we 'extend' them to index i and add to the total, 
since any slice that terminated at index j would now have at least length 3 terminating at i.
"""


import collections
class Solution2:
    def numberOfArithmeticSlices(self, A):
        dp, lookup, res = [{} for _ in range(len(A))], collections.defaultdict(list), 0
        for i in range(len(A)):
            lookup[A[i]].append(i)
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                X = A[j] - diff
                if X in lookup:
                    for idx in lookup[X]:
                        if idx < j:
                            dp[i][diff] = dp[i].get(diff, 0) + 1
                if diff in dp[j]:
                    dp[i][diff] = dp[i].get(diff, 0) + dp[j][diff]
        for x in dp:
            for k in x:
                res += x[k]
        return res


class Solution3:
    def numberOfArithmeticSlices(self, A):
        dp, res = collections.defaultdict(dict), 0
        for j in range(len(A)):
            for i in range(j):
                dp[j][A[j] - A[i]] = dp[j].get(A[j] - A[i], 0) + dp[i].get(A[j] - A[i], 1)
                if A[j] - A[i] in dp[i]: res, dp[j][A[j] - A[i]] = res + dp[i][A[j] - A[i]], dp[j][A[j] - A[i]] + 1
        return res


"""
Dynamic Programming Solution

sub_problem[i,d] = Number of arthimetic sequences of length 2 
or more which end at index i and have difference as d. Note we said length 2 or more and not 3.
Say we have an array called cache where every element of cache is a dictionary. 
The key for dictionary is difference d and value is number of sequences which end at i with difference d.
sub_problem[i,d] = sub_problem[j,d] + 1 iff A[i]-A[j] == d. 
The 1 in this equation represents the new subsequence of size 2 comprising of A[j], A[i]. Imagine array [2,2,3,4]. Say we are at index 2. 
Now we want to find the distribution of all sequences which end at index 2. 
Now for index 1 and 0, we notice a size 2 sequence of (2,3) and (2,3). These two would be added in the count of all subsequences ending at i.
We maintain a count of all size 2 subsequences and call it subs_len_2. 
Once we are done processing an index, we add all subsequences which end at index i to result. 
Finally we remove the count of size 2 subsequences from result and return the result.
"""

from collections import defaultdict
class Solution4:
    def numberOfArithmeticSlices(self, A):
        cache = [defaultdict(int) for _ in range(len(A))]
        result, subs_len_2 = 0, 0
        for i in range(1, len(A)):
            for j in range (i-1,-1,-1):
                curr_diff = A[i]-A[j]
                cache[i][curr_diff], subs_len_2 = cache[i][curr_diff]+1, subs_len_2+1
                if curr_diff in cache[j]:
                    cache[i][curr_diff] += cache[j][curr_diff]
            result += sum(cache[i].values())
        return result - subs_len_2

"""
Succinct Code
The above code can be made a bit more clever so that we do not need to maintain a count of size 2 subsequences.
"""
class Solution5:
    def numberOfArithmeticSlices(self, A):

        cache = [{} for _ in range(len(A))]
        result = 0
        for i in range(1, len(A)):
            for j in range (i-1,-1,-1):
                curr_diff = A[i]-A[j]
                cache[i].setdefault(curr_diff, 0)
                cache[i][curr_diff] += 1
                if curr_diff in cache[j]:
                    cache[i][curr_diff] += cache[j][curr_diff]
                    result += cache[j][curr_diff]
        return result


"""
Same idea with "https://discuss.leetcode.com/topic/67012/java-15-lines-solution".

Iterate trough A and for each number A[i], get the diff with all the previous nums A[j], 
0<=j<i. If A[j] also has the same diff, then it means we've found an Arithmetic Slice.
"""
class Solution6:
    def numberOfArithmeticSlices(self, A):
        result, dp = 0, [{} for _ in A]
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = dp[i].get(diff, 0) + 1
                if diff in dp[j]:
                    result += dp[j][diff]
                    dp[i][diff] += dp[j][diff]
        return result




