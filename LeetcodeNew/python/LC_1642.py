
import heapq


class SolutionTony:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        diffs = []
        for i in range(len(heights) - 1):
            diffs.append(heights[i + 1] - heights[i])

        res = 0
        for i in range(len(diffs)):
            if diffs[i] <= 0:
                res += 1
            elif bricks >= diffs[i]:
                bricks -= diffs[i]
                res += 1
            elif ladders >= 1:
                ladders -= 1
                res += 1
            else:
                return res
        return res



class Solution2:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        n = len(heights)
        heap = []

        for i in range(1, n):
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                continue
            heapq.heappush(heap, diff)
            if len(heap) <= ladders:
                continue
            bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i - 1

        return n - 1






