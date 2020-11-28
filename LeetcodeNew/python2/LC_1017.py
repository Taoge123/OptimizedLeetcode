"""
https://www.youtube.com/watch?v=ia_vwGMAFVY
https://www.youtube.com/watch?v=0MBC7y_j80A
https://www.youtube.com/watch?v=uo0jozNyNlg


"""
"""
Please follow more detailed explanation in my channel on Youtube.

Intuition:
Maybe write a base2 function first?
How about add minus -?
Done.

Explanation:
base2 function is quite basis of basis.

check last digit by N%2 or N&1.
If it's 1, you get 1.
If it's 0, you get 0.

shift to right N >> 1.
This actually do two things:
2.1 Minus 1 if last digit is 1.
2.2 Divide N by 2.

base -2 is no difference,
except that we need divide N by -2.

So we do the same thing,
just add a sign - after division.

Sorry that the explanation seems not enough.
But if you really understand how we do the base2,
you will find just literally the same process.


Time Complexity:
O(logN) Time, O(logN) space.
Note that I didn't deal with string concatenation,
and just take this part as O(1).

Instead of create a new string each time,
we can improve this process using some operations join/reverse or data structure list/vector .
Like Java we may need StringBuilder,
but those are not what I want to discuss deeply here.
"""

"""
xyz(10) = abcde(2)

N = x*10^2 + y*10^1 + z*10^0
  = a*2^4 + b*2^3 + c*2^2 + d*2^1 + e*2^0

    r0 = N%10
    N = N//10 => (N-r0)//10
    r1 = N%10
    N = (N-r1)//10

    r0 = N%2
    N = N//2 => (N-r0)//2
    r1 = N%2
    N = (N-r1)//2

    ...

    r0 = N%-2
    N = N//-2 => (N-r0)//-2
    r1 = N%-2
    N = (N-r1)//-2

5/3    => 1=1 r=2
-5/-3  => 1=1 r=-2
5/-3   => 1=1 r=-2
5/-3   => 1=2 r=1
1017.Convert-to-Base--2
本质上和求N的任何K进制的转化一样的做法。求得余数r=N%K作为当前最低位的数字，然后将N=(N-r)/K作为下一个循环的初始值直至为零。把所有的数字拼接起来倒序输出就是K进制的结果。

特别注意，余数r必须是正数，也就是说无法除尽的时候，采用的是向下取整。比如说5/(-3)，依据严格的数学定义，商是-2，余数是1.

但是，当除数是负数的时候，不同语言的运算规则会不一样。在C++/Java里面，整数的除法都是向零取整。比如说5/(-3)，结果商是-1，余数是-2.这个余数因为是负数，是无法用来作为进制转换结果的。解决方案是：将商加上一，余数加上abs(K)。这样就转变成了向下取整的结果，余数也变成了正数。在这个例子中，结果商就是-1，余数是1.

事实上，在wiki里面已经明确写明了negative base calculation的方法：https://en.wikipedia.org/wiki/Negative_base#Calculation

"""


class SolutionWisdom:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        res = []
        while (N != 0):
            remain = N % -2
            div = (N - remain) // -2

            if remain < 0:
                div += 1
                remain += 2

            res.append(str(remain))
            N = div

        return "".join(res[::-1])







def convertToBaseK(n, K):
    res = ""
    while n != 0:
        temp = n % K
        n //= K
        res = str(temp) + res
    return res


def convertToBaseTwo(N):
    res = []
    while N != 0:
        res.append(N & 1)
        N = N >> 1

    return "".join(map(str, res[::-1])) if len(res) > 0 else "0"

class Solution:
    def base2(self, N):
        if N == 0 or N == 1:
            return str(N)
        return self.base2(N >> 1) + str(N & 1)


    def baseNeg2(self, N):
        if N == 0 or N == 1:
            return str(N)
        return self.baseNeg2(-(N >> 1)) + str(N & 1)

    def base22(self, x):
        res = []
        while x:
            res.append(x & 1)
            x = x >> 1
        return "".join(map(str, res[::-1] or [0]))

    def baseNeg22(self, x):
        res = []
        while x:
            res.append(x & 1)
            x = -(x >> 1)
        return "".join(map(str, res[::-1] or [0]))


"""
Explanation
Inspired by @wen_han, I'd like to share this solution.
First we find a big number x with its binary value 10101...10101
x needs to be bigger than 10^9 so it can cover all input N.

Here I choose mask = 2^32 / 3 = 1431655765 and we have mask > 10^9

The 01 pattern binary number have 2 special characters:

Because it has 0 on all even bits, which are negative bits in base -2,
it has same value in base 2 and base -2.
When we bitwise operation mask ^ x, we will change some 1 to 0 on odd position,
and change some 0to 1 on even position.
In the view of base -2, we actually mask - x.
So mask ^ x in base 2 is same as mask - x in base -2.
Take advantage of this observation:
mask ^ (mask - x) in base 2 is same as mask - (mask - x) = x in base -2.
So we get the result of this problem.


Example
N = 3 has reault 00111 in base -2.

N = 3 = 00011
mask = 21 = 10101
mask - N = 18 = 10010
mask ^ (mask - N) = 00111


Complexity
1431655765 ^ (1431655765 - N) is O(1)
Transform of binary string,
I'll say O(1) for small integer,
O(logN) for big number.
"""

class Solution2:
    def baseNeg2(self, N):
        return bin(1431655765 ^ (1431655765 - N))[2:]

