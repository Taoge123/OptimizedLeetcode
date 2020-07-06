
"""
https://leetcode.com/problems/check-if-it-is-a-good-array/discuss/419368/JavaC%2B%2BPython-Chinese-Remainder-Theorem

如果听说过中国剩余定理（或者叫孙子定理）的话，可以直接知道结论。

第一次遇到的话，自己分析一下也容易找到线索。题意就是说，是否存在一段subarray，里面元素的线性组合能够得到1？
那么以三个元素[a1,a2,a3]为例子，我们想看看是否能有三个整数k1,k2,k3使得k1a1+k2a2+k3*a3=1.

如果a1,a2,a3存在一个大于1的公约数b，也就是说a1,a2,a3都是b的倍数，
那么我们这个线性组合可以写成k1*m1*b+k2*m2*b+k3*m3*b，合并一下就是(k1*m1+k2*m2+k3*m3)*b，
显然永远都不可能是1.所以结论是：要使得一段subarray里面元素的线性组合能够得到1，这些元素的最大公约数一定只能是1，
也就是说这些元素里面必然有两个元素互质。

因此，在整个数组array里面，只要存在两个数互质，那么必然可以找到一个subarray（只要包括它们就行）满足题意。

要判断一个数组里面是否有两个互质，只要顺序取最大公约数（gcd)，这个gcd肯定会越算越小，直至为1的话，
那就说明经过的数字里面必然有两个是互质的。（这是因为取最大公约数的操作是有交换律性质的）
Explanation
If a % x = 0 and b % x = 0,
appareantly we have (pa + qb) % x == 0
If x > 1, making it impossible pa + qb = 1.

Well, I never heard of Bezout's identity.
Even though the intuition only proves the necessary condition,
it's totally enough.

The process of gcd,
is exactly the process to get the factor.
The problem just doesn't ask this part.


1250.Check-If-It-Is-a-Good-Array
如果听说过中国剩余定理（或者叫孙子定理）的话，可以直接知道结论。

第一次遇到的话，自己分析一下也容易找到线索。题意就是说，是否存在一段subarray，里面元素的线性组合能够得到1？
那么以三个元素[a1,a2,a3]为例子，我们想看看是否能有三个整数k1,k2,k3使得k1a1+k2a2+k3*a3=1.

如果a1,a2,a3存在一个大于1的公约数b，也就是说a1,a2,a3都是b的倍数，那么我们这个线性组合可以写成k1*m1*b+k2*m2*b+k3*m3*b，合并一下就是(k1*m1+k2*m2+k3*m3)*b，
显然永远都不可能是1.所以结论是：要使得一段subarray里面元素的线性组合能够得到1，这些元素的最大公约数一定只能是1，也就是说这些元素里面必然有两个元素互质。

因此，在整个数组array里面，只要存在两个数互质，那么必然可以找到一个subarray（只要包括它们就行）满足题意。

要判断一个数组里面是否有两个互质，只要顺序取最大公约数（gcd)，这个gcd肯定会越算越小，直至为1的话，那就说明经过的数字里面必然有两个是互质的。
（这是因为取最大公约数的操作是有交换律性质的）

a^b^c^d^e .... = (b^c)^a^d^e, 顺序无所谓


"""

class Solution2:
    def isGoodArray(self, nums):
        k = nums[0]
        for i in range(1, len(nums)):
            k = self.gcd(k, nums[i])
            if k == 1:
                return True
        return k == 1

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)




class Solution:
    def isGoodArray(self, nums):
        gcd = nums[0]
        for num in nums:
            while num:
                gcd, num = num, gcd % num
        return gcd == 1






