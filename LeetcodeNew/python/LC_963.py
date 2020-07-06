"""
963.Minimum-Area-Rectangle-II
我们穷举任意的一对点（记作点i和点j），那么ij所组成的一条线段，可以用deltaX = xj-xi, deltaY = yj-ji来表示它的方向和长度。
我们将同属于{deltaX,deltaY}的point pair（或者说线段）放在一起，即

Map[{deltaX,deltaY}].push_back({i,j});
那么对于同一个key = {deltaX,deltaY}所代表的这些线段，两两之间都一定可以组成一个平行四边形！

我们遍历这些平行四边形。对于每一个平行四边形，它们的四个点的坐标都是已知的（比如记作ijkt）。
我们可以通过考察向量ij和向量jk是否垂直来判定这个四边形是否是矩形。数学上，具体的做法是考察两个二维向量的点积是否为零。即

v1(x1,y1)垂直于v2(x2,y2) <=> x1*x2+y1*y2 = 0
如果确认是矩形，那我们很容易计算它的面积，记录下来求最小值即可。

这种做法的效率较高，原因是我们将所有的线段（N^2)条按照“长度+方向”进行了分类。每一类里的线段数目其实比较少，
做两两组合（构建平行四边形）的开销不大。

"""

import collections
import math


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        n = len(points)
        table = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                deltaX = points[i][0] - points[j][0]
                deltaY = points[i][1] - points[j][1]
                table[(deltaX, deltaY)].append([i, j])

        res = float('inf')
        for delta, pairs in table.items():
            for m in range(len(pairs)):
                for n in range(m + 1, len(pairs)):
                    i = pairs[m][0]
                    j = pairs[m][1]
                    k = pairs[n][0]

                    dx1 = points[i][0] - points[j][0]
                    dy1 = points[i][1] - points[j][1]
                    dx2 = points[i][0] - points[k][0]
                    dy2 = points[i][1] - points[k][1]

                    if dx1 * dx2 + dy1 * dy2 != 0:
                        continue

                    side1 = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]) + (points[i][1] - points[j][1]) * (points[i][1] - points[j][1])
                    side2 = (points[i][0] - points[k][0]) * (points[i][0] - points[k][0]) + (points[i][1] - points[k][1]) * (points[i][1] - points[k][1])

                    area = math.sqrt(side1) * math.sqrt(side2)
                    res = min(res, area)
        return res if res != float('inf') else 0








