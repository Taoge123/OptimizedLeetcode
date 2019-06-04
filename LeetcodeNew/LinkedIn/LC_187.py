# Time O(n) one pass, Space O(10*n)
def findRepeatedDnaSequences1(self, s):
    res, dic = [], {}
    for i in xrange(len(s) - 9):
        if s[i:i + 10] not in dic:
            dic[s[i:i + 10]] = 1
        elif dic[s[i:i + 10]] == 1:
            res.append(s[i:i + 10])
            dic[s[i:i + 10]] = 2
    return res


# Time O(n) one pass, Space O(4*n)
def findRepeatedDnaSequences(self, s):
    res = []
    dic = {"A": 1, "C": 2, "G": 3, "T": 4}
    dicDNA = {}
    num = 1
    for i in xrange(len(s)):
        num = (num * 4 + dic[s[i]]) & 0XFFFFF
        if i < 9:
            continue
        if num not in dicDNA:
            dicDNA[num] = 1
        elif dicDNA[num] == 1:
            res.append(s[i - 9:i + 1])
            dicDNA[num] = 2
    return res
1