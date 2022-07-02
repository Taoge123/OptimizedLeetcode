"""
https://leetcode.com/problems/erect-the-fence/discuss/1442266/A-Detailed-Explanation-with-Diagrams-(Graham-Scan)
https://www.youtube.com/watch?v=B2AJoQSZf4M


"""


class SolutionBest:
    def outerTrees(self, trees):
        def cmp(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2
            x3, y3 = p3

            return (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)

        points = sorted(trees)

        lower = []
        upper = []
        for point in points:
            while len(lower) >= 2 and cmp(lower[-2], lower[-1], point) < 0:
                lower.pop()
            while len(upper) >= 2 and cmp(upper[-2], upper[-1], point) > 0:
                upper.pop()

            lower.append(tuple(point))
            upper.append(tuple(point))

        return list(set(lower + upper))





class Solution:

    def outerTrees(self, points):
        if len(points) <= 2:
            return points

        points.sort(key=lambda x: (x[0], x[1]))
        stack = []
        for i in range(len(points)):
            while len(stack) >= 2 and self.crossProduct(points[i], stack[-2], stack[-1]) > 0:
                stack.pop()

            stack.append(points[i])

        stack.pop()

        for i in range(len(points) - 1, -1, -1):
            while len(stack) >= 2 and self.crossProduct(points[i], stack[-2], stack[-1]) > 0:
                stack.pop()

            stack.append(points[i])

        stack.pop()

        return set(map(tuple, stack))

    def crossProduct(self, a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])



