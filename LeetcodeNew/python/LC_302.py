"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6
"""

"""
Suppose we have a 2D array

"000000111000000"
"000000101000000"
"000000101100000"
"000001100100000"
Imagine we project the 2D array to the bottom axis with the rule "if a column has any black pixel it's projection is black otherwise white". The projected 1D array is

"000001111100000"
Theorem

If there are only one black pixel region, then in a projected 1D array all the black pixels are connected.

Proof by contradiction

Assume to the contrary that there are disconnected black pixels at i
and j where i < j in the 1D projection array. Thus there exists one
column k, k in (i, j) and and the column k in the 2D array has no
black pixel. Therefore in the 2D array there exists at least 2 black
pixel regions separated by column k which contradicting the condition
of "only one black pixel region".

Therefore we conclude that all the black pixels in the 1D projection
array is connected.

This means we can do a binary search in each half to find the boundaries, if we know one black pixel's position. And we do know that.

To find the left boundary, do the binary search in the [0, y) range and find the first column vector who has any black pixel.

To determine if a column vector has a black pixel is O(m) so the search in total is O(m log n)

We can do the same for the other boundaries. The area is then calculated by the boundaries.
Thus the algorithm runs in O(m log n + n log m)
"""

import collections


class SolutionRika:
    def minArea(self, image, x, y):
        # to find the rectangle to cover all "1", need to find "1" in leftest, righest, top and bottom
        # calculate the areas

        m,n = len(image), len(image[0])
        queue = collections.deque()
        queue.append((x,y))
        minX, maxX, maxY,minY= x,x,y,y
        visited = set()
        visited.add((x,y))
        while queue:
            i,j = queue.popleft()
            for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and image[x][y] == 1 and (x, y) not in visited:
                    queue.append((x, y))
                    visited.add((x, y))
                    minX = min(minX, x)
                    maxX = max(maxX, x)
                    minY = min(minY, y)
                    maxY = max(maxY, y)

        return (maxX-minX+1)*(maxY-minY+1)


class SolutionTony:
    def minArea(self, image, x, y):
        m, n = len(image), len(image[0])
        queue = collections.deque()
        queue.append([x, y])
        visited = set()
        visited.add((x, y))
        minr, minc, maxr, maxc = m + 1, n + 1, -1, -1
        while queue:
            i, j = queue.popleft()
            minr, minc, maxr, maxc = min(minr, i), min(minc, j), max(maxr, i), max(maxc, j)
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x = i + dx
                y = j + dy
                if x < 0 or x >= m or y < 0 or y >= n or image[x][y] == "0" or (x, y) in visited:
                    continue
                visited.add((x, y))
                queue.append([x, y])
        return (maxr - minr + 1) * (maxc - minc + 1)




class Solution:
    def minArea(self, image, x, y):
        top = self.searchRows(image, 0, x, True)
        bottom = self.searchRows(image, x + 1, len(image), False)
        left = self.searchColumns(image, 0, y, top, bottom, True)
        right = self.searchColumns(image, y + 1, len(image[0]), top, bottom, False)
        return (right - left) * (bottom - top)

    def searchRows(self, image, top, bottom, opt):
        while top < bottom:
            m = (top + bottom) // 2
            if ('1' in image[m]) == opt:
                bottom = m
            else:
                top = m + 1
        return top

    def searchColumns(self, image, left, right, top, bottom, opt):
        while left < right:
            m = (left + right) // 2
            if any(image[k][m] == '1' for k in range(top, bottom)) == opt:
                right = m
            else:
                left = m + 1
        return left



class SolutionDFS:
    def minArea(self, image, x, y):
        left, right, up, down, m, n = [y], [y], [x], [x], len(image), len(image[0])
        self.dfs(image, x, y, left, right, up, down, m, n)
        return (right[0] - left[0] + 1) * (down[0] - up[0] + 1)

    def dfs(self, image, i, j, left, right, up, down, m, n):
        if i < up[0]:
            up[0] = i
        elif i > down[0]:
            down[0] = i
        if j < left[0]:
            left[0] = j
        elif j > right[0]:
            right[0] = j
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < m and 0 <= y < n and image[x][y] == "1":
                image[x][y] = "0"
                self.dfs(image, x, y, left, right, up, down, m, n)




image = [ "0010",
          "0110",
          "0100"]
x = 0
y = 2

a = Solution()
print(a.minArea(image, x, y))
