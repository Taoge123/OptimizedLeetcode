"""

https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/discuss/1398600/Python-3-or-Two-Pointers-Clean-One-Pass-O(m%2Bn)-or-Explanation

"""


class Solution:
    def findRLEArray(self, encoded1, encoded2):
        left, right = 0, 0

        res = []
        while left < len(encoded1) and right < len(encoded2):
            num = encoded1[left][0] * encoded2[right][0]
            freq = min(encoded1[left][1], encoded2[right][1])

            if res and res[-1][0] == num:
                res[-1][1] += freq
            else:
                res.append([num, freq])
            encoded1[left][1] -= freq
            encoded2[right][1] -= freq

            if encoded1[left][1] == 0:
                left += 1
            if encoded2[right][1] == 0:
                right += 1

        return res


