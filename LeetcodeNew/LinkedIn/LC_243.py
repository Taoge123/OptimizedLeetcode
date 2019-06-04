# O(n*n) time
def shortestDistance(self, words, word1, word2):
    res = len(words)
    for i in xrange(len(words)):
        if words[i] == word1:
            res = min(res, self.helper(words, i, word2))
    return res

# go from middle point to both sides,
# like: https://leetcode.com/problems/longest-palindromic-substring/
def helper(self, words, i, word2):
    j = 0
    while (i-j<0 or words[i-j]!=word2) and (i+j>=len(words) or words[i+j]!=word2):
        j += 1
    return j


def shortestDistance(self, words, word1, word2):
    size = len(words)
    index1, index2 = size, size
    ans = size

    for i in xrange(size):
        if words[i] == word1:
            index1 = i
            ans = min(ans, abs(index1 - index2))
        elif words[i] == word2:
            index2 = i
            ans = min(ans, abs(index1 - index2))
    return ans


