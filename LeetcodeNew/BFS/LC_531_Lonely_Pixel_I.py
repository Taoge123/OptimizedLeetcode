"""
思路：
这道题定义了一种孤独的黑像素，就是该黑像素所在的行和列中没有其他的黑像素，
让我们找出所有的这样的像素。那么既然对于每个黑像素都需要查找其所在的行和列，
为了避免重复查找，我们可以统一的扫描一次，将各行各列的黑像素的个数都统计出来，
然后再扫描所有的黑像素一次，看其是否是该行该列唯一的存在，是的话就累加计数器即可
(也可以在原数组上存，减少Space)

"""
class Solution:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        rows, cols = [0] * len(picture),  [0] * len(picture[0])
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1

        result = 0
        for i in range(len(picture)):
            if rows[i] == 1:
                for j in range(len(picture[0])):
                     result += picture[i][j] == 'B' and cols[j] == 1
        return result


class Solution2:
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        row = [0] * len(picture)
        col = [0] * len(picture[-1])

        for i in range(len(picture)):
            for j in range(len(picture[-1])):
                if picture[i][j] == 'B':
                    row[i] += 1
                    col[j] += 1
        row_1 = sum([1 for i in row if i == 1])
        col_1 = sum([1 for i in col if i == 1])
        return min(row_1, col_1)


