
"""
363	Max Sum of Rectangle No Larger Than K

For those who do not understand the logic behind this code at first glance as I, here is my explanation to help you understand:

1. calculate prefix sum for each row
for (int i = 0; i < m; i++)
    for (int j = 1; j < n; j++)
        A[i][j] += A[i][j - 1];
For this double-for loop, we are calculating the prefix sum for each row in the matrix, which will be used later

2. for every possible range between two columns, accumulate the prefix sum of submatrices that can be formed between these two columns by adding up the sum of values between these two columns for every row
for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
        Map<Integer, Integer> counter = new HashMap<>();
        counter.put(0, 1);
        int cur = 0;
        for (int k = 0; k < m; k++) {
            cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
            res += counter.getOrDefault(cur - target, 0);
            counter.put(cur, counter.getOrDefault(cur, 0) + 1);
        }
    }
}


To understand what this triple-for loop does, let us try an example, assume i = 1 and j = 3, then for this part of code:

Map<Integer, Integer> counter = new HashMap<>();
counter.put(0, 1);
int cur = 0;
for (int k = 0; k < m; k++) {
    cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
    res += counter.getOrDefault(cur - target, 0);
    counter.put(cur, counter.getOrDefault(cur, 0) + 1);
}
I will break this piece of code into two major part:

Map<Integer, Integer> counter = new HashMap<>();
counter.put(0, 1);
key of this hashmap present the unique value of all possible prefix sum that we've seen so far
value of this hashmap represents the count (number of appearances) of each prefix sum value we've seen so far
an empty submatrix trivially has a sum of 0
for (int k = 0; k < m; k++) {
    cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
    res += counter.getOrDefault(cur - target, 0);
    counter.put(cur, counter.getOrDefault(cur, 0) + 1);
}
Here we are actually calculating the prefix sum of submatrices which has column 1, 2, and 3, by adding up the sum of matrix[0][1...3], matrix[1][1...3] ... matrix[m-1][1...3] row by row, starting from the first row (row 0). The way of getting the number of submatrices whose sum equals to K uses the same idea of 560. Subarray Sum Equals K so I won't repeat it again.

Hope it helps



"""

import collections

class Solution:
    def numSubmatrixSumTarget(self, matrix, target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(n - 1):
                row[i + 1] += row[i]

        res = 0
        for left in range(n):
            for right in range(left, n):
                count = collections.defaultdict(int)
                cur = 0
                count[0] = 1
                for k in range(m):
                    cur += matrix[k][right] - (matrix[k][left - 1] if left > 0 else 0)
                    res += count[cur - target]
                    count[cur] += 1

        return res




