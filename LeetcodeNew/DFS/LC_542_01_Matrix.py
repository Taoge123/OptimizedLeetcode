
#BFS
#Basically we add 0 into queue, then do BFS for all neiboghs, to make neighbor add 1
class Solution1:
    def updateMatrix(self, matrix):
        queue, m, n = [], len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 0x7fffffff
                else:
                    queue.append((i, j))

        for i, j in queue:
            for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
                z = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                    matrix[r][c] = z
                    queue.append((r, c))
        return matrix


"""
We simply do 2 iterations from first to last and last to first element.
For the 1st for loop, we update distance of element with minimum of previous top and left elements + 1 (itself).
For the 2nd for loop, we update distance of element with minimum of previous bottom and right elements + 1 (itself).
As a result, we get minimum distance value for each element updated with distances of neighbours + 1.
这道题给了我们一个只有0和1的矩阵，让我们求每一个1到离其最近的0的距离，
其实也就是求一个距离场，而求距离场那么BFS将是不二之选。刚看到此题时，
我以为这跟之前那道 Shortest Distance from All Buildings 是一样的，从每一个0开始遍历，
不停的更新每一个1的距离，但是这样写下来TLE了。后来我又改变思路，从每一个1开始BFS，找到最近的0，
结果还是TLE，气死人。后来逛论坛发现思路是对的，就是写法上可以进一步优化，我们可以首先遍历一次矩阵，
将值为0的点都存入queue，将值为1的点改为INT_MAX。之前像什么遍历迷宫啊，起点只有一个，
而这道题所有为0的点都是起点，这想法，叼！然后开始BFS遍历，从queue中取出一个数字，
遍历其周围四个点，如果越界或者周围点的值小于等于当前值加1，则直接跳过。因为周围点的距离更小的话，
就没有更新的必要，否则将周围点的值更新为当前值加1，然后把周围点的坐标加入queue


-----------------------------------------------------------------------------
下面这种解法是参考的qswawrq大神的帖子，他想出了一种二次扫描的解法，从而不用使用BFS了。
这种解法也相当的巧妙，我们首先建立一个和matrix大小相等的矩阵res，初始化为很大的值，
这里我们用INT_MAX-1，为甚么要减1呢，后面再说。然后我们遍历matrix矩阵，当遇到为0的位置，
我们将结果res矩阵的对应位置也设为0，这make sense吧，就不多说了。然后就是这个解法的精髓了，
如果不是0的地方，我们在第一次扫描的时候，比较其左边和上边的位置，取其中较小的值，再加上1，
来更新结果res中的对应位置。这里就明白了为啥我们要初始化为INT_MAX-1了吧，因为这里要加1，
如果初始化为INT_MAX就会整型溢出，不过放心，由于是取较小值，res[i][j]永远不会取到INT_MAX，
所以不会有再加1溢出的风险。第一次遍历我们比较了左和上的方向，那么我们第二次遍历就要比较右和下的方向，
注意两种情况下我们不需要比较，一种是当值为0时，还有一种是当值为1时，
这两种情况下值都不可能再变小了，所以没有更新的必要
"""


#DP solution
class Solution2:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix


"""
队列（Queue）

初始令step = 0，将matrix中所有1元素加入队列queue

循环，直到queue为空：

  令step = step + 1

  遍历queue中的元素，记当前元素为p，坐标为(x, y)：

    若p的相邻元素中包含0元素，则p的距离设为step，从queue中移除p
    
  将上一步中移除的元素对应的matrix值设为0
"""

#Queue solution
class Solution3:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        h, w = len(matrix), len(matrix[0])
        ans = [[0] * w for x in range(h)]
        #If matrix[x][y] exist, then we add it to queue
        queue = [(x, y) for x in range(h) for y in range(w) if matrix[x][y]]
        step = 0
        while queue:
            step += 1
            nqueue, mqueue = [], []
            for x, y in queue:
                zero = 0
                #For each direction
                # for dx, dy in zip((1, 0, -1, 0), (0, 1, 0, -1)):
                for dx, dy in [[1, 0],[0, 1],[-1, 0],[0, -1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 0:
                        zero += 1
                if zero:
                    ans[x][y] = step
                    mqueue.append((x, y))
                else:
                    nqueue.append((x, y))
            for x, y in mqueue:
                matrix[x][y] = 0
            queue = nqueue
        return ans





