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

class Solution:
    def minArea(self, image, x, y):
        m, n = len(image), len(image[0])
        top = self.searchRows(image, 0, x, True)
        bottom = self.searchRows(image, x + 1, m, False)
        left = self.searchColumns(image, 0, y, top, bottom, True)
        right = self.searchColumns(image, y + 1, n, top, bottom, False)
        return (right - left) * (bottom - top)

    def searchRows(self, image, left, right, opt):
        while left != right:
            mid = (left + right) // 2
            if ('1' in image[mid]) == opt:
                right = mid
            else:
                left = mid + 1
        return left

    def searchColumns(self, image, left, right, top, bottom, opt):
        while left != right:
            mid = (left+ right) // 2
            if any(image[k][mid] == '1' for k in range(top, bottom)) == opt:
                right = mid
            else:
                left = mid + 1
        return left



image = [ "0010",
          "0110",
          "0100"]
x = 0
y = 2

a = Solution()
print(a.minArea(image, x, y))
