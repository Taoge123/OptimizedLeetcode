
"""
http://www.cnblogs.com/grandyang/p/5268775.html

An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel.
The black pixels are connected, i.e., there is only one black region.
Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels,
return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

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
这道题给我们一个二维矩阵，表示一个图片的数据，其中1代表黑像素，0代表白像素，
现在让我们找出一个最小的矩阵可以包括所有的黑像素，还给了我们一个黑像素的坐标，我们先来看Brute Force的方法，
这种方法的效率不高，遍历了整个数组，如果遇到了1，就更新矩形的返回
"""
"""
思路：

1、DFS：首先想到的就是深度优先搜索。从位置 (x, y) 开始深度搜索它的四个邻居，在搜索的过程中维护四个边界，
最后返回四个边界所对应的面积即可。该算法的时间复杂度是O(m*n)，其中m和n分别是图像的高度和宽度。
DFS应该是一个可以通过面试的算法了,当然这道题目用BFS我觉得也是可以解决的。

2、二分查找：还有一个更加巧妙、时间复杂度更低的算法。
1）采用二分法在[0, y]区间内搜索每一行，找出最先出现‘1’的那一列，这样就确定了左边界left；
2）采用二分法在[y + 1, col_num)区间内搜索每一行，找出最后出现‘0’的那一列，这样就确定了右边界right；
3）采用二分法在[left, right]区间内找出最先出现‘1’的那一行，这样就确定了上边界up；
4）采用二分法在[left, right]区间内找出最后出现‘0’的那一行，这样就确定了下边界down。四个边界都确定之后，
   就可以计算并返回包围盒的面积了。假设图像的高度和宽度分别是m和n，则算法的时间复杂度是O(mlogn + nlogm)。
   在实现中为了减少代码行数，将不同搜索函数整合在一起了，不过总体思路就是这么简单。

"""

"""
M is number of rows and N is number of cols of the image.
W is the width of the black region, which is at most N.
H is the height of the black region, which is at most M.
O(MlogW + WlogH) is at most O(MlogN + NlogM).
"""


class Solution1:
    def minArea(self, image, x, y):

        if not image or not image[0]: return 0

        self.image = image
        n_r, n_c = len(image), len(image[0])
        left = self.search(0, y, 0, n_r, True, True)
        right = self.search(y + 1, n_c, 0, n_r, False, True)
        top = self.search(0, x, left, right, True, False)
        bottom = self.search(x + 1, n_r, left, right, False, False)
        return (right - left) * (bottom - top)

    def search(self, lo, hi, start, end, isFindLow=True, isSearchCol=True):

        while lo < hi:
            k = start
            mid = lo + (hi - lo) // 2

            if isSearchCol:
                while k < end and self.image[k][mid] == '0':
                    k += 1
            else:
                while k < end and self.image[mid][k] == '0':
                    k += 1

            if (k < end) == isFindLow:
                hi = mid
            else:
                lo = mid + 1
        return lo


class Solution2:
    def minArea(self, image, x, y):
        l, r, u, d, m, n = [y], [y], [x], [x], len(image), len(image[0])
        def dfs(i, j):
            if i < u[0]: u[0] = i
            elif i > d[0]: d[0] = i
            if j < l[0]: l[0] = j
            elif j > r[0]: r[0] = j
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == "1":
                    image[x][y] = "0"
                    dfs(x, y)
        dfs(x, y)
        return (r[0] - l[0] + 1) * (d[0] - u[0] + 1)


# python in dfs
class Solution3:
    def minArea(self, image, x, y):
        if image is None or len(image) == 0:
            return 0

        left, right = y, y
        up, down = x, x

        self.dfs(image, x, y, left, right, up, down)

        return (right - left + 1) * (down - up + 1)


    def dfs(self , image, x, y, left, right, up, down):
        if x< 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != '1':
            return

        left = min(left, y)
        right = max(y, right)
        up = min(up, x)
        down = max (down, x)

        image[x] = image[x][:y] + 'm' + image[x][y+1:]

        self.dfs(image, x + 1, y, left, right, up, down) # down
        self.dfs(image, x - 1, y, left, right, up, down) # up
        self.dfs(image, x, y + 1, left, right, up, down) # right
        self.dfs(image, x, y - 1, left, right, up, down) # left


class Solution4:
    def minArea(self, image, r, c):
        m, n, queue = len(image), len(image[0]), [(r, c)]
        visited, minr, minc, maxr, maxc = {(r, c)}, m + 1, n + 1, -1, -1
        for r, c in queue:
            minr, minc, maxr, maxc = min(minr, r), min(minc, c), max(maxr, r), max(maxc, c)
            for d in {(-1, 0), (1, 0), (0, 1), (0, -1)}:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] != "0" and (nr, nc) not in visited:
                    visited |= {(nr, nc)}
                    queue += (nr, nc),
        return (maxr - minr + 1) * (maxc - minc + 1)




