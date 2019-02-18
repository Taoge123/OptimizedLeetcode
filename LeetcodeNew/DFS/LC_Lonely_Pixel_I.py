

"""
Go through the columns, count how many have exactly one black pixel
and it's in a row that also has exactly one black pixel.
"""

class Solution1:
    def findLonelyPixel(self, picture):
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))


"""
这道题定义了一种孤独的黑像素，就是该黑像素所在的行和列中没有其他的黑像素，
让我们找出所有的这样的像素。那么既然对于每个黑像素都需要查找其所在的行和列，为了避免重复查找，
我们可以统一的扫描一次，将各行各列的黑像素的个数都统计出来，然后再扫描所有的黑像素一次，
看其是否是该行该列唯一的存在，是的话就累加计数器即可
"""


class Solution2:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        w, h = len(picture), len(picture[0])
        rows, cols = [0] * w, [0] * h
        for x in range(w):
            for y in range(h):
                if picture[x][y] == 'B':
                    rows[x] += 1
                    cols[y] += 1
        ans = 0
        for x in range(w):
            if rows[x] == 1:
                for y in range(h):
                    if picture[x][y] == 'B':
                        if cols[y] == 1:
                            ans += 1
        return ans


picture =  [['W', 'W', 'B'],
            ['W', 'B', 'W'],
            ['B', 'W', 'W']]

a = Solution2()
print(a.findLonelyPixel(picture))
