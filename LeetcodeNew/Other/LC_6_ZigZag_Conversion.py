class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        res = [''] * numRows
        index, step = 0, 1

        for char in s:
            res[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(res)

s = "PAYPALISHIRING"
numRows = 4

a = Solution()
print(a.convert(s, numRows))













