"""
很明显，我们将二维平面划均分为四个区域，然后给自递归处理，计算每个区域的countShips，然后累积起来。

需要注意的几点：（1）划分区域的时候需要保证四块的边界不能重复。（2）提前用hasShip来预判是否有船在区域内，如果没有，可以直接返回零。
（3）边界条件是：当左上角与右下角重合时，返回的结果与hasShip的结果一致。(4)在调用hasShip之前，需要保证右上角和左下角的相对位置关系是正确的：
比如当右上角是[0,1]且左下角是[0,0]时，其实并不能分出四个区域，其实两个区域是“假的“，并不能调用 hasShip.
"""


class Sea:
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       return True

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', P: 'Point', Q: 'Point') -> int:
        res = 0
        if P.x >= Q.x and P.y >= Q.y and sea.hasShips(P, Q):
            if P.x == Q.x and P.y == Q.y:
                return 1
            mx, my = (P.x + Q.x) // 2, (P.y + Q.y) // 2
            res += self.countShips(sea, P, Point(mx + 1, my + 1))
            res += self.countShips(sea, Point(mx, P.y), Point(Q.x, my + 1))
            res += self.countShips(sea, Point(mx, my), Q)
            res += self.countShips(sea, Point(P.x, my), Point(mx + 1, Q.y))
        return res



