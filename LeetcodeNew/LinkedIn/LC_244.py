

def __init__(self, words):
    self.dic, self.l = {}, len(words)
    for i, w in enumerate(words):
        self.dic[w] = self.dic.get(w, []) + [i]

# @param {string} word1
# @param {string} word2
# @return {integer}
# Adds a word into the data structure.
def shortest(self, word1, word2):
    l1, l2 = self.dic[word1], self.dic[word2]
    i = j = 0
    res = self.l
    # O(m+n) time complexity
    while i < len(l1) and j < len(l2):
        res = min(res, abs(l1[i]-l2[j]))
        if l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return res


