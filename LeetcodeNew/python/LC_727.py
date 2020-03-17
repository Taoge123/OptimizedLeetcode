
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        pass



"""
dp[i][j] stores the starting index of the substring where T has length i and S has length j.

So dp[i][j would be:
if T[i - 1] == S[j - 1], this means we could borrow the start index from dp[i - 1][j - 1] to make the current
substring valid;
else, we only need to borrow the start index from dp[i][j - 1] which could either exist or not.

Finally, go through the last row to find the substring with min length and appears first.

    int m = T.length(), n = S.length();
    int[][] dp = new int[m + 1][n + 1];
    for (int j = 0; j <= n; j++) {
        dp[0][j] = j + 1;
    }

    for (int i = 1; i <= m; i++) {




































































































































        for (int j = 1; j <= n; j++) {
            if (T.charAt(i - 1) == S.charAt(j - 1)) {
                dp[i][j] = dp[i - 1][j - 1];
            } else {
                dp[i][j] = dp[i][j - 1];
            }
        }
    }
    int start = 0, len = n + 1;
    for (int j = 1; j <= n; j++) {
        if (dp[m][j] != 0) {
            if (j - dp[m][j] + 1 < len) {
                start = dp[m][j] - 1;
                len = j - dp[m][j] + 1;
            }
        }
    }
    return len == n + 1 ? "" : S.substring(start, start + len);
}
                 j
     a  b  c  d  e  b  d  d  e
  1  2  3  4  5. 6  7  8  9. 10
b 0  0. 2  2  2  2  6  6  6  6
d 0  0  0  0  2  2  2  6  6  6
e 0  0  0  0  0  2  2  2  2  6

                 j
     a  b  c  d  e  b  d  d  e
  1  2  3  4  5. 6  7  8  9. 10
e 0  0. 0  0. 0  5. 5  5. 5  5.
e 0  0  0  0  0  0. 0  0  0  5


e 0  0  0  0  0  0. 0  0  0  0


S = "abcdebdde"
T = "bde"

   b    d     e
a  -1.  -1    -1
b  b.   -1.   -1
c  bc.  -1    -1
d  bcd. bcd.  -1
e  bcde.  bcd.  bde
b  bcde.  bcd.  bde
d  bcd.  bcd.  bde
d  b.   bd   bde
e  b.   bd   bde

"""





