
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = 0
        watermark = 0
        for ch in croakOfFrogs:
            if ch == 'c':
                c += 1
                watermark = max(watermark, c - k)
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            elif ch == 'k':
                k += 1
            else:
                return -1
            if not c >= r >= o >= a >= k:
                return -1
        return watermark if c == r == o == a == k else -1





