
class Solution:
    def numberOfLines(self, widths, S: str):
        lines = 1
        width = 0
        for ch in S:
            w = widths[ord(ch) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w
        return [lines, width]


