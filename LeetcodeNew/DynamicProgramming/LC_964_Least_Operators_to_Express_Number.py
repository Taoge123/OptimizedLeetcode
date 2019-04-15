
"""
https://blog.csdn.net/lemonmillie/article/details/86628980
https://blog.csdn.net/zjucor/article/details/85221526
https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/0964._Least_Operators_to_Express_Number.md

# https://leetcode.com/problems/least-operators-to-express-number/discuss/208376/python2-O(log-target)-chinese
# https://leetcode.com/articles/least-operators-to-express-number/
https://zhanghuimeng.github.io/post/leetcode-964-least-operators-to-express-number/


Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ...
where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /).
For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happens before addition and subtraction.
It's not allowed to use the unary negation operator (-).
For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
We would like to write an expression with the least number of operators such that the expression equals the given target.
Return the least number of operators used.

Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.  The expression contains 5 operations.
Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.  The expression contains 8 operations.
Example 3:

Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.  The expression contains 3 operations.


Note:

2 <= x <= 100
1 <= target <= 2 * 10^8
"""
import math
import functools
import sys

"""
解法
无语辽，想了3个小时= =
这个就算能想出来也没法在面试的时候想出来……
首先要注意审题，没有括号意味着：

最后结果一定是x的i次方相加减（i>=0）
由于target是整数所以不可能有i<0
这样的话我们第一反应就是把target转换成x进制，得到：



"""

class Solution1:
    def leastOpsExpressTarget(self, x, target):
        # 由于不能有括号，所以每一位（x进制）必须是由自己组成或者由下一位减自己余数组成,所以首先短除法求出每一位的余数
        rl = list()
        while target:
            rl.append(target%x)
            target/=x
        n = len(rl)
        # 在个位的时候，必须用x/x表示1，所以*2，但其它位不用，所以单独先提出
        pos = rl[0] * 2
        neg = (x-rl[0]) * 2
        for i in range(1,n):
            # 正数表示时，可用自己+剩下的正数表示或者多加一个本位然后减去上一位的余数表示
            # 负数表示时，可用自己的余数加上剩下的正数表示或者用自己的余数+剩下的余数，但此时可以合并同级项减少运算符
            # 如在10进制下，86可表示为
            # 80 + 6 （6 为下一位正数表示
            # 80 + 10 - 4 （4 为下一位负数表示）
            # 100 - 20 + 6 （100-20为本位余数表示，6为下一位正数表示
            # 100 - 20 + 10 - 4 （100-20为本位余数表示，10 -4 为下一位余数表示
            # 在此时， 20 和 10注定为同一位且符号相反，可以省去两个符号（一个符号在该位用i 个符号表示（如100为第二位，所以表示为+10 * 10，用两个符号，在此时所有符号均带自己的正负号
            pos, neg = min(rl[i] * i + pos, rl[i] * i + i + neg), min((x - rl[i]) * i + pos, (x-rl[i]) * i + i + neg - 2 * i)
        # 因为在前面算法中所有位都带自己的正负号，所以第一位应该减去自己的符号，所以总量减1
        # 或者在余数表示法中，加上一个更高位的减去自己表示本位余数
        # 所以此题归根结底还是考察对进制的理解而不是简单的理解bfs, dfs，那样复杂度远远高于此，但是是对惯性思维者的一种挑战
        return min(pos-1, n+neg-1)


class Solution2:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        def cost(i):
            return 2 if i == 0 else i

        N = []  # x-based representation of target
        while target > 0:
            target, r = divmod(target, x)
            N.append(r)
        # For every i-th most significant digit `n`, it can be accounted either by
        # `n * cost(i)` or `(x - n) * cost(i) + cost(i + 1)`.
        # It may be proved (TODO: how?) that more operators are needed O.W., so the optimal
        #  value can be calculated digit by digit.

        # least operators required so far if there is no carry to the more significant digit
        nocarry = N[0] * cost(0)
        # least operators required so far if there is a carry to the more significant digit
        carry = (x - N[0]) * cost(0)
        for i, n in zip(range(1, len(N)), N[1:]):
            nocarry, carry = min(
                # 1. no carry from the previous && no carry to the next
                n * cost(i) + nocarry,
                # 2. carry from the previous && no carry to the next
                n * cost(i) + carry + cost(i)), \
                             min(
                                 # 3. no carry from the previous && carry to the next
                                 (x - n) * cost(i) + nocarry,
                                 # 4. carry from the previous && carry to the next
                                 (x - n) * cost(i) + carry + cost(i) - 2 * cost(i))
            # For case 4., there are redundant operators.
            # e.g. 100 - 20 + 10 - 4 which can be reduced to 100 - 10 - 4
            # Generally, there are 2 unnecessary operators.
        return min(nocarry, carry + cost(len(N))) - 1


"""
when k = 0:
   only two ways you can get the result. Add cur times x/x or add (cur - x) times x/x to x.
   for example, x = 3, cur = 2. 
   2 = 3/3 + 3/3 or 2 = 3 - 3/3.
when k != 0:
   assume origin target is called y, at every iteration yk and curk got. Then when k = 1.
   y = (y1*x + cur1)*x + cur0
   At time k = 0, we get:
       cur0 = + x/x + ... + x/x               (cur0 * 2 operators)
       cur0 = x - x/x - ... - x/x            ((x - cur0) * 2 operators)
   for same reason, cur1 also have this two statuations.

   cur1 is positive:
      y = (y1 * x + x/x + ... + x/x) * x + x/x + ... + x/x             // cur * k + pos
      y = (y1 * x + x/x + ... + x/x) * x + x - x/x - ... - x/x
        = (y1 * x + x/x + ... + x/x + x/x) * x - x/x - ... - x/x     // (cur + 1) * k + neg

      y = (y1 * x + x - x/x - ... - x/x - x/x) * x + x/x + ... + x/x             // (x - cur) * k + pos
      y = (y1 * x + x - x/x - ... - x/x - x/x) * x + x - x/x - ... - x/x
        = (y1 * x + x - x/x - ... - x/x) * x - x/x - ... - x/x     // (x - cur - 1) * k + neg
think about this example: 
14 = 3*3 + 3 + 2
   = 3*(4) + 2         // y0 = 4, cur0 = 2, k = 0
   = 3*(3*1 + 1) + 2       // y1 = 1, cur1 = 1, k = 1
   = 3*[3*(0 + 1) + 1] + 2  // y2 = 0, cur2 = 1, k = 2

when k = 1, what we should care is: 14 = 3*(3*1 + 【1) + 1 + 1】
ie. 3 * (1) + (2), things in () can be get by add or subtract
3 * (1) + (2) = 3 * (1) + (1 + 1)   // cur1 * k + pos
              = 3 * (1) + (3 - 1) = 3*(2) - 1      // (cur1 + 1) * k + neg
			  = 3 * (3 - 1 - 1) + (1 + 1) = 3*3 +【3*(-1-1) + 1 + 1】     // (x - cur1) * k + pos
			  // forget the first 3*3, it will be dealt at next time
			  = 3 * (3 - 1 - 1) + (3 - 1) = 3*3 +【3*(-1) + (3 -1)】  // [x - (cur1 + 1)] * k + neg
return min(pos, k + neg) - 1;
is equal to return min(pos - 1, k - 1 + neg);

As you can see, when we use positive version, we add the first '+' which should be subtracted.
When negitive version returned, addtion x^k is need, because only k-1 '*' between x^k, k - 1 + neg is OK.

"""

class SolutionLee:
    def leastOpsExpressTarget(self, x, y):
        pos = neg = k = 0
        while y:
            y, cur = divmod(y, x)
            if k:
                pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
            else:
                pos, neg = cur * 2, (x - cur) * 2
            k += 1
        return min(pos, k + neg) - 1


"""
The number of operators is the number of xs minus one. So the question asks about how many x are used.

If we use the x-sum of x*x, then it should be x*x*x instead, because, for example, 
when x=3, x*x+x*x+x*x used more x then x*x*x* does. Therefore, we use the term x^k at most x-1 times for any given k.

We start with target and try to decomposite it as the sum of terms x^k. Specially, for a given k, 
we can try add or minus i=0, 1, 2,...,x-1 times of the term x^k. The cost, i.e. the extra number of x involved, is equal to i*k.

Reduction rule:
dp[target] = min(dp[target + i * x^k] + i * k, dp[target - i * x^k] + i * k ) for i = 0,1,2,...,x-1

Python Code (DFS + memo, top-down DP):
"""

class Solutioin3:
    def leastOpsExpressTarget(self, x, target):
        f = [1]
        cost = [2]
        cnt = 1
        while f[-1] <= target:
            f.append(f[-1] * x)
            cost.append(cnt)
            cnt += 1
        # get the value and cost of x^k, for k = 1,2,....
        # bigger value first to speed up the decomposition
        f = f[::-1]
        cost = cost[::-1]

        if target == 0: return 1
        if target == 1: return 1

        dp = {0: 0}

        def dfs(target, s):
            if target in dp: return dp[target]
            if s == len(f): return float('inf')
            if s > 0 and abs(target) >= f[s - 1]: return float('inf')

            # every recursion tries to add/minus all possible number of x^s,
            # so the next iteration tries x^(s+1).
            tmp = dfs(target, s + 1)
            for i in range(1, x):
                tmp = min(tmp, i * cost[s] + dfs(target + i * f[s], s + 1))
                tmp = min(tmp, i * cost[s] + dfs(target - i * f[s], s + 1))
            dp[target] = tmp
            return tmp

        return dfs(target, 0) - 1

"""
It's obvious that the expression should be
c0*x^0 + c1*x^1 + ... + cn*x^n
And there is only one way to get x^0 by x / x, and it's the only use for divide operation.
Then regard target as a x base number(for example, the 3 base form of 19 is 201)
we split target into several parts, target = parts[0] * x^0 + parts[1] * x^1 + ... + parts[31] * x^31
We build our dp array, and define:

dp[i][0] means the minimun operations needed to form an expression whose answer is parts[i]*x^i+parts[i+1]*x^(i+1)+...+parts[31]*x^31
dp[i][1] means the minimun operations needed to form an expression whose answer is (parts[i]+1)*x^i+parts[i+1]*x^(i+1)+...+parts[31]*x^31
So:
Consider about generating parts[i]*x^i, you can get it by two ways (you will never generate parts[i] * x^i by some expression other than x^i):

x^i + x^i + ... + x^i (parts[i] times)
x^(i+1) - x^i - x^i - ... - x^i (x - parts[i] times)
And it's reason why dp[i][0] = min{dp[i+1][0] + i * parts[i], dp[i + 1][1] + i * (x - parts[i])} (don't forget to link them together with + or -)
For dp[i][1], follow the previous steps."""


"""
Suppose target has n digits in the form of (target)_x, for example: target = 501, (target)_5=4001,n=4。
Let a[i] represents the digits in (target)_x and we have target = sum(a[i]*x**i). For example: a[3] = 4。
To get x**i, we should use multis operators, where multis = i==1?1:i-1.
We can actually get a[i]*x**i from two different ways:
(1) Adding all a[i] x**is, which means 4*5**3 is represented by +5**3+5**3+5**3+5**3. The ith digits contributes a[i]*(multis+1) operators.
(2) Borrowing a x**(i+1), then a[i]*x**i is get by substracting x-a[i] x**is from one x**(i+1), 
which means a[4]*x**4+2*5**3 is represented by (a[4]+1)*x**(i+1)-5**3-5**3. 
The ith digits contributes (x-a[i])*(multis+1) operators.

Let f[i][0] be the minimum number of operators constructing the digits from i to n+1 when the ith digit isn't been borrowed 
(i.e. we have a[i] x**is rather than a[i]+1), and f[i][1] be the opposite.

f[i][0] = min(f[i+1][1]+(x-a[i])*(multis+1),f[i+1][0]+a[i]*(multis+1))
f[i][1] = min(f[i+1][1]+(x-a[i]-1)*(multis+1),f[i+1][0]+(a[i]+1)*(multis+1))

To reduce space cost, we can use a 1x2 array rather than (n+1)x2
"""

class Solution4:
    def leastOpsExpressTarget(self, x, target):

        n = int(math.log(target,x))
        mask = x**n
        last = [0,n+1]
        for i in xrange(n,-1,-1):
            d = target//mask
            multis = 2 if i==0 else i
            last = [min(last[1]+(x-d)*multis,last[0]+d*multis), min(last[1]+(x-d-1)*multis,last[0]+(d+1)*multis)]
            target = target % mask
            mask /=x
        return last[0]-1


"""
Explanation:
For any target, the expression could be written as:
a(0)*pow(x, n) + a(1)*pow(x, n-1) + ... + a(n-1)*pow(x, 1) + a(n)*(x/x)
Here, a(m) is an integer (neg or pos or 0). "x/x" is actually the shortest expression of target 1.
And I took (index, target) as the cache key. The parameter "index" is the maximum power index allowed in the current recursion.
"""
class Solution5:
    def leastOpsExpressTarget(self, x, target):

        cache = dict()
        ret = self.helper(x, target, math.ceil(math.log(target, x)), cache)
        return ret

    def helper(self, x, target, index, cache):
        if index == 0 or target == 1:
            return target * 2 - 1
        if (index, target) in cache:
            return cache[(index, target)]
        power = x**index
        count = target // power
        if target % power == 0:
            return index * count - 1
        low = index * count + \
            self.helper(x, target - power * count, index - 1, cache)
        high = index * (count + 1) + \
            self.helper(x, power * (count + 1) - target, index - 1, cache)
        cache[(index, target)] = min(low, high)
        return cache[(index, target)]


"""
the least number of moves to make x ^ k ( cost) is k (except when k = 0 then the cost is 1 because x ^ 0 = 1 = x/x). 
with any target we will try to find the biggest natural number i ( i >= 0) which x ^ i <= target 
and x ^ i is closest to the target. 
then the least number of moves to make the target will either is cost(i) + leastOpsExpressTarget(target - x ^i) 
or leastOpsExpressTarget (x ^(i+1) - target) if x ^ (i+1) <= 2 * target 
(because if is not, the new target will equal or greater than the old target and it will cost infinite loop 
cause we are trying to minize the new target). If x ^ i == target, just return the cost(i)
"""
class Solution6:
    def leastOpsExpressTarget(self, x, k):
        from functools import lru_cache
        cost = lambda i : i and i or 2
        @lru_cache(None)
        def dfs(target):
            i = math.floor(math.log(target, x))
            if x ** i == target : return cost(i)
            ans = cost(i) + dfs(target - x ** i)
            if x ** (i+1) < 2 * target:
                ans = min(ans, dfs(x ** (i+1) - target) + i + 1)
            return ans
        return dfs(k)-1


class Solution7:
    def leastOpsExpressTarget(self, x, target):

        n = int(math.log(target,x))
        mask = x**n
        last = [0,n+1]
        for i in xrange(n,-1,-1):
            d = target//mask
            multis = 2 if i==0 else i
            last = [min(last[1]+(x-d)*multis,last[0]+d*multis), min(last[1]+(x-d-1)*multis,last[0]+(d+1)*multis)]
            target = target % mask
            mask /=x
        return last[0]-1

"""
思路：

1一定是通过x/x得到，然后剩下的部分一定是x的倍数，除以x的余数一定通过1得到，所以比赛的时候一直想的是划分成若干层，
比如x = 3, target = 19：先求6+1，因为3*6+1=19，但是随着层数的嵌套，实际用了多少符号变得不好求了。

Discuss里的答案：独立考虑每个x的次幂使用的个数。具体来说：

求出x的整数次幂数组（一直求到比target大的那个数）A，然后从后往前考虑A，每次考虑用不用当前这个A[i]，
假设还剩下left需要求出来，那就可以有left/A[i]个A[i]，或者（left/A[i]）+1个A[i]（超过left用减法）

注意：对于每个次幂，前面会加一个符号，比如用3*3*3的时候，在算的时候用的是+3*3*3或者-3*3*3；然而最后算完之后要把前面那个多余的符号去掉，对应 elif y == 0:return -1 这行代码
"""

class Solution10:
    @functools.lru_cache(None)
    def leastOpsExpressTarget(self, x, y):

        k = int(math.log(y, x)) + 1
        def dfs(y, k):
            if k == 0:  return y + y - 1
            elif y == 0:return -1
            need, left = divmod(y, x**k)
            return min(dfs(left, k - 1) + need * k, dfs(x**k - left, k - 1) + (need + 1) * k)
        return dfs(y, k)


class Solution11:
    def leastOpsExpressTarget(self, x, y):

        k = int(math.log(y, x)) + 1
        memo = {}
        def dfs(y, k):
            if (y,k) in memo: return memo[(y,k)]
            if k == 0:  return y + y - 1
            elif y == 0:return -1
            need, left = divmod(y, x**k)
            res = min(dfs(left, k - 1) + need * k, dfs(x**k - left, k - 1) + (need + 1) * k)
            memo[(y,k)] = res
            return res
        return dfs(y, k)


class Solution12:
    class Solution:
        def leastOpsExpressTarget(self, x, target):
            # At this time, you can get target either by add target times x/x or
            # subtract (x - target) times x/x to x
            # For example, x = 3, target = 2. Then, 3/3 + 3/3 or 3 - 3/3 is possible result
            if x > target:
                return min(target * 2 - 1, (x - target) * 2)
            if x == target:  # just push x at the end
                return 0
            sums, times = x, 0
            while sums < target:  # this is gready, put as much as possible 'x'
                times += 1
                sums *= x
            if sums == target:  # one more 'x' you put, one more operator
                return times
            # when you have remainder, you have two choices, one is add, the other is subtract
            # for example, x = 3, target = 5. Then, 5 = 3 + 2 or 5 = 9 - 4
            l, r = sys.maxsize, sys.maxsize
            if sums - target < target:
                l = self.leastOpsExpressTarget(x, sums - target) + times  # using subtract
            r = self.leastOpsExpressTarget(x, target - (sums // x)) + times - 1  # using add
            return min(l, r) + 1  # No matter +/- used, one more operator is add



# 思路 2 - 时间复杂度: O(lg(Target))- 空间复杂度: O(lg(Target))******
# 加一下cache, 一行就够了@functools.lru_cache(None)

class Solution13:
    @functools.lru_cache(None)
    def leastOpsExpressTarget(self, x, target):
        # At this time, you can get target either by add target times x/x or
        # subtract (x - target) times x/x to x
        # For example, x = 3, target = 2. Then, 3/3 + 3/3 or 3 - 3/3 is possible result
        if x > target:
            return min(target * 2 - 1, (x - target) * 2)
        if x == target:  # just push x at the end
            return 0
        sums, times = x, 0
        while sums < target:  # this is gready, put as much as possible 'x'
            times += 1
            sums *= x
        if sums == target:  # one more 'x' you put, one more operator
            return times
        # when you have remainder, you have two choices, one is add, the other is subtract
        # for example, x = 3, target = 5. Then, 5 = 3 + 2 or 5 = 9 - 4
        l, r = sys.maxsize, sys.maxsize
        if sums - target < target:
            l = self.leastOpsExpressTarget(x, sums - target) + times  # using subtract
        r = self.leastOpsExpressTarget(x, target - (sums // x)) + times - 1  # using add
        return min(l, r) + 1  # No matter +/- used, one more operator is add


# 思路 3 - 时间复杂度: O(lg(Target))- 空间复杂度: O(lg(Target))******
class Solution14:
    def leastOpsExpressTarget(self, x, target):

        cost = list(range(28)) # log(target, x)最大为26.57, 因此我们可能需要幂为27
        cost[0] = 2 # x^0 = 1 = +x/x, 需要2个操作符

        @functools.lru_cache(None)
        def dp(power, target): # 当前幂次为power，要达到target
            if target == 0: return 0
            if target == 1: return cost[power]
            if power >= 27: return float('inf')

            t, r = divmod(target, x)
            return min(r * cost[power] + dp(power+1, t),
                       (x-r) * cost[power] + dp(power+1, t+1))

        return dp(0, target) - 1 # we have to remove the leading operator just like +x/x


class Solution15:
    def leastOpsExpressTarget(self, x, target):

        cost = list(range(30))
        cost[0] = 2

        self.cache = {}
        def dp(i, target):
            if i >= 30:
                return float('inf')
            if target == 0:
                return 0
            if target == 1:
                return cost[i]
            if (i, target) in self.cache:
                return self.cache[(i, target)]
            t, r = divmod(target, x)
            ans = min(r * cost[i] + dp(i + 1, t),
                     (x - r) * cost[i] + dp(i + 1, t + 1))
            self.cache[(i, target)] = ans
            return ans

        return dp(0, target) - 1


