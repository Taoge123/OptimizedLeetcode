
"""
x = x1^x2^x3^ ...^ xn
x != 0

xi, Ai = x1^x2^x3^ .(xi)..^ xn != 0

x1: A1 = x2^x3^x4...xn = 0
x2: A2 = x1^x3^x4...xn = 0
x3: A3 = x1^x2^x4...xn = 0
..
xn: A3 = x1^x2^x3...xn-1 = 0

(x1^x2^x3...xn) ^ (n-1) = 0 ^ (n)
x ^ (n-1) = 0 ^ (n)
n % 2 == 1
如果n is even, 我们不会那么惨, 一定能过过一轮

Should not be Hard problem
The solution can be only 3 lines and really simple.
It should be a medium problem.
Hard is kind of misleading.

Why [1, 2, 3] expect true
If xor == 0 at first for Alice, it is considered as Bob lose already!
I find this stupid idea just after contest and I think it doesn't make any sense.
It should complete this condition in the description.

Let's discuss it if we add this condition.
If xor == 0, Alice win directly.
If xor != 0 and length of numbers is even, Alice will win.

Beacause:
All numbers won't be the same. Otherwise xor will be equal to 0
If all numbers are not the same, It means there are at least 2 different numbers.
Alice can always erase a number different from current xor.
So Alice won't never lose this turn at this situation.

If we don't have the condition
Just return nums are not all 0 and length of nums is even

810.Chalkboard-XOR-Game
对于Alice而言，如果手头的X=x1^x2^x3^...^xn=0，那么算赢．

如果X!=0,因为XOR的运算具有交换律，所以最后必然可以化简为ai^Ai!=0的形式．其中ai是其中的某个元素xi，而Ai是除了xi以外所有元素的亦或和．如果Ai不是零的话，那么Alice取ai就可以了(因为留给对手的是Ai)．如果这个Ai是零的话，那么我们试图重新找一个a/A的组合，直到找到一个非零的Ai，于是Alice就可以取相应的ai．

那么会不会所有的Ai都是零呢？我们来分析一下．假设所有的Ai都是零．那么A1^A2^...^An=X^X^..^X (共n-1次)＝０．由此推出ｎ必须是奇数．根据逆否的性质，如果n是偶数的话，那么不可能所有的Ai都是零，于是Alice必然有此轮不输策略．

于是有意思的事情来了．如果n是偶数，Alice有不输的策略；轮到Bob的时候，n就是奇数；如果他侥幸能存活那一轮，再轮到Alice的时候，她面对的依然是n是偶数的情况，又有了不输的策略．这个轮回最多一直持续到Bob只剩下一个数可选，也就必输了．

所以，如果数列的总个数是偶数的话，对于先手（Alice)必赢．反之，Bob面对的总是偶数的情况，他就能必赢．

Leetcode Link

"""

class Solution:
    def xorGame(self, nums) -> bool:
        x = 0
        for num in nums:
            x ^= num
        if x == 0:
            return True
        return len(nums) % 2 == 0





