"""
https://www.youtube.com/watch?v=sgDdhNTByLQ

"""


class Solution:
    def pourWater(self, heights, V: int, K: int):
        while V:
            self.drop(heights, K)
            V -= 1
        return heights

    def drop(self, heights, K):
        best = K
        for d in range(-1, 2, 2):
            i = K + d
            while i>= 0 and i < len(heights) and heights[i] <= heights[i - d]:
                if heights[i] < heights[best]:
                    best = i
                i += d

            if best != K:
                break
        heights[best] += 1


