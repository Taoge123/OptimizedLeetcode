"""

Intuition:
Considering how to change Y to X
Opertation 1: Y = Y / 2 if Y is even
Opertation 2: Y = Y + 1


Explanation:
Obviously,
If Y <= X, we won't do Y / 2 anymore.
We will increase Y until it equals to X

So before that, while Y > X, we'll keep reducing Y, until it's smaller than X.
If Y is odd, we can do only Y = Y + 1
If Y is even, if we plus 1 to Y, then Y is odd, we need to plus another 1.
And because (Y + 1 + 1) / 2 = (Y / 2) + 1, 3 operations are more than 2.
We always choose Y / 2 if Y is even.


Why it's right
Actually, what we do is:
If Y is even, Y = Y / 2
If Y is odd, Y = (Y + 1) / 2

We reduce Y with least possible operations, until it's smaller than X.

And we know that, we won't do Y + 1 twice in a row.
Becasue we will always end with an operation Y / 2.

2N times Y + 1 and once Y / 2 needs 2N + 1 operations.
Once Y / 2 first and N times Y + 1 will end up with same result, but needs only N + 1 operations.


Time complexity
We do Y/2 all the way until it's smaller than X,
time complexity is O(log(Y/X)).


991.Broken-Calculator
首先，当X>Y时，容易判断出我们只有对X持续地减一才能实现Y。

当X<Y时，我们也容易判断出，如果Y是奇数，那么最后一步操作一定是-1（否则x2是得不到奇数的），所以我们只需要递归考虑brokenCalc(X,Y+1)即可。

那么如果Y是偶数呢？我们将任意从X变换成Y的过程，可以分为两个大类：第一类是最后若干步是-1，第二类是最后若干步是x2。这两类方法可以分别写作：

(a) X ... [x2 x2 ... x2][-1 -1 ... -1] = Y
(b) X ... [-1 -1 ... -1][x2 x2 ... x2] = Y
注意，我们并不关心“最后若干步”具体是有多少步。所以上面的两种方法就可以代表任意从X到Y的变换过程。其中，第一种方法最后的若干步-1一定是偶数次，假设是2k。
我们容易看出第一种方法其实是不高效的，因为通过简单的分解就可以看出X ... [x2 x2 ... x2][-1 -1 ... -1]{2k个}等效于X ... [x2 x2 ...][-1 -1 ... -1]{k个} x2。而前者最后需要1+2k步，而后者只需要k+1步。

所以结论是，当Y>X并且Y是偶数的时候，方法(a)是不高效的，不如等效的方法(b)。也就是说，从X到Y最高效的变化方法，最后一步应该是x2而不是-1.
因此下一步我们只需要递归考虑brokenCalc(X,Y/2)即可。

"""

"""
X -1...-1-1-1...-1-1 *2*2...*2*2 = Y
X *2*2...*2*2 -1...-1-1-1...-1-1 = Y

*2 -1-1-1--1-1- = [-1-1-1-1-1] X 2 is better
         k           k//2

"""


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y
        if Y % 2 == 1:
            return self.brokenCalc(X, Y + 1) + 1
        else:
            return self.brokenCalc(X, Y // 2) + 1


class SolutionLee:
    def brokenCalc(self, X: int, Y: int) -> int:

        res = 0
        while Y > X:
            if Y % 2 == 1:
                Y += 1
                res += 1
            else:
                Y //= 2
                res += 1

        return res + (X - Y)


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            # Base case, also known as stop condition
            return X - Y

        else:
            if Y % 2 == 1:
                # Y is odd
                return 1 + self.brokenCalc(X, Y + 1)
            else:
                # Y is even
                return 1 + self.brokenCalc(X, Y // 2)




