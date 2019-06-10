
"""
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/discuss/226166/Python-O(32)-using-Fibonacci

Given a positive integer n, find the number of non-negative integers less than or equal to n,
whose binary representations do NOT contain consecutive ones.

Example 1:
Input: 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
Note: 1 <= n <= 109
"""
"""
 # Case 1 -  Leading 1's are consecutive
    #   0b001101010
    #   =>
    #   0b0010xxxxx    Find all possibility up to 7 digits
    #
    # Case 2 - Leading 1 is not consecutive
    #   0b001010100
    #   =>
    #   0b00010xxxx    Find all possibility up to 6 digits
    #   0b0010010xx    Find all possibility up to 4 digits
    #   0b001000010    Find all possibility up to 2 digit
    #   0b001000000    1
    #
    # Mixed Cases
    #   0b010011010
    #   =>
    #   0b0010xxxxx    Find all possibility up to 7 digits
    #   0b000010xxx    Find all poossibiity up to 5 digits
    
    #               n digits      add     total f(n)
    #   0b00000     0 digit     +1          1
    #   0b00001     1 digit     +1          2
    #   0b00010     2 digit     +f(0)       3
    #   0b0010_     3 digit     +f(1)       5
    #   0b010__     4 digit     +f(2)       8
    #   0b10___     5 digit     +f(3)       13
    #
    #   This is Fibonacci
"""
"""
x, y are used to calculate Fibonacci numbers.
num & 1 and num & 2 will check if num ends with 11 in binary.

Why can I use fibonacci numbers?
a(n) = the number of valid integers less than 2^n
a(5) = the number of valid integers less than 0b100000
It equals to the number of valid integers in [0b0, 0b10000[ and in [0b10000, 0b11000[.
The number of valid integers [0b0, 0b10000[, which is like '0b0XXXX', equals to a(4).
The number of valid integers [0b10000, 0b11000[, which is like '0b101XX', equals to a(3).
So a(5) = a(4) + a(3).
This rule is the same for other values of n, and it is the same as Fibonacci numbers recurrence relation definition.
"""

class SolutionLee:
    def findIntegers(self, num):
        x, y = 1, 2
        res = 0
        num += 1
        while num:
            if num & 1 and num & 2:
                res = 0
            res += x * (num & 1)
            num >>= 1
            x, y = y, x + y
        return res


"""
Build a tree to consider all possible number.

Let 1.and 0 for each bit be tree node

compress to 4 possible result for each bit:

all bit before cur is less than num and no continues 1 and cur bit is at one.
all bit before cur is less than num and no continues 1 and cur bit is at zero.
cur and prev bit is equal to num.
larger than num or has contiunes '1'.
then run through the tree.


Brilliant and concise solution! Let's push it to the top of all solutions :)

It took me a while to figure it out, so I added some comments in the code below. 
To better illustrate the idea of this solution, we can check this example:

num = (10110)2

prefix = 1
smallerPrefixEnding0 = 1, it consists of candidates {0}
smallerPrefixEnding1 = 0,
isPrefixValid = true, it consists of candidates {1}

prefix = 10
smallerPrefixEnding0 = 1, it consists of candidates {00}
smallerPrefixEnding1 = 1, it consists of candidates {01}
isPrefixValid = true, it consists of candidates {10}

prefix = 101
smallerPrefixEnding0 = 3, it consists of candidates {000,010,100}
smallerPrefixEnding1 = 1, it consists of candidates {001}
isPrefixValid = true, it consists of candidates {101}

prefix = 1011
smallerPrefixEnding0 = 5, it consists of candidates {0000,0100,1000,0010,1010}
smallerPrefixEnding1 = 3, it consists of candidates {0001,0101,1001}
isPrefixValid = false, it consists of candidates {}

prefix = 10110
smallerPrefixEnding0 = 8, it consists of candidates {00000,01000,10000,00100,10100,00010,01010,10010}
smallerPrefixEnding1 = 5, it consists of candidates {00001,01001,10001,00101,10101}
isPrefixValid = false, it consists of candidates {}

At the end, we return 8 + 5 = 13.
"""
class Solution1:
    def findIntegers(self, num):
        end0, end1 = 0, 0
        no_adj_1s = True
        prevbit = 0
        for i in reversed(range(num.bit_length())):
            end0, end1 = end0+end1, end0
            currbit = (num>>i) & 1
            if no_adj_1s and currbit:
                end0 += 1
            if currbit and prevbit:
                no_adj_1s = False
            prevbit = currbit
        return end0 + end1 + no_adj_1s


"""
Say X is the given number, and A = a list of that number in binary. 
For example, if X = 1234 = 0b10011010010, A = [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0].

We will perform a 'flag-dp': let dp[i][flag] = the answer for the number corresponding to A[i:], 
where flag = 1 if we have written a lower number than A[i] at some point in our writing process 
(and can now freely write higher numbers), else flag = 0.

1234 has bitlength 11. With that example, we would try to write 11 binary digits 
(without writing consecutive 1s) from left to right, 
such that the number it represents is less than or equal to 1234.

If our flag is down (flag = 0), then we cannot write a higher number than A[i]. 
If A[i] = 1, then we can write '10' or '0'. If A[i] = 0, we can only write '0'. 
We should check as we write a zero, to lower our flag if we wrote a lower number. 
This is what dp[.][A[i]] and dp[.][A[i+1]] do.
If our flag is up, then we can freely write '10' or '0'.
"""
"""
f(n) is what we want, means the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.
g(n) is the part of f(n) whose end digit is 0
check(n) returns 1 if n doesn't contain consecutive 1s, otherwise 0.

Since [0, 2n+1] are from appending 0 or 1 at the end of numbers in [0, n]

For i in f(n),
If i ends with 0, then appending 0 or 1 gets (i<<1) and (i<<1)+1 both gives are valid numbers, so this part contributes 2*g(n) numbers for f(2n+1)
If i ends with 1, then appending 0 or 1 gets (i<<1) and (i<<1)+1, only (i<<1) gives a valid number, so this part contributes f(n)-g(n) numbers(all f(n) substracts numbers in f(n) that ends with 0) for f(2n+1)

So f(2n+1)=2*g(n)+f(n)-g(n)=f(n)+g(n).
and f(2n)=f(n)+g(n)-check(2n+1)

As for g(2n), for each number in g(2n), it comes from appending a 0 for any number x in f(n), no matter x ends with 0 or 1, both are valid. So g(2n)=f(n), 2n+1 is an odd number, so g(2n+1)=g(2n)=f(n) too.

Now we can use the properties to get f(n).

If n is odd, f(n)=f(n>>1)+g(n>>1)
If n is even, f(n)=f(n>>1)+g(n>>1)-check(2n+1)

The basic case is f(0)=1.

As for g(n), g(n)=f(n>>1)

Following is my python code:
"""
class Solution2:
    def findIntegers(self, X):
        A = map(int, bin(X)[2:])
        N = len(A)
        dp = [[0, 0] for _ in range(N + 2)]
        dp[N] = dp[N + 1] = [1, 1]

        for i in range(N - 1, -1, -1):
            dp[i][0] = dp[i + 1][A[i]] + A[i] * dp[i + 2][i + 1 < N and A[i + 1]]
            dp[i][1] = dp[i + 1][1] + dp[i + 2][1]

        return dp[0][0]


class Solution3:
    def findIntegers(self, num):
        num, sub = bin(num)[2:], 0
        zero, one = [1] * len(num), [1] * len(num)
        for i in range(1, len(num)):
            zero[i], one[i] = zero[i - 1] + one[i - 1], zero[i - 1]
        for i in range(1, len(num)):
            if num[i] == num[i - 1] == "1": break
            if num[i] == num[i - 1] == "0": sub += one[-1 - i]
        return zero[-1] + one[-1] - sub



