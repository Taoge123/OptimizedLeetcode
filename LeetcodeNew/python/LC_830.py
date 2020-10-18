class Solution:
    def largeGroupPositions(self, s):
        res = []
        i = 0  # The start of each group
        for j in range(len(s)):
            if j == len(s) - 1 or s[j] != s[j + 1]:
                # Here, [i, j] represents a group.
                if j - i + 1 >= 3:
                    res.append([i, j])
                i = j + 1
        return res

