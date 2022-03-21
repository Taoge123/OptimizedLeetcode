import collections


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        prevColor = image[sr][sc]

        if (prevColor != newColor):
            self.floodFillUtil(image, sr, sc, prevColor, newColor)

        return image

    def floodFillUtil(self, image, sr, sc, prevColor, newColor):

        R = len(image)
        C = len(image[0])

        if (sr >= 0 and sr < R and sc >= 0 and sc < C and image[sr][sc] == prevColor):
            image[sr][sc] = newColor
            self.floodFillUtil(image, sr + 1, sc, prevColor, newColor)
            self.floodFillUtil(image, sr - 1, sc, prevColor, newColor)
            self.floodFillUtil(image, sr, sc + 1, prevColor, newColor)
            self.floodFillUtil(image, sr, sc - 1, prevColor, newColor)




class SolutionBFS:
    def floodFill(self, image, sr: int, sc: int, newColor: int):

        m, n = len(image), len(image[0])
        queue = collections.deque()
        queue.append((sr, sc))
        visited = set()
        old_color = image[sr][sc]
        while queue:
            i, j = queue.popleft()
            image[i][j] = newColor

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != old_color:
                    continue
                if (x, y) in visited:
                    continue
                visited.add((x, y))
                queue.append((x, y))

        return image



