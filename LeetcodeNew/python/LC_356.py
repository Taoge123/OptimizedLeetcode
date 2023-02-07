
class Solution:
    def isReflected(self, points) -> bool:

        left = min(point[0] for point in points)
        right = max(point[0] for point in points)

        table = set()
        # add all pints
        for i, j in points:
            table.add((i, j))

        for i, j in points:
            # If the reflected point not in points set
            if (left + right - i, j) not in table:
                return False
        return True


points = [[1,1],[-1,1]]
a = Solution()
print(a.isReflected(points))



