"""
https://leetcode.cn/problems/self-crossing/solution/acmjin-pai-ti-jie-zhao-gui-lu-bian-cheng-ujds/

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.



Example 1:

┌───┐
│   │
└───┼──>
    │

Input: [2,1,1,2]
Output: true
Example 2:

┌──────┐
│      │
│
│
└────────────>

Input: [1,2,3,4]
Output: false
Example 3:

┌───┐
│   │
└───┼>

Input: [1,1,1,1]
Output: true

335.Self-Crossing
通过画图分析可以得知，要想不相交，就只有三种模式：

不断地螺旋形膨胀，时刻满足 x[i]>x[i-2]

不断地螺旋形收缩，时刻满足 x[i]<x[i-2]

先螺旋膨胀，再螺旋收缩。假设其中的转折点是x[i]，即第i步是第一次出现x[i]<x[i-2]的线段。根据之前的分析，从i+1开始，就进入了螺旋收缩模式，需要时刻满足 x[i]<x[i-2]。
但通过作图可以发现，x[i]的长短，还会略微影响x[i+1]的取值：

(a) 如果x[i]<x[i-2]-x[i-4]的话，接下来的x[i+1]只需要简单地满足小于x[i-1]即可（也就是它之前的对边），之后也是只要服从螺旋收缩的基本规则就行。

(b) 但是如果x[i]>=x[i-2]-x[i-4]的话，为了避免相交，x[i+1]不能超过x[i-1]-x[i-3]。这个等价于我们将x[i-1]-=x[i-3]，之后从x[i+1]开始，只要仍服从螺旋收缩的基本规则即可。

特别注意，为了保证x[i-4]之类的操作不会下标越界，一个巧妙的方法是在x序列的前面添加四个零，模拟一圈螺旋膨胀的路径，然后从i=4开始考察它接下来的模式。



-------- x_2
|      |
|   |  |
|   ----
|      x_4  
_____x

if x > (x_2 - x_4):
    then x + 1 must 


--------------|
|             |
| -|    |     |
|  |    |     |
|  |     ------
|  |
|  | @
----
  ?

 x+1 < x_-1就可以

"""

class SolutionRika:
    def isSelfCrossing(self, distance) -> bool:
        # 画图-->  三种情况：第1条和第4条相交，第1条和第5条相交，第1条和第6条相交

        for i in range(3, len(distance)):
            # case1： 第四条线与第一条线相交  (所有相隔三个的情况都通用)
            if distance[i - 1] <= distance[i - 3] and distance[i] >= distance[i - 2]:
                return True
                # case2： 第五条线与第(一)?条线相交 （所有相隔四个的情况都通用）
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True
                # case3： 第六条线与第一条线相交 （所有相隔五个的情况都通用）
            if i >= 5 and distance[i - 1] + distance[i - 5] >= distance[i - 3] and distance[i - 1] <= distance[i - 3] and distance[i - 2] > distance[i - 4] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True
        return False



class SolutionWisdom:
    def isSelfCrossing(self, x) -> bool:
        x = [0, 0, 0, 0] + x
        i = 4
        # 检查螺旋状
        while i < len(x) and x[i] > x[i - 2]:
            i += 1
        # 走到最后就没有crossing
        if i == len(x):
            return False
        # case 1
        if x[i] >= x[i - 2] - x[i - 4]:
            # 从此x[i-1]缩减
            x[i - 1] = x[i - 1] - x[i - 3]
        i += 1
        # 改完以后再来一次
        while i < len(x) and x[i] < x[i - 2]:
            i += 1
        if i == len(x):
            return False
        return True



class Solution:
    def isSelfCrossing(self, x):
        if len(x) < 4:
            return False
        for i in range(3, len(x)):
            if x[i] >= x[i - 2] and x[i - 1] <= x[i - 3]:
                return True
            if i >= 4 and x[i - 1] == x[i - 3] and x[i] + x[i - 4] >= x[i - 2]:
                return True
            if i >= 5 and x[i - 1] <= x[i - 3] and x[i - 3] <= x[i - 1] + x[i - 5] and x[i] + x[i - 4] >= x[i - 2] and x[i - 4] <= x[i - 2]:
                return True
        return False




