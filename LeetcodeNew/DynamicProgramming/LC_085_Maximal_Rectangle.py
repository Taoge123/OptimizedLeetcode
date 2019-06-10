
"""
Based on these two resources:
https://www.youtube.com/watch?v=g8bSdXCG-lA
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/153055/Really-short-python-solution-using-stack

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

"""
The DP solution proceeds row by row, starting from the first row. 
Let the maximal rectangle area at row i and column j be computed by [right(i,j) - left(i,j)]*height(i,j).

All the 3 variables left, right, and height can be determined by the information from previous row, 
and also information from the current row. So it can be regarded as a DP solution. The transition equations are:

left(i,j) = max(left(i-1,j), cur_left), cur_left can be determined from the current row

right(i,j) = min(right(i-1,j), cur_right), cur_right can be determined from the current row

height(i,j) = height(i-1,j) + 1, if matrix[i][j]=='1';

height(i,j) = 0, if matrix[i][j]=='0'

The code is as below. The loops can be combined for speed but I separate them for more clarity of the algorithm.

If you think this algorithm is not easy to understand, you can try this example:

0 0 0 1 0 0 0 
0 0 1 1 1 0 0 
0 1 1 1 1 1 0
The vector "left" and "right" from row 0 to row 2 are as follows

row 0:

l: 0 0 0 3 0 0 0
r: 7 7 7 4 7 7 7
row 1:

l: 0 0 2 3 2 0 0
r: 7 7 5 4 5 7 7 
row 2:

l: 0 1 2 3 2 1 0
r: 7 6 5 4 5 6 7
The vector "left" is computing the left boundary. Take (i,j)=(1,3) for example. On current row 1, the left boundary is at j=2. However, because matrix[1][3] is 1, you need to consider the left boundary on previous row as well, which is 3. So the real left boundary at (1,3) is 3.

I hope this additional explanation makes things clearer.

/* we start from the first row, and move downward;
 * height[i] record the current number of countinous '1' in column i;
 * left[i] record the left most index j which satisfies that for any index k from j to  i, height[k] >= height[i];
 * right[i] record the right most index j which satifies that for any index k from i to  j, height[k] >= height[i];
 * by understanding the definition, we can easily figure out we need to update maxArea with value (height[i] * (right[i] - left[i] + 1));
 * 
 * Then the question is how to update the array of height, left, and right
 * =================================
 * for updating height, it is easy
 * for (int j = 0; j < n; j++) {
 *    if (matrix[i][j] == '1') height[j]++;
 *    else height[j] = 0;
 * }
 * =============================================================================
 * It is a little bit tricky for initializing and updating left and right array
 * for initialization: 
 * we know initially, height array contains all 0, so according to the definition of left and right array, left array should contains all 0, and right array should contain all n - 1
 * for updating left and right, it is kind of tricky to understand...
 *     ==============================================================
 *     Here is the code for updating left array, we scan from left to right
 *     int lB = 0;  //lB is indicating the left boundry for the current row of the matrix (for cells with char "1"), not the height array...
 *     for (int j = 0; j < n; j++) {
 *          if (matrix[i][j] == '1') {
 *              left[j] = Math.max(left[j], lB); // this means the current boundry should satisfy two conditions: within the boundry of the previous height array, and within the boundry of the current row...
 *          } else {
 *              left[j] = 0; // when matrix[i][j] = 0, height[j] will get update to 0, so left[j] becomes 0, since all height in between 0 - j satisfies the condition of height[k] >= height[j];
 *              lB = j + 1; //and since current position is '0', so the left most boundry for next "1" cell is at least j + 1;
 *          }
 *     }
 *     ==============================================================
 *     the idea for updating the right boundary is similar, we just need to iterate from right to left
 *     int rB = n - 1;
 *     for (int j = n - 1; j >= 0; j--) {
 *         if (matrix[i][j] == '1') {
 *              right[j] = Math.min(right[j], rB);
 *         } else {
 *              right[j] = n - 1;
 *              rB = j - 1;
 *      }
 */


a matrix example:

[
   ["1","0","1","0","0"],
   ["1","0","1","1","1"],
   ["1","1","1","1","1"],
   ["1","0","0","1","0"]
 ]
策略: 把matrix看成多个直方图, 每一行及其上方的数据都构成一个直方图, 需要考察matrix.size()个直方图
对于每个点(row, col), 我们最后都计算以这个点上方的连续的'1'往left, right方向延申可以得到的最大的矩形的面积
通过这种方法获取的矩形一定会把最大的矩形包含在内
height[row][col]记录的是(row, col)这个坐标为底座的直方图柱子的高度, 如果这个点是'0', 那么高度当然是0了
left[row][col]记录的是(row, col)这个坐标点对应的height可以延申到的最左边的位置
right[row][col]记录的是(row, col)这个坐标点对应的height可以延申到的最右边的位置+1
以上面的matrix为例,
对于(row=2, col=1)这个点, left=0, right=5, height=1
对于(row=2, col=2)这个点, left=2, right=3, height=3
(2,2)这个点与(2,1)紧挨着,left和right却已经变化如此之大了, 这是因为left和right除了受左右两边的'1'影响, 还受到了其上方连续的'1'的制约
由于点(2,2)上有height=3个'1', 这几个'1'的left的最大值作为当前点的left, 这几个'1'的right的最小值作为当前点的right
因此, 实际上, 我们是要找以hight对应的这条线段往左右两边移动(只能往全是'1'的地方移动), 可以扫过的最大面积
当hight与目标最大矩形区域的最短的height重合时, 最大矩形的面积就找到了, 如上面的例子, 就是点(2,3)或(2,4)对应的height


Last Edit: September 28, 2018 4:33 PM

Read More
这道题太难了，先搞清楚这些matrix分别代表什么。
height means from top to this position, there are how many '1'
left means at current position, what is the index of left bound of the rectangle with height[j]. 0 means at this position, no rectangle. (现在这个矩形的左边的下标)
right means the right bound index of this rectangle. 'n' means no rectangle.

matrix
0 0 0 1 0 0 0
0 0 1 1 1 0 0
0 1 1 1 1 1 0

height
0 0 0 1 0 0 0
0 0 1 2 1 0 0
0 1 2 3 2 1 0

left
0 0 0 3 0 0 0
0 0 2 3 2 0 0
0 1 2 3 2 1 0

right
7 7 7 4 7 7 7
7 7 5 4 5 7 7
7 6 5 4 5 4 7

result
0 0 0 1 0 0 0
0 0 3 2 3 0 0
0 5 6 3 6 5 0
dp的太难了，来看下Histogram的解法吧。参考这道题：https://discuss.leetcode.com/topic/7599/o-n-stack-based-java-solution/23

比如这个matrix有n行，就把这个问题转换成n个Histogram的问题。
每个问题就是一个以这一行为底的Histogram问题，上面连续的1的个数就是Height。



matrix
0 1 1 1 1 1 0
0 0 1 1 1 0 0
0 0 0 1 0 0 0

height
0 1 1 1 1 1 0
0 0 2 2 2 0 0
0 0 0 3 0 0 0

left
0 1 1 1 1 1 0
0 0 2 2 2 0 0
0 0 0 3 0 0 0

right
7 6 6 6 6 6 7
7 7 5 5 5 7 7
7 7 7 4 7 7 7

result
0 5 5 5 5 5 0
0 0 6 6 6 0 0
0 0 0 3 0 0 0

matrix
1 1 1 0 0 0 0 0
1 1 1 1 1 1 1 1
0 0 0 0 1 1 1 1
0 0 0 0 1 1 1 1

height
1 1 1 0 0 0 0 0
2 2 2 1 1 1 1 1
0 0 0 0 2 2 2 2
0 0 0 0 3 3 3 3

left
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 4 4 4 4
0 0 0 0 4 4 4 4

right
3 3 3 8 8 8 8 8
3 3 3 8 8 8 8 8
8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8

result
3 3 3 0 0 0 0 0
6 6 6 8 8 8 8 8
0 0 0 0 8 8 8 8
0 0 0 0 12 12 12 12

matrix
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0
0 1 1 1 0
0 1 1 1 0

height
0 0 1 0 0
0 0 2 0 0
0 0 3 0 0
0 1 4 1 0
0 2 5 2 0

left
0 0 2 0 0
0 0 2 0 0
0 0 2 0 0
0 1 2 1 0
0 1 2 1 0

right
5 5 3 5 5
5 5 3 5 5
5 5 3 5 5
5 4 3 4 5
5 4 3 4 5

results
0 0 1 0 0
0 0 2 0 0
0 0 3 0 0
0 3 4 3 0
0 6 5 6 0
"""

class Solution1:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans


class Solution2:
    def maximalRectangle(self, matrix):

        if not matrix or len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        ans = 0

        left, right, height = [0] * n, [n] * n, [0] * n
        for i in range(m):
            curl = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(curl, left[j])
                else:
                    left[j] = 0
                    curl = j + 1
            curr = n
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(curr, right[j])
                else:
                    right[j] = n
                    curr = j
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
                ans = max(height[j] * (right[j] - left[j]), ans)
        return ans


class Solution3:

    def largestRectangleArea(self, heights):

        heights.append(0)
        stack = [-1]
        area = 0
        for i in range(len(heights)):
            while heights[stack[-1]]>heights[i]:
                height = heights[stack.pop()]
                area = max(area, height*(i-stack[-1]-1))
            stack.append(i)
        return area

    def maximalRectangle(self, matrix):

        if matrix == []:
            return 0
        area = 0
        prev = matrix[0]
        prev = [int(i) for i in prev]
        area = max(area, self.largestRectangleArea(prev))
        for row in matrix[1:]:
            for i in range(len(row)):
                row[i] = int(row[i])
                if int(row[i])!=0:
                    row[i] += int(prev[i])
            area = max(area, self.largestRectangleArea(row))
            prev = row
        return area


class Solution4:

    def calc_histogram_area(self, nums):
        stack = []
        max_area = 0
        nums.append(0)

        for curr_idx, curr_height in enumerate(nums):

            left_idx = curr_idx

            while stack and stack[-1][0] >= curr_height:
                last_height, left_idx = stack.pop()
                max_area = max(
                    max_area,
                    curr_height * (curr_idx + 1 - left_idx),
                    last_height * (curr_idx - left_idx)
                )

            stack.append((curr_height, left_idx))

        return max_area

    def maximalRectangle(self, matrix):

        if len(matrix) == 0:
            return 0

        max_area = 0
        histogram = [0] * len(matrix[0])

        for row in matrix:
            histogram = [histogram[idx] + 1 if val == '1' else 0 for idx, val in enumerate(row)]
            max_area = max(max_area, self.calc_histogram_area(histogram))

        return max_area


class Solution5:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        for j in range(n):
            for i in range(m):
                matrix[i][j]=int(matrix[i][j])
        col_mat=matrix
        for i in range(1,m):
            for j in range(n):
                if col_mat[i][j]==0:
                    continue
                col_mat[i][j]=col_mat[i-1][j]+col_mat[i][j]
        res=0
        for k in range(m):
            max_row=max(col_mat[k])
            res=max(max_row,res)
            for i in range(n):
                for j in range(i+1,n+1):
                    res=max(res,min(col_mat[k][i:j])*(j-i))
        return res



    