"""

https://leetcode.com/problems/mirror-reflection/solution/

858.Mirror-Reflection
容易想象，光路射出后，会在左右边界上来回反弹数次，可能会到达接收器1，也可能会到达接收器2，但更有可能会打到上边界从而弹回，造成后续非常复杂的光路。这是本题的难点所在。

解决方法是：当光线打到上边界1-2时，我们不考虑其弹回的路径，而是假设其直接穿越了上边界，进入了一个镜像世界1-3'0'-2。如下图：

3'----------0'
|           |
|  Virtual  |
1-----------2
|           |
|   Real    |
3-----------0
这样光路就可以继续在左右边界上来回反弹数次，如果有幸能被3'接收，就意味着在真实世界里光路能抵达3；同理，如果有幸能被0'接收，就意味着在真实世界里光路能抵达0；当然，同样也有可能会继续达到上边界3'-0'，那怎么办呢？那就沿着那条镜面再做一次镜像翻转，得到二次虚拟空间。如下图：

3'----------0'
|           |
|  Virtual2 |
1'----------2'
|           |
|  Virtual2 |
3'----------0'
|           |
|  Virtual  |
1-----------2
|           |
|  Real     |
3-----------0
可见二次虚拟空间进一步扩展了纵向的空间，使得光路可以继续来回折线向上走，一路上又有可能被1','2',3',0'接收，同理这意味着真实世界里的光路可以相应地被1,2,3,0接收...这样的虚拟空间可以进一步的扩展。

因为本题中每次光路的“折向”都会上升q，而每层接收器之间的距离是p，两者都是正整数，因此，光路必定会在来回盘升了LCM(p,q)之后，抵达（虚拟）接收器的位置。

那么如何确定抵达了哪一个接收器呢？我们可以找规律。从起点开始（真实世界的3），每上升q就会到达右边界，再上升q就会到达左边界，依次交替。同样，每上升p就会到达1-2水平层（或它们的镜像），再上升p就会到达3-0水平层（或它们的镜像），依次交替。所以我们令LCM(p,q)=mq=np，当m是奇数时就可能是2或者0，偶数时就可能是1或者3。当n是奇数，就可能是1或者2，偶数时就可能是3或者0.

当我们明确了m和n的奇偶性，就可以唯一确定光路射入的是哪一个（虚拟）接收器。

"""

import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        def lcm(x, y):
            return x * y // math.gcd(x, y)

        h = lcm(p, q)
        m = h // p
        n = h // q
        a = m % 2
        b = n % 2
        if a == 0 and b == 0:
            return 3
        elif a == 1 and b == 0:
            return 2
        elif a == 0 and b == 1:
            return 0
        else:
            return 1



class SolutionSimultation:
    def mirrorReflection(self, p, q):
        from fractions import Fraction as F

        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]

        while (x, y) not in targets:
            #Want smallest t so that some x + rx, y + ry is 0 or p
            #x + rxt = 0, then t = -x/rx etc.
            t = float('inf')
            for v in [F(-x,rx), F(-y,ry), F(p-x,rx), F(p-y,ry)]:
                if v > 0: t = min(t, v)

            x += rx * t
            y += ry * t

            #update rx, ry
            if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
                rx *= -1
            if y == p or y == 0:
                ry *= -1

        return 1 if x==y==p else 0 if x==p else 2

