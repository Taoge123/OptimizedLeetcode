
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



