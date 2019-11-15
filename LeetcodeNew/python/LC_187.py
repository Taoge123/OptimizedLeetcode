"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

"""


class Solution:
    def findRepeatedDnaSequences(self, s):

        visited = set()
        res = set()
        for i in range(len(s) - 9):
            word = s[i:i + 10]
            if word in visited:
                res.add(word)
            else:
                visited.add(word)
        return list(res)





