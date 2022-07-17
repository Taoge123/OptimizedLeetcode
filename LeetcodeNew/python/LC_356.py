
class Solution:
    def isReflected(self, points) -> bool:
        if not points:
            return True

        mini = min(i[0] for i in points)
        maxi = max(i[0] for i in points)
        table = set()
        for i in points:
            table.add(tuple(i))
        for i in points:
            if (mini + maxi - i[0], i[1]) not in table:
                return False
        return True


points = [[1,1],[-1,1]]
a = Solution()
print(a.isReflected(points))



