
"""
Given a positive integer N, return the number of positive integers
less than or equal to N that have at least 1 repeated digit.



Example 1:

Input: 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit
are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: 1000
Output: 262
"""

"""
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
For anyone who doesn't understand the function def A(), you can see the iterative version of it below.

        def A(m, n):
            res = 1
            for i in range(n):
                res *= m
                m -= 1
            return res
It means the permutation of m * (m-1) * ... * (m-(n-1)).

And for why use 9*A(9,i-1) instead of A(9,i), 
that's because there should be no leading 0, but the following digit can be 0.
恩，就是m个球里选n个出来有多少种排列。。。m！/（m-n）！

"""

class SolutionLee:
    def numDupDigitsAtMostN(self, N):
        L = map(int, str(N + 1))
        res, n = 0, len(L)

        def A(m, n):
            return 1 if n == 0 else A(m, n - 1) * (m - n + 1)

        for i in range(1, n): res += 9 * A(9, i - 1)
        s = set()
        for i, x in enumerate(L):
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += A(9 - i, n - i - 1)
            if x in s: break
            s.add(x)
        return N - res


"""
The corner case is too hard to manage...

count res as N - total number without duplicated digits.
turns into a math and permutation problem.

select m out of n
P(m, n): n! / (n-m)!

Algorithm:

lets say N has k digits.
1) count number less than k digits
lets say number with i digits
first digit 1 ~ 9, following option is 0 ~ 9 without first digit
count = 9 * P(i-1,9)

2) count number has k digits. 
Calculate digits with same prefix. 
Prefix cannot has duplicate digits.
for case like 77xxx, we should stop the calculation.
"""


class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        def f(n):
            if n == 0 or n == 1: return 1
            return f(n - 1) * n

        # pick m out of n, ordred matters
        def P(m, n):
            return f(n) // f(n - m)

        # N + 1 as padding.
        nums = [int(d) for d in str(N + 1)]
        K = len(nums)  # N has K digits
        cnt = 0  # number with no repeated val

        # count **postive number with digits less than K
        for i in range(1, K): cnt += 9 * P(i - 1, 9)

        # count number with K digits
        seen = set()  # seen digit
        for i in range(K):
            # prefix = nums[:i] + currentDigit
            # currentDigit < nums[i]
            for x in range(1 if i == 0 else 0, nums[i]):
                if x in seen: continue  # avoid duplication
                cnt += P(K - (i + 1), 10 - (i + 1))

            # since next iteration, prefix has duplicate digits, break
            if nums[i] in seen: break
            seen.add(nums[i])

        return N - cnt



"""
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

# given number n, see whether n has repeated number
def has_repeated(n):
    str_n = str(n)
    return len(set(str_n)) != len(str_n)

def permutation(n, k):
    prod = 1
    for i in range(k):
        prod *= (n-i)
    return prod

# calculate number of non-repeated n-digit numbers
# note: the n-digit number can't start with 0
# i.e: n_digit_no_repeat(2) calculates the non-repeated
#   numbers in range [10, 99] (inclusive)
def n_digit_no_repeat(n):
    if n == 1:
        return 9
    else:
        return  9 * permutation(9, n-1)

class Solution2:
    def numDupDigitsAtMostN(self, N):

        N_str = str(N)
        n_digit = len(N_str)
        digits = map(int, N_str)
        result = N - 1
        prefix = 0
        for i in range(1, n_digit):
            result -= n_digit_no_repeat(i)
        for i in range(n_digit):
            # when we fix the most significant digit, it
            # can't be zero
            start = 0 if i else 1
            for j in range(start, digits[i]):
                if has_repeated(prefix * 10 + j):
                    continue
                if i != n_digit-1:
                    result -= permutation(10-i-1, n_digit-1-i)
                else:
                    # optmized from `result -= has_repeated(prefix*10+j)`
                    result -= 1
            prefix = prefix*10 + digits[i]
        return result + has_repeated(N)

