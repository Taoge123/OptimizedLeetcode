class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        n = len(s)
        m = len(p)

        M = [[False for x in range(m + 1)] for y in range(n + 1)]
        M[0][0] = True

        for j in range(2, m + 1):
            if p[j - 1] == "*":
                M[0][j] = M[0][j - 2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == ".":
                    M[i][j] = M[i - 1][j - 1]
                elif p[j - 1] == "*":
                    if M[i][j - 2] or M[i][j - 1] or ((p[j - 2] == "." or p[j - 2] == s[i - 1]) and M[i - 1][j]):
                        M[i][j] = True
                else:
                    M[i][j] = M[i - 1][j - 1] and p[j - 1] == s[i - 1]

        return M[n][m]


