"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.

"""


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:

        nums = []
        res = 0
        for i in range(len(low), len(high) + 1):
            nums.extend(self.helper(i, i))

        # Need to convert the values into num to compare
        low, high = int(low), int(high)
        for num in nums:
            num = int(num)
            if num >= low and num <= high:
                res += 1

        return res

    def helper(self, n, length):

        if n == 0:
            return [""]
        elif n == 1:
            return ["0", "1", "8"]

        middles = self.helper(n -2, length)
        res = []
        for middle in middles:
            if n != length:
                res.append("0" + middle + "0")
            res.append("1" + middle + "1")
            res.append("6" + middle + "9")
            res.append("8" + middle + "8")
            res.append("9" + middle + "6")

        return res



