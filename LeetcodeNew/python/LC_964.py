"""


964.Least-Operators-to-Express-Number
解法1：递归
这道题还是很有难度的。

首先我们要厘清本题的实质。根据四则混合运算的性质，我们可以将一串表达式看成是若干个乘除项的加减。对于所有的乘除项，其实无非就是那么几种：x/x,x,x*x,x*x*x,...其他的都不可能。为什么呢？首先，类似于x*x/x*x**x/x/x这种乘除混搭的形式，明显可以合并精简，这样设计显然浪费了操作。其次，类似于x/x/x/x/x这种除法操作多于乘法操作的形式，得到的结果一定是小数，如果整个表达式里包含了小数项，那么无论怎么操作都不可能得到最终target为整数的答案。

所以综上，本题的目的其实就是将target写成 a0*x^0 + a1*x^1 + a2*x^2 + ... ak*x^k的形式，要使得总操作符的数目最小。其中a0,a1,a2,...,ak都是整系数，但是可正可负。

我们容易知道，如果想要得到3*x^4,就是写成+x*x*x*x+x*x*x*x+x*x*x*x的形式，需要3*4=12个操作符（包括队首的那个正号）。如果想要得到2*x^5,就是写成+x*x*x*x*x+x*x*x*x*x的形式，需要2*5=10个操作符（因为要包括每个乘除项队首的那个正号）。总的来说，要得到ai*x^i，需要用到ai*i个操作符。唯一例外的就是i==0的时候，我们要得到一个x^0，反而需要两个字符+x/x。

OK，有了以上的铺垫，那么我们进入正题：如何确定ak呢？上面的分解形式target = a0*x^0 + a1*x^1 + a2*x^2 + ... ak*x^k，这与把一个数进行x进制分解何其相似。于是，我们应该想到会不会 ak = target / x^k，确定了ak之后，我们可以得到剩下的部分 remainder = target - ak*x^k，而这部分的最高次只能是k-1. 于是，递归的算法 helper(remainder,k-1) 就呼之欲出了。

显然，以上想法得到的是一个固定的分解方式，因为这种方法我们强制使得所有的ai>0。我们还可以怎么做呢？我们还可以尝试x^k的系数设置为(ak+1)，这样我们多出了remainder = (ak+1)*x^k-target这部分，没关系，我们依然可以一样递归处理，即处理 helper(remainder,k-1)即可，只不过得到的a_(k-1)需要反个符号就行了。

所以，我们可以设计递归函数 helper(target,k)，确定ak的系数（有两种方案，分别是a_k1 = target/x^k, a_k2=a_k1+1），然后剩下的部分继续调用 helper(remainder,k-1)，直至k==0为止。

最大的k是什么呢？注意应该是(int)log(target)/log(x)+1。也就是说x^k完全可能比target还大。比如 helper(75,11)的最佳方案就是 1*11^2 - 4*11^1 - 2*x^0.

另外，我们需要记忆化手段记录每次得到的helper(target,k)以缩短递归时间。此题的时间复杂度是2^{log(N)/log(x)}=O(N)，其中N是target的大小。

还有，最终答案要减去1，这是因为第一个乘除项的队首其实不需要正号。

解法2：DP
解法1中的一个缺陷是无法优化和剪枝，当所尝试的ai已经偏离“最优解”非常遥远时，整个递归过程仍然会持续进行到最低位（即i=0）。

如果结合一个数学结论，那么就可以进一步化解解法。那就是将target做标准的x进制分解：

target = am*x^m + ... ak*x^k + ... + a2*x^2 + a1*x^1 + a0*x^0 ，

假设本题最优的分解方式是：

target = bm*x^m + ... bk*x^k + ... + b2*x^2 + b1*x^1 + b0*x^0 ，

这个数学结论是：每一位上“真实”的最优系数只可能是ai或者ai+1。（证明略）

举个例子，如果第六位上b6=a6，那么我们认为其对第五位没有影响，第五位上b5可以根据上面的结论，放心取a5或者a5+1。如果第六位上b6=a6+1，那么第六位可以分解成a6*x^6+x*x^6，我们将后者的影响放在下一位上，使得第五位上的等效系数其实是b5+x。根据我们之前claim：第五位上的等效系数的最优解只能a5或者a5+1，因此可知b5的解只能是a5-x或者a5+1-x.

所以我们定义f[i]表示第i位上的等效系数是ai时（从最高位开始到第i位，下同）所需要的操作数；定义g[i]表示第i位上的等效系数是ai+1时所需要的操作数。我们有如下的递推关系：

f[i] = min(f[i+1]+a[i]*s,  g[i+1]+abs(a[i]-x)*s);
g[i] = min(f[i+1]+(a[i]+1)*s, g[i+1]+abs(a[i]+1-x)*s);
其中s表示第i位（也就是x^i）每一个单项式所需要的符号数：s=(i==0)?2:i。

最终的输出结果是f[0]，因为g[0]还需要后续的操作才能满足target，但是当前已经是最低位了。

这种方法的时间复杂度是log(N)，只需要从高到低one pass每一位的两种选择即可。

x//x == 1
x//x + x//x + ..... + x//x = 也可以等于19

target = a0*x^0 + a1*x^1 + a2*x^2 + a3*x^3 + ... + ai*x^i

+ai*x^i => ai*i
+a0*x^0 => +x//x + x//x + x//x => a0*2


196, 11
0*11^2 + 6*11^1 + 9*11^0 => 24
1*11^2 + 4*11^1 + 2*11^0 => 10

"""

import math


class SolutionMemo:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        self.table = {}
        T = math.log(target) // math.log(x) + 1
        # -1 because the first number will always be positive, no need a sign
        return int(self.dfs(x, target, T)) - 1

    def dfs(self, x, target, k):
        if k == 0:
            return target * 2
        if (target, k) in self.table:
            return self.table[(target, k)]
        a = target // pow(x, k)
        res1 = a * k + self.dfs(x, target - a * pow(x, k), k - 1)
        res2 = (a + 1) * k + self.dfs(x, abs(target - (a + 1) * pow(x, k)), k - 1)
        self.table[(target, k)] = min(res1, res2)
        return min(res1, res2)





class SolutionTLE:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        T = math.log(target) // math.log(x) + 1
        return int(self.dfs(x, target, T)) - 1

    def dfs(self, x, target, k):
        if k == 0:
            return target * 2

        a = target // pow(x, k)
        res1 = a * k + self.dfs(x, target - a * pow(x, k), k - 1)
        res2 = (a + 1) * k + self.dfs(x, abs(target - (a + 1) * pow(x, k)), k - 1)
        return min(res1, res2)








