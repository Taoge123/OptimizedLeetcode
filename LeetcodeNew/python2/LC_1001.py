'''
解题思路
每个点对于横向(x)、纵向(y)、斜向(x - y)和反斜向(x + y)，都有各自对应的位置变量，一共4个
以这四种位置变量为基础，建立4个hash table。hash table的key是位置变量，value是对应位置变量上的亮灯个数
每个点是否被照亮取决于这个点对应的四个位置变量在对应的hash table中是否存在（当value == 0时，我们会直接erase这对key-value）

亮灯阶段:
更新四个hash table，同时用一个hash table (命名为lamps_status) 记录灯的坐标和状态

query阶段:

对于每一个query，先以该query点的4个位置变量check这个点是不是会被照亮
遍历该点的邻居和它自身。如果有灯并且灯亮着，需要update相应的4个hash map的信息以及lamps_status的信息
'''


import collections

class Solution:
    def __init__(self):
        self.dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

    def gridIllumination(self, N: int, lamps, queries):
        lights = {(x, y) for x, y in lamps}
        horizontal = collections.Counter(x for x, y in lamps)
        vertical = collections.Counter(y for x, y in lamps)
        diag = collections.Counter(x - y for x, y in lamps)
        anti_diag = collections.Counter(x + y for x, y in lamps)

        res = []
        for x, y in queries:
            if horizontal[x] > 0 or vertical[y] > 0 or diag[x - y] > 0 or anti_diag[x + y] > 0:
                res.append(1)
            else:
                res.append(0)

            # check 9 adjacent cells
            for dx, dy in self.dirs:
                i = x + dx
                j = y + dy

                if (i, j) in lights:
                    lights.remove((i, j))
                    horizontal[i] -= 1
                    vertical[j] -= 1
                    diag[i - j] -= 1
                    anti_diag[i + j] -= 1
        return res



N = 5
lamps = [[0,0],[4,4]]
queries = [[1,1],[1,0]]

a = Solution()
print(a.gridIllumination(N, lamps, queries))


