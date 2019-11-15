"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]

"""


class Solution:
    def findStrobogrammatic(self, n):

        return self.helper(n, n)

    def helper(self, n, length):

        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]

        middles = self.helper( n -2, length)
        res = []
        for middle in middles:
            if n != length:
                res.append("0" + middle + "0")
            res.append("1" + middle + "1")
            res.append("6" + middle + "9")
            res.append("8" + middle + "8")
            res.append("9" + middle + "6")
        return res




