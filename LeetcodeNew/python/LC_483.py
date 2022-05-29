"""

https://leetcode.cn/problems/smallest-good-base/solution/zui-xiao-hao-jin-zhi-er-fen-shu-xue-fang-frrv/

For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format.

Example 1:

Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.


Example 2:

Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.


Example 3:

Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.


Note:

The range of n is [3, 10^18].
The string representing n is always valid and will not have leading zeros.
"""

"""
First things first. Let's see the math behind it.

From given information, we can say one thing- Numbers will be of form-

n = k^m + k^(m-1) + ... + k + 1
=> n-1 = k^m + k^(m-1) + ... + k
=> n-1 = k (k^(m-1) + k^(m-2) + ... + k + 1) ...... [1]

Also, from n = k^m + k^(m-1) + ... + k + 1, we can say,
n-k^m = k^(m-1) + k^(m-2) + ... + k + 1 ...... [2]

from [1] and [2],

n-1 = k (n - k^m)
=>k^(m+1) = nk - n + 1

if you shuffle sides you will end up getting following form,

(k^(m+1) - 1)/(k - 1) = n .... [3]

Also from [1] note that, (n - 1) must be divisible by k.

We know that, n = k^m + k^(m-1) + ... + k + 1

=> n > k^m
=> m-th root of n > k .... [4]

[EDIT] -->

With inputs from @StefanPochmann we can also say, from binomial thorem, n = k^m + ... + 1 < (k+1)^m .... [5]
Therefore, k+1 > m-th root of n > k. .... from [4] and [5]
Thus ⌊m-th root of n⌋ is the only candidate that needs to be tested. [6]

<--

So our number should satisfy this equation where k will be our base and m will be (number of 1s - 1)

This brings us to the search problem where we need to find k and m.

Linear search from 1 to n does not work. it gives us TLE. So it leaves us with performing some optimization on search space.

From [6] we know that the only candidate that needs to be tested is, ⌊m-th root of n⌋

We also know that the smallest base is 2 so we can find our m must be between 2 and log2n else m is (n-1) [7]

That brings me to the code:
[EDIT] -- >


For a given m > 1:

From n = km + ... + k0 > km you get k < m-th root of n (as you said already).
From n = km + ... + k0 < (k+1)m (see binomial theorem) you also get k+1 > m-th root of n.

So k < m-th root of n < k+1. Thus ⌊m-th root of n⌋ is the only candidate that needs to be tested. As @hausch did here.

Edit: More explanations:

I think of the above k < x < k+1 (with x being the m-th root of n) as x being really close to the potentially existing k.
Rounding it down might be a working k, but integers larger than that can't be (because already x is larger than k)
and integers smaller also can't be (because x < k+1 shows that x is less than 1 too large,
so if we subtract 1 or more, we'd be too small).

You can also reverse the focus, though, and turn those inequations into x-1 < k < x. In other words,
k would have to be an integer between x-1 and x. So round down x to get the only integer in that little range.
Yeah ok, this is probably the easier viewpoint :-)

And to show km + ... + k0 < (k+1)m: One way to see it is that expanding (k+1)m gives you all those powers of k,
 most of them multiple times, for example (k+1)4 = k4+4k3+6k2+4k1+k0. The binomial theorem just makes that more formal,
 giving us (k+1)m = ∑i=0:m (m choose i)⋅ki. Here (m choose i) is at least 1, and larger than 1 when i is strictly between 0 and m
 (this is btw where "m > 1" comes into play, guaranteeing such an i). So we have (k+1)m = ∑i=0:m (m choose i)⋅ki > ∑i=0:m ki.

"""

import math

class Solution:
    # 二分
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        # 枚举 k进制 中 1 的个数，最多为 二进制 时的位数
        for i in range(num.bit_length(), 2, -1):
            # k^0 + k^1 + …… + k^(i-1) = n -- 通过二分法计算 k
            # kn - n = k^i - 1
            left, right = 2, num - 1
            while left <= right:
                mid = (left + right) // 2
                s = mid * num - num - pow(mid, i) + 1
                if s == 0:
                    return str(mid)
                elif s > 0:
                    left = mid + 1
                else:
                    right = mid - 1
        return str(num - 1)



class Solution2:
    def smallestGoodBase(self, n):
        n = int(n)
        max_m = int(math.log(n, 2))  # Refer [7]
        for m in range(max_m, 1, -1):
            k = int(n ** m ** -1)  # Refer [6]
            if (k ** (m + 1) - 1) // (k - 1) == n:
                # Refer [3]
                return str(k)

        return str(n - 1)




