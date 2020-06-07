"""

More of the same approach:
233. Number of Digit One
357. Count Numbers with Unique Digits
600. Non-negative Integers without Consecutive Ones
788. Rotated Digits
902. Numbers At Most N Given Digit Set
1012 Numbers With Repeated Digits
1397. Find All Good Strings

At each recursive call (adding digit to less significant position) compute:

isPrefix - if the new number is the prefix of N
isBigger - if the new number will be bigger than N when we reach final position
digits - current digits of the new number
repeated - if there is already a repeated digit
Optimization - if there is already a repeated number and the current number
cannot be bigger than N when we reach the last position we can add 10 (for 10 digits)
to the result and every subresult gets multiplied by 10.

Intuition
Count res the Number Without Repeated Digit
Then the number with repeated digits = N - res

Similar as
788. Rotated Digits
902. Numbers At Most N Given Digit Set

Explanation:
Transform N + 1 to arrayList
Count the number with digits < n
Count the number with same prefix
For example,
if N = 8765, L = [8,7,6,6],
the number without repeated digit can the the following format:
XXX
XX
X
1XXX ~ 7XXX
80XX ~ 86XX
870X ~ 875X
8760 ~ 8765

Time Complexity:
the number of permutations A(m,n) is O(1)
We count digit by digit, so it's O(logN)
"""

"""
1. 我们计算<=N的数中没有重复数字的个数
2. 计算位数比N + 1小的数中没有重复数字的个数
3. 计算与N + 1相同位数，相同prefix但小于(N + 1)情况下, 没有重复数字的个数

例如：
1. digits = [8, 7, 6, 5]
2. 计算位数 < 4位没有重复数字的个数
   9 * P(9, 2) + 9 * P(9, 1) + 9 = 738
3. 计算相同prefix没有重复数字的个数:
   1xxx - 7xxx : 逐个考察1 - 7， 每一位P(9, 3)
   80xx - 86xx : 逐个考察0 - 6,  每一位P(8, 2)
   870x - 875x : 逐个考察0 - 5,  每一位P(6, 0)
   8760 - 8765

"""




class SolutionTLE:
    def numDupDigitsAtMostN(self, N: int) -> int:
        self.count = 0
        for i in range(1, 10):
            nums = [False for i in range(10)]
            nums[i] = True
            self.dfs(i, N, nums)
        return N - self.count

    def dfs(self, cur, N, nums):
        if cur > N:
            return
        self.count += 1
        for i in range(10):
            if not nums[i]:
                nums[i] = True
                self.dfs(cur * 10 + i, N, nums)
                nums[i] = False


"""
1012.Numbers-With-Repeated-Digits
此题本质就是求不大于N的、没有重复数字的数。简单的想法，可以用无脑的DFS，结果会超时。

超时的原因在于，比如N=782581676，如果第一位取了1，后面8位数字其实就是从[0，2-9]这些数字里面任取8个全排列。这就提示我们DFS的时候，不必在每一个分支都用递归来计算，适当的时候直接调用数学公式就行了。

所以本题的解包括两部分：对于M位数的上限，我们先注意考察一位数，两位数，直到M-1位数的解。这些解注定不会大于N，所以直接调用数学公式，计算用10个不同的数字如何排列出k位数的方案数。但需要注意，任何k位数，其首位都不能是0.

第二部分，就是考察M位数的解。主体框架就是DFS，每个位置逐一考察。第k个位置如果选择比num[k]小的数字，那么剩余的部分就可以用全排列来解。如果第k个位置选择了num[k]，那么就递归考察下一个位置。注意，一个必要条件是，第k个位置的选择不能在前k-1个位置上出现过，所以我们需要一个visited来记录使用过的数字，这是一个回溯的过程。

"""

class SolutionWisdom:
    def numDupDigitsAtMostN(self, N: int) -> int:
        self.count = 0
        num = list(str(N))
        num = [int(i) for i in num]
        # 先算出所有n-1位的permutation
        for k in range(1, len(num)):
            print(k, len(num) - (k + 1), self.perm(9, len(num) - (k + 1)))
            #第一位数必须是9, 因为用了一位了， 后面就是9位选一位
            self.count += 9 * self.perm(9, len(num) - (k + 1))

        digits = [False for i in range(10)]
        # 0代表最高位
        self.dfs(num, digits, 0)
        return N - self.count

    def dfs(self, num, digits, k):
        if k == len(num):
            self.count += 1
            return

        for i in range(10):
            # 最高位不能是0
            if k == 0 and i == 0:
                continue

            if digits[i] == True:
                continue

            if i < num[k]:
                # (k+1)代表已经用过多少数字了, 要减掉
                self.count += self.perm(10 - (k + 1), len(num) - (k + 1))
            elif i == num[k]:
                digits[i] = True
                self.dfs(num, digits, k + 1)
                digits[i] = False

    def perm(self, m, n):
        res = 1
        for i in range(n):
            res *= (m - i)
        return res






class Solution:
    def numDupDigitsAtMostN(self, N):
        nums = list(map(int, str(N + 1)))
        res = 0
        n = len(nums)

        for i in range(1, n):
            res += 9 * self.prob(9, i - 1)

        visited = set()
        for i, x in enumerate(nums):
            for y in range(0 if i else 1, x):
                if y not in visited:
                    res += self.prob(9 - i, n - i - 1)
            if x in visited:
                break
            visited.add(x)
        return N - res

    def prob(self, m, n):
        if n == 0:
            return 1

        return self.prob(m, n - 1) * (m - n + 1)



"""
此题本质就是求不大于N的、没有重复数字的数。简单的想法，可以用无脑的DFS，结果会超时。

超时的原因在于，比如N=782581676，如果第一位取了1，后面8位数字其实就是从[0，2-9]这些数字里面任取8个全排列。
这就提示我们DFS的时候，不必在每一个分支都用递归来计算，适当的时候直接调用数学公式就行了。

所以本题的解包括两部分：对于M位数的上限，我们先注意考察一位数，两位数，直到M-1位数的解。
这些解注定不会大于N，所以直接调用数学公式，计算用10个不同的数字如何排列出k位数的方案数。
但需要注意，任何k位数，其首位都不能是0.

第二部分，就是考察M位数的解。主体框架就是DFS，每个位置逐一考察。第k个位置如果选择比num[k]小的数字，
那么剩余的部分就可以用全排列来解。如果第k个位置选择了num[k]，那么就递归考察下一个位置。注意，一个必要条件是，
第k个位置的选择不能在前k-1个位置上出现过，所以我们需要一个visited来记录使用过的数字，这是一个回溯的过程。
"""



"""
https://leetcode.com/problems/numbers-with-repeated-digits/discuss/256866/Python-O(logN)-solution-with-clear-explanation

The number of non-repeated digits can be easily calculated with permutaiton. We only need to exclude all the non-repeated digits to get the answer.

Let's first consider about the cases where N=10^k
N=10
the free digits are marked as *, so we only need to consider about * and 1*

*: obviously all 1-digit numbers are non-repeated, so non-repeated number = 9
1*: we only need to consider about 1* <= 10, so non-repeated number = 1
Thus, the result for N=10 is:
N - #non_repeat(*) - #non_repeat(1*) = 10 - 9 - 1 = 0

N=100
the free digits are marked as *, so we only need to consider about *, **, and 1**

*: obviously all 1-digit numbers are non-repeated, so non-repeated number = 9
**: this can be calculated with permutation: leading digit has 9 options(1-9) and the last 1 digit has 10-1 options, thus the total permuation is 9 * permutation(9, 1)=81. i.e: non-repeated number = 81
1**: we only need to consider about 1**<=100, so non-repeated number =0
Thus, the result for N=100 is:
N - #non_repeat(*) - #non_repeat(**) - #non_repeat(1**) = 100 - 9 - 81 = 10

N=1000
#non_repeat(***) = 9 * permutation(9, 2) = 9 * 9 * 8 = 648
similarly, we can get:
N - #non_repeat(*) - #non_repeat(**) - #non_repeat(***) - #non_repeat(1***) = 1000 - 9 - 81 - 648 = 282

Now, let's consider a more general case:
N=12345
actually, we can get the count of non-repeated numbers by counting all non-repeated numbers in following patterns:

    *
   **
  ***
 ****
10***
11*** (prefix repeated, skip)
120**
121** (prefix repeated, skip)
122** (prefix repeated, skip)
1230*
1231* (prefix repeated, skip)
1232* (prefix repeated, skip)
1233* (prefix repeated, skip)
12340
12341 (prefix repeated, skip)
12342
12343
12344 (prefix repeated, skip)
12345
and use N to minus the count we will get the answer.

Reference implementation:

"""


class Solution2:
    def numDupDigitsAtMostN(self, N):
        num = str(N)
        n = len(num)
        num = list(map(int, num))
        res = N - 1
        prefix = 0
        for i in range(1, n):
            res -= self.noRepeat(i)

        for i in range(n):
            # when we fix the most significant digit, it
            # can't be zero
            if i:
                start = 0
            else:
                start = 1
            for j in range(start, num[i]):
                if self.repeated(prefix * 10 + j):
                    continue
                if i != n - 1:
                    res -= self.perm(10 - i - 1, n - 1 - i)
                else:
                    # optmized from res -= repeated(prefix*10+j)`
                    res -= 1
            prefix = prefix * 10 + num[i]
        return res + self.repeated(N)

        # given number n, see whether n has repeated number

    def repeated(self, n):
        n = str(n)
        return len(set(n)) != len(n)

    def perm(self, n, k):
        res = 1
        for i in range(k):
            res *= (n - i)
        return res

    # calculate number of non-repeated n-digit numbers
    # note: the n-digit number can't start with 0
    # i.e: n_digit_no_repeat(2) calculates the non-repeated
    #   numbers in range [10, 99] (inclusive)
    def noRepeat(self, n):
        if n == 1:
            return 9
        else:
            return 9 * self.perm(9, n - 1)


N = 78368236
a = SolutionWisdom()
print(a.numDupDigitsAtMostN(N))
