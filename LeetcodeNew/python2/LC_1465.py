
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:

        horizontal = [0] + sorted(horizontalCuts) + [h]
        vertical = [0] + sorted(verticalCuts) + [w]

        maxStripWidth = max([horizontal[i + 1] - horizontal[i] for i in range(len(horizontal) - 1)])
        maxStripHeight = max([vertical[i + 1] - vertical[i] for i in range(len(vertical) - 1)])

        return (maxStripWidth * maxStripHeight) % ((10 ** 9) + 7)


