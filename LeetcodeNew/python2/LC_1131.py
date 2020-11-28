

"""
1131.Maximum-of-Absolute-Value-Expression
本题的本质就是求一堆三维空间内的点，找出曼哈顿距离最大的一个。其中每个点的坐标就是(arr1[i],arr2[i],i). 这个问题如何求解呢？我们先来解决更简单点的问题，
也就是在一堆二维空间中的点如何找到曼哈顿距离最远的两个。

在二维平面中，设曼哈顿距离最远的两点坐标为 (a1,b1) (a2,b2)， 则其曼哈顿距离为： |a1−a2|+|b1−b2|

去掉绝对值便有四种形式：

(a1−a2)+(b1−b2)，
(a1−a2)+(b2−b1)，
(a2−a1)+(b1−b2)，
(a2−a1)+(b2−b1)，
我们需要注意到，|a1−a2|+|b1−b2|其实就是这四个式子中的最大值，即

max {
(a1−a2)+(b1−b2)，
(a1−a2)+(b2−b1)，
(a2−a1)+(b1−b2)，
(a2−a1)+(b2−b1) }
变化一下就成了

max {
(a1+b1)−(a2+b2)，
(a1−b1)−(a2−b2)，
(−a1+b1)−(−a2+b2)，
(−a1−b1)−(−a2−b2) }
那么对于任意的i，j，我们有

max |ai−aj|+|bi−bj|= max over (i,j){
  max {
      (ai+bi)−(aj+bj)，
      (ai−bi)−(aj−bj)，
      (−ai+bi)−(−aj+bj)，
      (−ai−bi)−(−aj−bj) }
}
调换两个max的顺序，即是

 max{
    max over (i,j)  {(ai+bi)−(aj+bj)},
    max over (i,j)  {(ai−bi)−(aj−bj)},
    max over (i,j)  {(−ai+bi)−(−aj+bj)},
    max over (i,j)  {(−ai−bi)−(−aj−bj)},
 }
显然，其中第一项

max over (i,j)  {(ai+bi)−(aj+bj)}
=   max {ak+bk} for any k
  - min {ak+bk} for any k
于是，整个算法就是：k个维度的坐标(x1,...,xk)，就有2^k种状态。对于每一种状态(s1,..,sk)，（其中每种状态的分量都是+1或者-1）我们遍历所有元素i，
计算 sum(xi*si)里面的最大值mx和最小值mn，得到maxDiff = mx-mn。最终答案就是在所有状态对应的maxDiff中再取最大值。
"""

"""
3维找曼哈顿距离

(arr1[i], arr2[j], arr3[i])

(x1, y1) (x2, y2)

d = |x1-y1| + |x2-y2|
  = max{
        x1-y1+x2-y2,
        -x1+y1+x2-y2,
        x1-y1-x2+y2,
        -x1+y1-x2+y2,        
  }

  = max{
        (x1-y1)-(-x2+y2),
        (-x1+y1)-(-x2+y2),
        (x1-y1)-(x2-y2),
        (-x1+y1)-(x2-y2),        
  }


  = max{
        x1-x2+y1-y2,
        -x1+x2+y1-y2,
        x1-x2-y1+y2,
        -x1+x2-y1+y2,        
  }

  = max{
        (x1-y1)-(-x2+y2),
        (-x1+y1)-(-x2+y2),
        (x1-y1)-(x2-y2),
        (-x1+y1)-(x2-y2),        
  }



"""

"""
解题思路：对于表达式 |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|，在i < j的情况下，这个表达式的值是下面其中四个之一：

 （arr1[i] + arr2[i] - i）   -   （arr1[j] + arr2[j] - j）

  (arr1[i] - arr2[i] - i)   -    (arr1[j] - arr2[j] - j)

  (arr2[i] - arr1[i] - i)   -    (arr2[j] - arr1[j] - j)

  (arr2[i] + arr1[i] + i)   -    (arr2[j] + arr1[j] + j)

 所以只要遍历一次数组，求出四个表达式中差值的最大值和最小值即可。
"""


class SolutionTony:
    def maxAbsValExpr(self, arr1, arr2):
        maxi = [float('-inf')] * 4
        mini = [float('inf')] * 4

        for i in range(len(arr1)):
            maxi[0] = max(maxi[0], arr1[i] + arr2[i] - i)
            mini[0] = min(mini[0], arr1[i] + arr2[i] - i)

            maxi[1] = max(maxi[1], arr1[i] - arr2[i] - i)
            mini[1] = min(mini[1], arr1[i] - arr2[i] - i)

            maxi[2] = max(maxi[2], arr2[i] - arr1[i] - i)
            mini[2] = min(mini[2], arr2[i] - arr1[i] - i)

            maxi[3] = max(maxi[3], arr2[i] + arr1[i] + i)
            mini[3] = min(mini[3], arr2[i] + arr1[i] + i)

        return max(maxi[0] - mini[0], maxi[1] - mini[1], maxi[2] - mini[2], maxi[3] - mini[3])




class Solution:
    def maxAbsValExpr(self, arr1, arr2) -> int:
        n = len(arr1)
        a = [[0 for i in range(3)] for j in range(n)]

        for i in range(n):
            a[i][0] = arr1[i]
            a[i][1] = arr2[i]
            a[i][2] = i
        res = 0
        for s in range(1 << 3):  # s = 000, 001, 010, 011
            mini = float('inf')
            maxi = float('-inf')

            for i in range(n):
                summ = 0
                for j in range(3):
                    # 从000转成+-号
                    if ((s >> j) & 1) == 1:
                        summ += a[i][j]
                    else:
                        summ += -a[i][j]
                mini = min(mini, summ)
                maxi = max(maxi, summ)
            res = max(res, maxi - mini)
        return res






