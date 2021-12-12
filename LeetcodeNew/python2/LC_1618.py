
# class Solution1:
#     def trimMean(self, arr) -> float:
#         n = len(arr)
#         return sum(sorted(arr)[n // 20: -n // 20]) / (n * 9 // 10)
#

# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
# class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
#
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """

class Solution:
    def maxFont(self, text, w, h, fonts, fontInfo):
        l, r = 0, len(fonts) - 1
        while l <= r:
            m = l + (r - l) // 2
            height = fontInfo.getHeight(fonts[m])
            width = 0
            for ch in text:
                width += fontInfo.getWidth(fonts[m], ch)
            if height <= h and width <= w:
                l = m + 1
            else:
                r = m - 1
        return fonts[r] if r >= 0 else -1

