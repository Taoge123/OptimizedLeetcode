
"""
This is essentially the same question as longest common substring.

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].


Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

"""
Approach #3: Dynamic Programming [Accepted]
Intuition and Algorithm

Since a common subarray of A and B must start at some A[i] and B[j], 
let dp[i][j] be the longest common prefix of A[i:] and B[j:]. 
Whenever A[i] == B[j], we know dp[i][j] = dp[i+1][j+1] + 1. Also, the answer is max(dp[i][j]) over all i, j.

We can perform bottom-up dynamic programming to find the answer based on this recurrence. 
Our loop invariant is that the answer is already calculated correctly and stored in dp for any larger i, j.
"""

class Solution1:
    def findLength(self, A, B):
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i+1][j+1]+1
        return max(max(row) for row in memo)


"""
dp[i][j] = a[i] == b[j] ? 1 + dp[i + 1][j + 1] : 0;
dp[i][j] : max lenth of common subarray start at a[i] & b[j];

when i == m - 1 and j == n - 1, the formular will be: dp[m-1][n-1] = A[m-1] == B[n-1] ? 1 + dp[m][n] : 0;

"""

class Solution2:
    def findLength(self, A, B):
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
        return max(max(row) for row in dp)


class Solution3:
    def findLength(self, A, B):

        m = len(A)
        n = len(B)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        maxLen = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxLen = max(maxLen, dp[i][j])

        return maxLen


"""
In order to use only one row for extra space, we update dp row from right to left as done in

for j in range(len(B)-1, -1, -1):
    dp[j+1] = 1 + dp[j] if A[i] == B[j] else 0
"""
class Solution4:
    def findLength(self, A, B):
        dp = [0] * (len(B) + 1)
        res = 0
        for i in range(len(A)):
            for j in range(len(B)-1, -1, -1):
                dp[j+1] = 1 + dp[j] if A[i] == B[j] else 0
            res = max(res, max(dp))
        return res


"""
2D -> 1D space
Time O(N^2) and Space O(N) DP Solution

dp[i][j] indicates the maximum length of repeated subarray which ends at index i-1 in A and index j-1 in B i.e. index i-1 is length i when measured from the start of the array. This gives the recurrence dp[i][j] = dp[i-1][j-1] + 1 if A[i-1] == B[j-1] else 0.
While we can initialize a 2D matrix to compute this, we really need two vectors of dimension (N+1) since the dp[i][j] just depends on the previous row.
"""

class Solution5:
    def findLength(self, A, B):

        M, N = len(A), len(B)
        dp, temp = [0]*(N+1), [0]*(N+1)
        ans = 0
        for i in range(1, M+1):
            for j in range(1, N+1):
                dp[j] = temp[j-1] + 1 if A[i-1] == B[j-1] else 0
            ans = max(ans, max(dp))
            temp, dp = dp, temp
        return ans



