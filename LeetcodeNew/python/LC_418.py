
"""
https://www.bilibili.com/video/BV16P4y1E75D?vd_source=c5928795c3e6210df961484faf790a47
https://github.com/wisdompeak/LeetCode/tree/master/String/418.Sentence-Screen-Fitting

"""


class Solution:
    def wordsTyping(self, sentence, rows, cols):

        s = ' '.join(sentence) + ' '
        start = 0
        n = len(s)
        for _ in range(rows):
            start += cols
            # 不能fit就回到上个空格，后面的重新算
            while s[start % n] != ' ':
                start -= 1
            start += 1
        return start // n




rows = 4
cols = 8
sentence = ["hello", "world"]

a = Solution()
print(a.wordsTyping(sentence, rows, cols))




