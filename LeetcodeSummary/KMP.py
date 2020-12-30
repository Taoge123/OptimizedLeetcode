"""
1392. Longest Happy Prefix
1397. Find All Good Strings



"""


def LPS(self, pattern):
    M = len(pattern)
    lps = [0] * M
    i, j = 1, 0
    while i < M:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1
    return lps



